interana-sdk Readme
============

This will contain a simplified SDK to enable easy access to the Interana APIs.
Being provided at a best-effort basis. So please use at your risk.

## High Level desciption of files

* **query_sdk\interana_client.py** - Python implementation of Interana SDK - Provides the Interana Object as a helper to query the Interana External API as documented [here](https://docs.interania.com/Guides/Reference/External_API%3A_query)

* **ingest_sdk** - TBD

* **ia_api_consumer.py** - Uses the Python SDK. Provides for further abstraction of the Interana Query API. Allows for easy access and validation to ensure that connectivity and results are as needed. Fork at will :)

## Usage

* Currently, the API Consumer utility only supports the Query APIs

* For the API Consumer script, there are three position parameters that need to be provided.
In addition, there are optional parameters that can be leveraged as well.

* To access the Atlassian cluster and do a simple count*, do:
./ia_api_consumer.py dr7AAV6SEd5GqkC734GwGwQuVgDTBhuG0sSHWb=fsE0k+AB6v3mJVnJuHMaMklt+3GcUeIR=xoCOAQLHCCZlTPjEqazw0000 atlassian-staging.interana.com atl_test_whitelist
