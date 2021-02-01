[![Build Status](https://travis-ci.com/DMTF/Redfish-Tools.svg?branch=master)](https://travis-ci.com/github/DMTF/Redfish-Tools)
<p align="center">
  <img src="http://redfish.dmtf.org/sites/all/themes/dmtf2015/images/dmtf-redfish-logo.png" alt="DMTF Redfish" width=180>

# OData CSDL validator

Copyright 2016-2021 Distributed Management Task Force, Inc. All rights reserved.

The **OData CSDL validator** &mdash; [`odata_validator.py`](odata_validator.py "odata_validator.py") &mdash; is a Python tool that parses and validates that specified OData-formatted metadata file or files and all referenced files conform to [OData V4.0](https://www.odata.org/documentation/ "https://www.odata.org/documentation/").

## Contents

* [Installation](#installation)
* [Usage](#usage)
* [Examples](#examples)
* [Configuration](#configuration)
* [Processing](#processing)

## Installation

1. Clone the `Redfish-Tools` repository:

   ```zsh
   % git clone git@github.com:DMTF/Redfish-Tools.git
   % git remote add upstream git@github.com:DMTF/Redfish-Tools.git
   ```
1. [Download and install Python](https://www.python.org/downloads/ "https://www.python.org/downloads/") on the machine from which you will run this tool.

## Usage

The `odata_validator.py` tool takes a single `MetaData` argument in one of the following formats:

| Format                                           | Example argument                                     |
| :----------------------------------------------- | :--------------------------------------------------- |
| Local path to a [single XML metadata file](#single-xml-metadata-file).        | `test_metadata/ServiceRoot.xml`                      |
| Local path to a [directory of XML metadata files](#directory-of-xml-metadata-files). | `test_metadata`                                      |
| [URL of an XML metadata file](#url-of-an-xml-metadata-file).                     | `http://redfish.dmtf.org/schemas/v1/ServiceRoot.xml` |

```
usage: odata_validator.py [-h] MetaData

OData Validation Tool

positional arguments:
  MetaData    Path to the metadata to be parsed, could be a url (start with
              http), file or folder

optional arguments:
  -h, --help  show this help message and exit
```

## Examples

* [Single XML metadata file](#single-xml-metadata-file)
* [Directory of XML metadata files](#directory-of-xml-metadata-files)
* [URL of an XML metadata file](#url-of-an-xml-metadata-file)

### Single XML metadata file

Run the OData CSDL validator against a single XML metadata file:

```zsh
% cd Redfish-Tools/odata-csdl-validator
% python3 odata_validator.py ../../Redfish/test_metadata/ServiceRoot.xml
```

In this example, the **OData CSDL validator** parses and validates that the metadata in the `Redfish/test_metadata/ServiceRoot.xml` input file conforms to OData V4.0.

### Directory of XML metadata files

Run the OData CSDL validator against the local path to a directory of XML metadata files:
         
```zsh
% cd Redfish-Tools/odata-csdl-validator
% python3 odata_validator.py ../../Redfish/test_metadata
```

In this example, the **OData CSDL validator** parses and validates that the metadata in the files in the `/Redfish/test_metadata` input directory conform to OData V4.0.

### URL of an XML metadata file

Run the OData CSDL validator against the URL of an XML metadata file:
         
```zsh
$ cd Redfish-Tools/odata-csdl-validator
% python3 odata_validator.py http://redfish.dmtf.org/schemas/v1/ServiceRoot.xml
```

In this example, the **OData CSDL validator** parses and validates that the metadata in the `http://redfish.dmtf.org/schemas/v1/ServiceRoot.xml` input file conforms to OData V4.0.

## Configuration

None.

## Processing

The OData CSDL validator parses and validates that the specified OData-formatted metadata file or files and all referenced files conform to [OData V4.0](https://www.odata.org/documentation/ "https://www.odata.org/documentation/"). 

If the validator finds an error, it prints the path to the metadata file that contains the error with a simple explanation of the error.

Example:

```text
MetaData:http://redfish.dmtf.org/schemas/v1/ServiceRoot.xml->DataServices->Schema:ServiceRoot->EntityType:ServiceRoot->Resource.1.0.0.Resource is not a valid QualifiedName
```
