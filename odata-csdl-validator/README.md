[![Build Status](https://travis-ci.com/DMTF/Redfish-Tools.svg?branch=master)](https://travis-ci.com/github/DMTF/Redfish-Tools)
<p align="center">
  <img src="http://redfish.dmtf.org/sites/all/themes/dmtf2015/images/dmtf-redfish-logo.png" alt="DMTF Redfish" width=180>

# OData CSDL validator

Copyright 2016-2021 Distributed Management Task Force, Inc. All rights reserved.

## Contents

* [About](#about)
* [Installation](#installation)
* [Usage](#usage)
* [Examples](#examples)
* [Processing](#processing)

## About

The **OData CSDL validator** &mdash; [`odata_validator.py`](odata_validator.py "odata_validator.py") &mdash; is a Python tool that parses OData-formatted metadata to validate that it conforms to [OData V4.0](https://www.odata.org/documentation/ "https://www.odata.org/documentation/").

## Installation

1. Clone the `Redfish-Tools` repository:

   ```bash
   % git clone git@github.com:DMTF/Redfish-Tools.git
   % git remote add upstream git@github.com:DMTF/Redfish-Tools.git
   ```
1. [Download and install Python](https://www.python.org/downloads/ "https://www.python.org/downloads/") on the machine from which you will run this tool.

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

The `odata_validator.py` tool takes a single `MetaData` parameter in one of the following formats:

| Format                                           | Example                                              |
| :----------------------------------------------- | :--------------------------------------------------- |
| Local path to a single XML metadata file.        | `test_metadata/ServiceRoot.xml`                      |
| Local path to a directory of XML metadata files. | `test_metadata`                                      |
| URL of an XML metadata file.                     | `http://redfish.dmtf.org/schemas/v1/ServiceRoot.xml` |

## Examples

Run the OData CSDL validator against a single XML metadata file:

```bash
% python3 odata_validator.py test_metadata/ServiceRoot.xml
```

Run the OData CSDL validator against the local path to a directory of XML metadata files:
         
```bash
% python3 odata_validator.py test_metadata
```

Run the OData CSDL validator against the URL of an XML metadata file:
         
```bash
% python3 odata_validator.py http://redfish.dmtf.org/schemas/v1/ServiceRoot.xml
```

## Processing

The OData CSDL validator parses and validates the specified file or files and all referenced files. If it finds an error, it prints the path to the metadata file that contains the error with a simple explanation of the error.

Example:

```text
MetaData:http://redfish.dmtf.org/schemas/v1/ServiceRoot.xml->DataServices->Schema:ServiceRoot->EntityType:ServiceRoot->Resource.1.0.0.Resource is not a valid QualifiedName
```
