from __future__ import annotations
import pandas as pd
import time

from lndgrpc import LNDClient
from dataclasses import dataclass
from pb2dataframe import (
    ProtobufPath,
    messages_to_pandas,
    create_message_generator,
)


@dataclass
class Node:
    version: str
    commit_hash: str
    identity_pubkey: str
    block_height: int
    block_hash: str
    best_header_timestamp: str


@dataclass
class LndBaseResult:
    local_node: Node
    timestamp: int

    @classmethod
    def _init(cls, local_node: Node):
        timestamp = int(time.time())
        return cls(local_node=local_node, timestamp=timestamp)


@dataclass
class LndDescribeGraph(LndBaseResult):
    nodes: pd.DataFrame | None = None
    addresses: pd.DataFrame | None = None
    features: pd.DataFrame | None = None
    custom_records: pd.DataFrame | None = None
    edges: pd.DataFrame | None = None


@dataclass
class LndClosedChannels(LndBaseResult):
    channels: pd.DataFrame | None = None
    resolutions: pd.DataFrame | None = None


@dataclass
class LndForwardingHistory(LndBaseResult):
    forwarding_events: pd.DataFrame | None = None
    last_offset_index: int | None = None


@dataclass
class LndGetInfo(LndBaseResult):
    root: pd.DataFrame | None = None


@dataclass
class LndGetMissionControlConfig(LndBaseResult):
    root: pd.DataFrame | None = None


@dataclass
class LndListAccounts(LndBaseResult):
    accounts: pd.DataFrame | None = None


@dataclass
class LndListAddresses(LndBaseResult):
    account_with_addresses: pd.DataFrame | None = None
    addresses: pd.DataFrame | None = None


@dataclass
class LndListChannels(LndBaseResult):
    channels: pd.DataFrame | None = None
    pending_htlcs: pd.DataFrame | None = None


@dataclass
class LndListInvoices(LndBaseResult):
    invoices: pd.DataFrame | None = None
    htlcs: pd.DataFrame | None = None
    route_hints: pd.DataFrame | None = None
    custom_records: pd.DataFrame | None = None
    last_index_offset: int | None = None
    first_index_offset: int | None = None


@dataclass
class LndListLeases(LndBaseResult):
    locked_utxos: pd.DataFrame | None = None


@dataclass
class LndListPayment(LndBaseResult):
    payments: pd.DataFrame | None = None
    htlc_attempts: pd.DataFrame | None = None
    hops: pd.DataFrame | None = None
    custom_records: pd.DataFrame | None = None
    first_index_offset: int | None = None
    last_index_offset: int | None = None


@dataclass
class LndListPeers(LndBaseResult):
    peers: pd.DataFrame | None = None
    features: pd.DataFrame | None = None
    errors: pd.DataFrame | None = None


@dataclass
class LndListSweeps(LndBaseResult):
    transactions: pd.DataFrame | None = None
    output_details: pd.DataFrame | None = None
    previous_outpoints: pd.DataFrame | None = None
    transaction_ids: pd.DataFrame | None = None


@dataclass
class LndListUnspent(LndBaseResult):
    utxos: pd.DataFrame | None = None


@dataclass
class LndPendingChannels(LndBaseResult):
    pending_open_channels: pd.DataFrame | None = None
    pending_force_closing_channels: pd.DataFrame | None = None
    pending_htlcs: pd.DataFrame | None = None
    waiting_close_channels: pd.DataFrame | None = None
    total_limbo_balance: int | None = None


@dataclass
class LndPendingSweeps(LndBaseResult):
    pending_sweeps: pd.DataFrame | None = None


@dataclass
class LndQueryMissionControl(LndBaseResult):
    pairs: pd.DataFrame | None = None


@dataclass
class LndTransactionDetails(LndBaseResult):
    transactions: pd.DataFrame | None = None
    output_details: pd.DataFrame | None = None
    previous_outpoints: pd.DataFrame | None = None


class LndDataframeClient(LNDClient):
    DEFAULT_GRPC_MAX_FORWARDING_EVENTS = 10000
    DEFAULT_GRPC_MAX_INVOICES = 10000
    DEFAULT_GRPC_MAX_PAYMENTS = 10000

    @property
    def _local_node(self) -> Node:
        from lndgrpc.compiled.lightning_pb2 import GetInfoResponse

        response: GetInfoResponse = self.get_info()
        return Node(
            version=response.version,  # type: ignore
            commit_hash=response.commit_hash,  # type: ignore
            identity_pubkey=response.identity_pubkey,  # type: ignore
            block_height=response.block_height,  # type: ignore
            block_hash=response.block_hash,  # type: ignore
            best_header_timestamp=response.best_header_timestamp,  # type: ignore
        )

    def _remove_deprecated(
        self,
        dataframe: pd.DataFrame,
        columns_deprecated: list,
        remove_deprecated: bool,
    ) -> pd.DataFrame:
        df = dataframe
        if remove_deprecated:
            df = dataframe.drop(columns=columns_deprecated)

        return df

    def closed_channels_dataframe(
        self,
        disable_channels: bool = False,
        disable_resolutions: bool = False,
        **kwargs,
    ) -> LndClosedChannels:
        from lndgrpc.compiled.lightning_pb2 import ClosedChannelsResponse

        result = LndClosedChannels._init(self._local_node)

        paths: list[ProtobufPath] = []

        path_ids: dict[str, int] = {}

        if not disable_channels:
            id = len(paths)
            path_ids["channels"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="channels")

        if not disable_resolutions:
            id = len(paths)
            path_ids["resolutions"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="channels")
            paths[id].add_step(key="resolutions", foreign_key="chan_id")

        message = self.closed_channels(**kwargs)

        dataframes = messages_to_pandas(
            messages=message, message_type=ClosedChannelsResponse, paths=paths
        )

        for key in path_ids.keys():
            setattr(result, key, dataframes[path_ids[key]])

        return result

    def describe_graph_dataframe(
        self,
        disable_nodes: bool = False,
        disable_addresses: bool = False,
        disable_features: bool = False,
        disable_custom_records: bool = False,
        disable_edges: bool = False,
        **kwargs,
    ) -> LndDescribeGraph:
        from lndgrpc.compiled.lightning_pb2 import ChannelGraph

        result = LndDescribeGraph._init(self._local_node)

        paths: list[ProtobufPath] = []

        path_ids: dict[str, int] = {}

        if not disable_nodes:
            id = len(paths)
            path_ids["nodes"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="nodes")

        if not disable_addresses:
            id = len(paths)
            path_ids["addresses"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="nodes")
            paths[id].add_step(key="addresses", foreign_key="pub_key", enumerate=True)

        if not disable_features:
            id = len(paths)
            path_ids["features"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="nodes")
            paths[id].add_step(key="features", foreign_key="pub_key")

        if not disable_custom_records:
            id = len(paths)
            path_ids["custom_records"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="nodes")
            paths[id].add_step(
                key="custom_records", foreign_key="pub_key", enumerate=True
            )

        if not disable_edges:
            id = len(paths)
            path_ids["edges"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="edges")

        message = self.describe_graph(**kwargs)

        dataframes = messages_to_pandas(
            messages=message, message_type=ChannelGraph, paths=paths
        )

        for key in path_ids.keys():
            setattr(result, key, dataframes[path_ids[key]])

        return result

    def forwarding_history_dataframe(
        self,
        grpc_max_forwarding_events: int = DEFAULT_GRPC_MAX_FORWARDING_EVENTS,
        remove_deprecated: bool = True,
        disable_forwarding_events: bool = False,
        **kwargs,
    ) -> LndForwardingHistory:
        from lndgrpc.compiled.lightning_pb2 import ForwardingHistoryResponse

        result = LndForwardingHistory._init(self._local_node)

        paths: list[ProtobufPath] = []

        paths.append(ProtobufPath())

        path_ids: dict[str, int] = {}

        if not disable_forwarding_events:
            id = len(paths)
            path_ids["forwarding_events"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="forwarding_events", enumerate=True)

        messages = create_message_generator(
            func=self.forwarding_history,
            grpc_max_responses=grpc_max_forwarding_events,
            field_response_data="forwarding_events",
            field_response_last_index="last_offset_index",
            field_request_max="num_max_events",
            field_request_offset="index_offset",
            **kwargs,
        )

        dataframes = messages_to_pandas(
            messages=messages,
            message_type=ForwardingHistoryResponse,
            paths=paths,
        )

        result.last_offset_index = dataframes[0]["last_offset_index"].iloc[-1]
        for key in path_ids.keys():
            setattr(result, key, dataframes[path_ids[key]])

        return result

    def get_info_dataframe(self, **kwargs) -> LndGetInfo:
        from lndgrpc.compiled.lightning_pb2 import GetInfoResponse

        result = LndGetInfo._init(self._local_node)

        paths: list[ProtobufPath] = []
        paths.append(ProtobufPath())

        message = self.get_info(**kwargs)

        dataframes = messages_to_pandas(
            messages=message, message_type=GetInfoResponse, paths=paths
        )

        result.root = dataframes[0]

        return result

    def get_mission_control_config_dataframe(
        self, **kwargs
    ) -> LndGetMissionControlConfig:
        from lndgrpc.compiled.router_pb2 import GetMissionControlConfigResponse

        result = LndGetMissionControlConfig._init(self._local_node)

        paths: list[ProtobufPath] = []
        paths.append(ProtobufPath())

        message = self.get_mission_control_config(**kwargs)

        dataframes = messages_to_pandas(
            messages=message,
            message_type=GetMissionControlConfigResponse,
            paths=paths,
        )

        result.root = dataframes[0]

        return result

    def get_transactions_dataframe(
        self,
        start_height: int = 0,
        end_height: int = 0,
        remove_deprecated: bool = True,
        disable_transactions: bool = False,
        disable_output_details: bool = False,
        disable_previous_outpoint: bool = False,
        **kwargs,
    ) -> LndTransactionDetails:
        from lndgrpc.compiled.lightning_pb2 import TransactionDetails

        result = LndTransactionDetails._init(self._local_node)

        paths: list[ProtobufPath] = []

        path_ids: dict[str, int] = {}

        if not disable_transactions:
            id = len(paths)
            path_ids["transactions"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="transactions")

        if not disable_output_details:
            id = len(paths)
            path_ids["output_details"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="transactions")
            paths[id].add_step(key="output_details", foreign_key="tx_hash")

        if not disable_previous_outpoint:
            id = len(paths)
            path_ids["previous_outpoints"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="transactions")
            paths[id].add_step(key="previous_outpoints", foreign_key="tx_hash")

        message = self.get_transactions(
            start_height=start_height, end_height=end_height, **kwargs
        )

        dataframes = messages_to_pandas(
            messages=message, message_type=TransactionDetails, paths=paths
        )

        for key in path_ids.keys():
            setattr(result, key, dataframes[path_ids[key]])

        return result

    def list_accounts_dataframe(
        self, remove_deprecated: bool = True, **kwargs
    ) -> LndListAccounts:
        from lndgrpc.compiled.walletkit_pb2 import ListAccountsResponse

        result = LndListAccounts._init(self._local_node)

        paths: list[ProtobufPath] = []

        paths.append(ProtobufPath())
        paths[0].add_step(key="accounts")

        message = self.list_accounts(**kwargs)

        dataframes = messages_to_pandas(
            messages=message, message_type=ListAccountsResponse, paths=paths
        )

        result.accounts = dataframes[0]

        return result

    def list_addresses_dataframe(
        self,
        remove_deprecated: bool = True,
        disable_account_with_addresses: bool = False,
        disable_addresses: bool = False,
        **kwargs,
    ) -> LndListAddresses:
        from lndgrpc.compiled.walletkit_pb2 import ListAddressesResponse

        result = LndListAddresses._init(self._local_node)

        paths: list[ProtobufPath] = []

        path_ids: dict[str, int] = {}

        if not disable_account_with_addresses:
            id = len(paths)
            path_ids["account_with_addresses"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="account_with_addresses")

        if not disable_addresses:
            id = len(paths)
            path_ids["addresses"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="account_with_addresses")
            paths[id].add_step(key="addresses", foreign_key="name")

        message = self.list_addresses(**kwargs)

        dataframes = messages_to_pandas(
            messages=message, message_type=ListAddressesResponse, paths=paths
        )

        for key in path_ids.keys():
            setattr(result, key, dataframes[path_ids[key]])

        return result

    def list_channels_dataframe(
        self,
        remove_deprecated: bool = True,
        disable_channels: bool = False,
        disable_htlcs: bool = False,
        **kwargs,
    ) -> LndListChannels:
        from lndgrpc.compiled.lightning_pb2 import ListChannelsResponse

        result = LndListChannels._init(self._local_node)

        paths: list[ProtobufPath] = []

        path_ids: dict[str, int] = {}

        if not disable_channels:
            id = len(paths)
            path_ids["channels"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="channels")

        if not disable_htlcs:
            id = len(paths)
            path_ids["pending_htlcs"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="channels")
            paths[id].add_step(key="pending_htlcs", foreign_key="chan_id")

        message = self.list_channels(**kwargs)

        dataframes = messages_to_pandas(
            messages=message, message_type=ListChannelsResponse, paths=paths
        )

        for key in path_ids.keys():
            setattr(result, key, dataframes[path_ids[key]])

        return result

    def list_invoices_dataframe(
        self,
        grpc_num_max_invoices=DEFAULT_GRPC_MAX_INVOICES,
        remove_deprecated: bool = True,
        disable_invoices: bool = False,
        disable_htlcs: bool = False,
        disable_route_hints: bool = False,
        disable_custom_records: bool = False,
        **kwargs,
    ) -> LndListInvoices:
        from lndgrpc.compiled.lightning_pb2 import ListInvoiceResponse

        result = LndListInvoices._init(self._local_node)

        paths: list[ProtobufPath] = []

        root_id = 0
        paths.append(ProtobufPath())

        path_ids: dict[str, int] = {}

        if not disable_invoices:
            id = len(paths)
            path_ids["invoices"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="invoices")

        if not disable_htlcs:
            id = len(paths)
            path_ids["htlcs"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="invoices")
            paths[id].add_step(key="htlcs", foreign_key="add_index")

        if not disable_route_hints:
            id = len(paths)
            path_ids["route_hints"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="invoices")
            paths[id].add_step(key="route_hints", foreign_key="add_index")

        if not disable_custom_records:
            id = len(paths)
            path_ids["custom_records"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="invoices")
            paths[id].add_step(key="htlcs", foreign_key="add_index")
            paths[id].add_step(key="custom_records", foreign_key="htlc_index")

        messages = create_message_generator(
            func=self.list_invoices,
            grpc_max_responses=grpc_num_max_invoices,
            field_response_data="invoices",
            field_response_last_index="last_index_offset",
            field_request_max="num_max_invoices",
            field_request_offset="index_offset",
            **kwargs,
        )

        dataframes = messages_to_pandas(
            messages=messages, message_type=ListInvoiceResponse, paths=paths
        )

        result.first_index_offset = dataframes[root_id]["first_index_offset"].iloc[0]
        result.last_index_offset = dataframes[root_id]["last_index_offset"].iloc[-1]

        for key in path_ids.keys():
            setattr(result, key, dataframes[path_ids[key]])

        return result

    def list_leases_dataframe(
        self, remove_deprecated: bool = True, **kwargs
    ) -> LndListLeases:
        from lndgrpc.compiled.walletkit_pb2 import ListLeasesResponse

        result = LndListLeases._init(self._local_node)

        paths: list[ProtobufPath] = []
        paths.append(ProtobufPath())
        paths[0].add_step(key="locked_utxos")

        message = self.list_leases(**kwargs)

        dataframes = messages_to_pandas(
            messages=message, message_type=ListLeasesResponse, paths=paths
        )

        result.locked_utxos = dataframes[0]

        return result

    """
        ListPayments
    """

    def list_payments_dataframe(
        self,
        grpc_max_payments: int = DEFAULT_GRPC_MAX_PAYMENTS,
        remove_deprecated: bool = True,
        disable_payments: bool = False,
        disable_htlcs: bool = False,
        disable_hops: bool = False,
        disable_custom_records: bool = False,
        **kwargs,
    ) -> LndListPayment:
        from lndgrpc.compiled.lightning_pb2 import ListPaymentsResponse

        result = LndListPayment._init(self._local_node)

        paths: list[ProtobufPath] = []

        root_id = 0
        paths.append(ProtobufPath())

        path_ids: dict[str, int] = {}

        if not disable_payments:
            id = len(paths)
            path_ids["payments"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="payments")

        if not disable_htlcs:
            id = len(paths)
            path_ids["htlcs"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="payments")
            paths[id].add_step(key="htlcs", foreign_key="payment_index")

        if not disable_hops:
            id = len(paths)
            path_ids["hops"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="payments")
            paths[id].add_step(key="htlcs", foreign_key="payment_index")
            paths[id].add_step(key="route", foreign_key="attempt_id")
            paths[id].add_step(key="hops", enumerate=True)

        if not disable_custom_records:
            id = len(paths)
            path_ids["custom_records"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="payments")
            paths[id].add_step(key="htlcs", foreign_key="payment_index")
            paths[id].add_step(key="route", foreign_key="attempt_id")
            paths[id].add_step(key="hops", enumerate=True)
            paths[id].add_step(
                key="custom_records", foreign_key="chan_id", enumerate=True
            )

        messages = create_message_generator(
            func=self.list_payments,
            grpc_max_responses=grpc_max_payments,
            field_response_data="payments",
            field_response_last_index="last_index_offset",
            field_request_max="max_payments",
            field_request_offset="index_offset",
            **kwargs,
        )

        dataframes = messages_to_pandas(
            messages=messages, message_type=ListPaymentsResponse, paths=paths
        )

        result.first_index_offset = dataframes[root_id]["first_index_offset"].iloc[0]
        result.last_index_offset = dataframes[root_id]["last_index_offset"].iloc[-1]

        for key in path_ids.keys():
            setattr(result, key, dataframes[path_ids[key]])

        return result

    """
        ListPeers
    """

    def list_peers_dataframe(
        self,
        remove_deprecated: bool = True,
        disable_peers: bool = False,
        disable_features: bool = False,
        disable_errors: bool = False,
        **kwargs,
    ) -> LndListPeers:
        from lndgrpc.compiled.lightning_pb2 import ListPeersResponse

        result = LndListPeers._init(self._local_node)

        paths: list[ProtobufPath] = []

        path_ids: dict[str, int] = {}

        if not disable_peers:
            id = len(paths)
            path_ids["peers"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="peers")

        if not disable_features:
            id = len(paths)
            path_ids["features"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="peers")
            paths[id].add_step(key="features", foreign_key="pub_key")

        if not disable_errors:
            id = len(paths)
            path_ids["errors"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="peers")
            paths[id].add_step(key="errors", foreign_key="pub_key")

        message = self.list_peers(**kwargs)
        dataframes = messages_to_pandas(
            messages=message, message_type=ListPeersResponse, paths=paths
        )

        for key in path_ids.keys():
            setattr(result, key, dataframes[path_ids[key]])

        return result

    def query_mission_control_dataframe(
        self, remove_deprecated: bool = True, **kwargs
    ) -> LndQueryMissionControl:
        from lndgrpc.compiled.router_pb2 import QueryMissionControlResponse

        result = LndQueryMissionControl._init(self._local_node)

        paths: list[ProtobufPath] = []
        paths.append(ProtobufPath())
        paths[0].add_step(key="pairs")

        message = self.query_mission_control(**kwargs)

        dataframes = messages_to_pandas(
            messages=message,
            message_type=QueryMissionControlResponse,
            paths=paths,
        )

        result.pairs = dataframes[0]

        return result

    def list_sweeps_dataframe(
        self,
        verbose: bool = True,
        remove_deprecated: bool = True,
        disable_transactions: bool = False,
        disable_output_details: bool = False,
        disable_previous_outpoints: bool = False,
        disable_transaction_ids: bool = False,
        **kwargs,
    ) -> LndListSweeps:
        from lndgrpc.compiled.walletkit_pb2 import ListSweepsResponse

        result = LndListSweeps._init(self._local_node)

        message = self.list_sweeps(verbose=verbose, **kwargs)

        paths: list[ProtobufPath] = []

        path_ids: dict[str, int] = {}

        if not disable_transactions:
            id = len(paths)
            path_ids["transactions"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="transaction_details")
            paths[id].add_step(key="transactions")

        if not disable_output_details:
            id = len(paths)
            path_ids["output_details"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="transaction_details")
            paths[id].add_step(key="transactions")
            paths[id].add_step(key="output_details", foreign_key="tx_hash")

        if not disable_previous_outpoints:
            id = len(paths)
            path_ids["previous_outpoints"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="transaction_details")
            paths[id].add_step(key="transactions")
            paths[id].add_step(key="previous_outpoints", foreign_key="tx_hash")

        if not disable_transaction_ids:
            id = len(paths)
            path_ids["transaction_ids"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="transaction_ids")
            paths[id].add_step(key="transaction_ids")

        dataframes = messages_to_pandas(
            messages=message, message_type=ListSweepsResponse, paths=paths
        )

        for key in path_ids.keys():
            setattr(result, key, dataframes[path_ids[key]])

        return result

    def list_unspent_dataframe(
        self, remove_deprecated: bool = True, **kwargs
    ) -> LndListUnspent:
        from lndgrpc.compiled.walletkit_pb2 import ListUnspentResponse

        result = LndListUnspent._init(self._local_node)

        paths: list[ProtobufPath] = []
        paths.append(ProtobufPath())
        paths[0].add_step(key="utxos")

        message = self.list_unspent(min_confs=0, max_confs=None, **kwargs)  # type: ignore  # noqa: E501

        dataframes = messages_to_pandas(
            messages=message, message_type=ListUnspentResponse, paths=paths
        )

        result.utxos = dataframes[0]

        return result

    def pending_channels_dataframe(
        self,
        remove_deprecated: bool = True,
        disable_pending_open_channels: bool = False,
        disable_pending_force_closing_channels: bool = False,
        disable_pending_htlcs: bool = False,
        disable_waiting_close_channels: bool = False,
        **kwargs,
    ) -> LndPendingChannels:
        from lndgrpc.compiled.lightning_pb2 import PendingChannelsResponse

        result = LndPendingChannels._init(self._local_node)

        paths: list[ProtobufPath] = []

        root_id = 0
        paths.append(ProtobufPath())

        path_ids: dict[str, int] = {}

        if not disable_pending_open_channels:
            id = len(paths)
            path_ids["pending_open_channels"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="pending_open_channels")

        if not disable_pending_force_closing_channels:
            id = len(paths)
            path_ids["pending_force_closing_channels"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="pending_force_closing_channels")

        if not disable_pending_htlcs:
            id = len(paths)
            path_ids["pending_htlcs"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="pending_force_closing_channels")
            paths[id].add_step(key="pending_htlcs", foreign_key="channel")

        if not disable_waiting_close_channels:
            id = len(paths)
            path_ids["waiting_close_channels"] = id
            paths.append(ProtobufPath())
            paths[id].add_step(key="waiting_close_channels")

        message = self.pending_channels(**kwargs)

        dataframes = messages_to_pandas(
            messages=message, message_type=PendingChannelsResponse, paths=paths
        )

        result.total_limbo_balance = dataframes[root_id]["total_limbo_balance"].iloc[0]

        for key in path_ids.keys():
            setattr(result, key, dataframes[path_ids[key]])

        return result

    def pending_sweeps_dataframe(
        self, remove_deprecated: bool = True, **kwargs
    ) -> LndPendingSweeps:
        from lndgrpc.compiled.walletkit_pb2 import PendingSweepsResponse

        result = LndPendingSweeps._init(self._local_node)

        paths: list[ProtobufPath] = []
        paths.append(ProtobufPath())
        paths[0].add_step(key="pending_sweeps")

        message = self.pending_sweeps(**kwargs)

        dataframes = messages_to_pandas(
            messages=message, message_type=PendingSweepsResponse, paths=paths
        )

        result.pending_sweeps = dataframes[0]

        return result
