Overview
==========

This will contain a simplified SDK to enable easy access to the Interana APIs.
Being provided at a best-effort basis. So please use at your risk.

High Level desciption of files
==============================

* **query_sdk\python\interana_query_sdk.py** - Python implementation of Interana SDK - Provides the Interana Object as a helper to query the Interana External API as documented [here](https://docs.interania.com/Guides/Reference/External_API%3A_query)

* **ingest_sdk** - TBD

* **query_sdk\ia_query_client.py** - Uses the Python SDK. Provides for further abstraction of the Interana Query API. Allows for easy access and validation to ensure that connectivity and results are as needed. Fork at will :)

Usage
=====

* For the IA Query Client (python) script, there are three position parameters that need to be provided.
In addition, there are optional parameters that can be leveraged as well.

* To access Interana's Demo Cluster and do a simple count*, do:

`cd ./query_sdk && pip install -r python/requirements.txt`

`./ia_query_client.py tffZR6q0fbVqSBbeuvvLllLMLV0KHbuH+/DjXo9K=ER0PY/qNh+hdjEh+16DcL5Gc=BfHTJ7dE64x06YFWMbtbqtcdO90000 demo2.interana.com music`

(note this will only work when you are on the Interana Corporate Network)

A sample output might look like this:

`$ ./ia_query_client.py tffZR6q0fbVqSBbeuvvLllLMLV0KHbuH+/DjXo9K=ER0PY/qNh+hdjEh+16DcL5Gc=BfHTJ7dE64x06YFWMbtbqtcdO90000 demo2.interana.com music`

`-------------------------------------------`

`Results recieved from Interana:`

`-------------------------------------------`

`{u'rows': [{u'values': [[u'All'], 4058569848.0]}], u'columns': [{u'type': u'array', u'label': [u'result']}, {u'type': u'number', u'label': u'measure_value'}]}`

`-------------------------------------------`

`End of Results`

`-------------------------------------------`

How to Contribute
==================
Simple. Feel free to jump in and contribute code. Some of the immediate next steps are:
* R implementation - work in progress
* MS-Excel (Windows only) implementation
* Jupyter Notebook
* Perl Implementation

Support & License
=======
## Support
The SDK is provided on a best-effort basis only. All support will be community-driven only.

## License
We have adopted the MIT license (see the file LICENSE.txt) for this project.
