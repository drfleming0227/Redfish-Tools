[![Build Status](https://travis-ci.com/DMTF/Redfish-Tools.svg?branch=master)](https://travis-ci.com/github/DMTF/Redfish-Tools)
<p align="center">
  <img src="http://redfish.dmtf.org/sites/all/themes/dmtf2015/images/dmtf-redfish-logo.png" alt="DMTF Redfish" width=180>

# OData CSDL validator

Copyright 2016-2021 Distributed Management Task Force, Inc. All rights reserved.

The **OData CSDL validator** &mdash; [`odata_validator.py`](odata_validator.py "odata_validator.py") &mdash; is a Python tool that parses OData-formatted metadata to validate that it conforms to OData V4.0.

* [Installation](#installation)
* [Usage](#usage)
* [Processing](#processing)

## Installation

To install the OData CSDL validator, see [Installation](README.md#installation "README.md#installation").

## Usage

```
usage: odata_validator.py [-h] MetaData

OData Validation Tool

positional arguments:
  MetaData    Path to the metadata to be parsed, could be a url (start with
              http), file or folder

optional arguments:
  -h, --help  show this help message and exit
```

The `odata_validator.py` tool takes a single parameter in one of the following formats:

| Format                                 | Example                                      |
| :------------------------------------- | :------------------------------------------- |
| Local path to a single XML metadata file. | <pre lang="bash">odata\_validator.py test\_metadata/ServiceRoot.xml</pre> |
| Local path to a directory of XML metadata files. | <pre lang="bash">odata\_validator.py test\_metadata</pre> |
| URL of an XML metadata file. | <pre lang="bash">odata\_validator.py http://redfish.dmtf.org/schemas/v1/ServiceRoot.xml</pre> |

## Processing

The `odata_validator.py` tool parses and validates the files and all referenced files.

If the tool finds an error, it prints the path to the metadata file where it found the error and a simple explanation of the error.

Example:

```bash
MetaData:http://redfish.dmtf.org/schemas/v1/ServiceRoot.xml->DataServices->Schema:ServiceRoot->EntityType:ServiceRoot->Resource.1.0.0.Resource is not a valid QualifiedName
```
