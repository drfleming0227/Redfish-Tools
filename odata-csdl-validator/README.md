# OData CSDL validator

Copyright 2016-2021 Distributed Management Task Force, Inc. All rights reserved.

## About

The `odata_validator.py` tool is a Python tool that crawls through OData-formatted metadata, parses it, and validates that it conforms to OData V4.0.

## Installation

To install the OData CSDL validator, see [Installation](Redfish-Tools#installation "Redfish-Tools#installation").

## Usage

The `odata_validator.py` tool requires one parameter. The tool uses this parameter's value to find and validate the metadata files.

The parameter can be in one of the following formats:

1. The local path to a single XML metadata file.

    Example:

    ```
    odata\_validator.py test\_metadata/ServiceRoot.xml
    ```
1. The local path to a directory of XML metadata files.

    Example:

    ```
    odata\_validator.py test\_metadata
    ```
1. The URL of an XML metadata file. 
    
    Example:

    ```
    odata\_validator.py http://redfish.dmtf.org/schemas/v1/ServiceRoot.xml
    ```

## Processing

The `odata_validator.py` tool parses and validates the files and all referenced files.

If the tool finds an error, it prints the path to the metadata file in which the error was found and a simple explanation of the error.

Example:

```
MetaData:http://redfish.dmtf.org/schemas/v1/ServiceRoot.xml->DataServices->Schema:ServiceRoot->EntityType:ServiceRoot->Resource.1.0.0.Resource is not a valid QualifiedName
```
