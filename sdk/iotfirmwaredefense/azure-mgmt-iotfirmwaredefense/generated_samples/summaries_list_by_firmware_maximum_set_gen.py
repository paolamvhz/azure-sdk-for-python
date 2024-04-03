# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.iotfirmwaredefense import IoTFirmwareDefenseMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-iotfirmwaredefense
# USAGE
    python summaries_list_by_firmware_maximum_set_gen.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = IoTFirmwareDefenseMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    response = client.summaries.list_by_firmware(
        resource_group_name="FirmwareAnalysisRG",
        workspace_name="default",
        firmware_id="109a9886-50bf-85a8-9d75-000000000000",
    )
    for item in response:
        print(item)


# x-ms-original-file: specification/fist/resource-manager/Microsoft.IoTFirmwareDefense/stable/2024-01-10/examples/Summaries_ListByFirmware_MaximumSet_Gen.json
if __name__ == "__main__":
    main()
