"""
Dataclass representing one Tron transaction (like an actual transaction, not a TRC20 txn).
"""
from dataclasses import InitVar, asdict, dataclass, field, fields
from typing import Any, ClassVar, Dict, List, Optional, Tuple, Union

import pendulum
from rich.align import Align
from rich.console import Console, ConsoleOptions, RenderResult
from rich.panel import Panel
from rich.text import Text

from trongrid_extractoor.config import log
from trongrid_extractoor.helpers.address_helpers import coerce_to_base58
from trongrid_extractoor.helpers.rich_helpers import console, pretty_print
from trongrid_extractoor.helpers.string_constants import (BLOCK_TIMESTAMP, CONTRACT, CONTRACT_ADDRESS, PARAMETER,
     TRIGGER_SMART_CONTRACT, VALUE)
from trongrid_extractoor.models.function import Function

INTEGER_FIELDS = ['amount']


@dataclass(kw_only=True)
class TronTxn:
    # This should be populated before use.
    contract_method_info: ClassVar[Dict[str, Dict[str, Function]]] = {}

    transaction_id: str
    block_number: int
    ms_from_epoch: int  # block_timestamp
    raw_data: Dict[str, Any]
    internal_transactions: List[Dict[str, Any]]
    net_usage: int
    net_fee: int
    energy_fee: int
    energy_usage: int
    energy_usage_total: int
    raw_txn: Dict[str, Any]

    # Derived fields
    txn_type: Optional[str] = None
    contract_address: Optional[str] = None
    function: Optional[Function] = None
    method_id: Optional[str] = None
    method_args: Optional[Dict[str, int|str|bool]] = None

    def __post_init__(self) -> None:
        """Compute various derived fields."""
        self.seconds_from_epoch = int(self.ms_from_epoch / 1000.0)
        self.datetime = pendulum.from_timestamp(self.seconds_from_epoch, pendulum.tz.UTC)
        self.unique_id = self.transaction_id  # There is no log_index / event_index for an actual txn

        if CONTRACT not in self.raw_data:
            log.info(f"No contract in this txn '{self.transaction_id}'...")
            return

        contracts = self.raw_data[CONTRACT]
        contract = contracts[0]
        self.txn_type = contract['type']

        if not self.is_trigger_smart_contract_txn():
            return
        if len(contracts) > 1:
            raise ValueError(f"{self.transaction_id} has {len(contracts)} contracts in it...")

        try:
            parameter_value = contract[PARAMETER][VALUE]
            self.contract_address = coerce_to_base58(parameter_value.get(CONTRACT_ADDRESS))
            self.contract_owner = coerce_to_base58(parameter_value['owner_address'])
            function_call_data = parameter_value.get('data')
        except KeyError:
            console.print_exception()
            console.print(f"\n\n--------DATA START-----------")
            pretty_print(self.raw_txn)
            console.print(f"---------DATA-END-----------\n\n")
            raise

        # Function ID is the first 8 chars
        self.method_id = function_call_data[0:8]
        method_args = [arg.lstrip('0') for arg in self._split_data(function_call_data[8:])]

        if self.contract_address not in type(self).contract_method_info:
            return

        try:
            self.function = type(self).contract_method_info[self.contract_address][self.method_id]

            if len(method_args) != len(self.function.args):
                raise ValueError(f"Expected {len(self.function.args)} args but got {len(self.method_args)} for {self}")

            self.method_args = {
                arg.name: arg.coerce_arg_value(method_args[i], True)
                for i, arg in enumerate(self.function.args)
            }
        except Exception:
            console.print_exception()
            console.print(f"\n\n--------DATA START-----------")
            pretty_print(self.raw_txn)
            console.print(f"---------DATA-END-----------\n\n")
            raise

    @classmethod
    def from_event_dict(cls, txn: Dict[str, Any], method_ids: Optional[Dict[str, Any]] = None) -> 'TronTxn':
        """Build an event from the json data returned by Trongrid."""
        return cls(
            transaction_id=txn['txID'],
            block_number=txn['blockNumber'],
            ms_from_epoch=txn[BLOCK_TIMESTAMP],
            raw_data=txn['raw_data'],
            internal_transactions=txn['internal_transactions'],
            net_usage=txn['net_usage'],
            net_fee=txn['net_fee'],
            energy_fee=txn['energy_fee'],
            energy_usage=txn['energy_usage'],
            energy_usage_total=txn['energy_usage_total'],
            raw_txn=txn
        )

    def is_trigger_smart_contract_txn(self) -> bool:
        return TRIGGER_SMART_CONTRACT == self.txn_type

    def _split_data(self, data: str) -> List[str]:
        """The 'data' field is a concatenated list of args in one monster hex string."""
        return list(map(''.join, zip(*[iter(data)] * 64)))

    def __rich_console__(self, console: Console, options: ConsoleOptions) -> RenderResult:
        panel_txt = Text('[Tx] ').append(self.transaction_id, style='transaction_id').append('\n')
        panel_txt.append('[Contract] ').append(self.contract_address, style=CONTRACT_ADDRESS)
        panel_txt.append('   [Owner] ').append(self.contract_owner, style=CONTRACT_ADDRESS).append('\n')
        panel_txt.append('[Fxn] ').append(self.function.__rich__())
        yield(Panel(panel_txt, expand=False))

        for arg_name, arg_value in self.method_args.items():
            yield Text(f"    ").append(arg_name, style='green bold').append(': ').append(str(arg_value))
