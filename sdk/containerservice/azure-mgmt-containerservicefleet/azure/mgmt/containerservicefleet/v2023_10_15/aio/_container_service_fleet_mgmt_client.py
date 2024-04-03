# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, TYPE_CHECKING

from azure.core.pipeline import policies
from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient
from azure.mgmt.core.policies import AsyncARMAutoResourceProviderRegistrationPolicy

from .. import models as _models
from ..._serialization import Deserializer, Serializer
from ._configuration import ContainerServiceFleetMgmtClientConfiguration
from .operations import (
    FleetMembersOperations,
    FleetUpdateStrategiesOperations,
    FleetsOperations,
    Operations,
    UpdateRunsOperations,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential


class ContainerServiceFleetMgmtClient:  # pylint: disable=client-accepts-api-version-keyword
    """Azure Kubernetes Fleet Manager api client.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.containerservicefleet.v2023_10_15.aio.operations.Operations
    :ivar fleets: FleetsOperations operations
    :vartype fleets: azure.mgmt.containerservicefleet.v2023_10_15.aio.operations.FleetsOperations
    :ivar fleet_members: FleetMembersOperations operations
    :vartype fleet_members:
     azure.mgmt.containerservicefleet.v2023_10_15.aio.operations.FleetMembersOperations
    :ivar update_runs: UpdateRunsOperations operations
    :vartype update_runs:
     azure.mgmt.containerservicefleet.v2023_10_15.aio.operations.UpdateRunsOperations
    :ivar fleet_update_strategies: FleetUpdateStrategiesOperations operations
    :vartype fleet_update_strategies:
     azure.mgmt.containerservicefleet.v2023_10_15.aio.operations.FleetUpdateStrategiesOperations
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The ID of the target subscription. Required.
    :type subscription_id: str
    :param base_url: Service URL. Default value is "https://management.azure.com".
    :type base_url: str
    :keyword api_version: Api Version. Default value is "2023-10-15". Note that overriding this
     default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = ContainerServiceFleetMgmtClientConfiguration(
            credential=credential, subscription_id=subscription_id, **kwargs
        )
        _policies = kwargs.pop("policies", None)
        if _policies is None:
            _policies = [
                policies.RequestIdPolicy(**kwargs),
                self._config.headers_policy,
                self._config.user_agent_policy,
                self._config.proxy_policy,
                policies.ContentDecodePolicy(**kwargs),
                AsyncARMAutoResourceProviderRegistrationPolicy(),
                self._config.redirect_policy,
                self._config.retry_policy,
                self._config.authentication_policy,
                self._config.custom_hook_policy,
                self._config.logging_policy,
                policies.DistributedTracingPolicy(**kwargs),
                policies.SensitiveHeaderCleanupPolicy(**kwargs) if self._config.redirect_policy else None,
                self._config.http_logging_policy,
            ]
        self._client: AsyncARMPipelineClient = AsyncARMPipelineClient(base_url=base_url, policies=_policies, **kwargs)

        client_models = {k: v for k, v in _models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.operations = Operations(self._client, self._config, self._serialize, self._deserialize, "2023-10-15")
        self.fleets = FleetsOperations(self._client, self._config, self._serialize, self._deserialize, "2023-10-15")
        self.fleet_members = FleetMembersOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-10-15"
        )
        self.update_runs = UpdateRunsOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-10-15"
        )
        self.fleet_update_strategies = FleetUpdateStrategiesOperations(
            self._client, self._config, self._serialize, self._deserialize, "2023-10-15"
        )

    def _send_request(
        self, request: HttpRequest, *, stream: bool = False, **kwargs: Any
    ) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, stream=stream, **kwargs)  # type: ignore

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "ContainerServiceFleetMgmtClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details: Any) -> None:
        await self._client.__aexit__(*exc_details)
