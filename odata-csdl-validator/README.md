[![Build Status](https://travis-ci.com/DMTF/Redfish-Tools.svg?branch=master)](https://travis-ci.com/github/DMTF/Redfish-Tools)
<p align="center">
  <img src="http://redfish.dmtf.org/sites/all/themes/dmtf2015/images/dmtf-redfish-logo.png" alt="DMTF Redfish" width=180>

# OData CSDL validator

Copyright 2016-2021 Distributed Management Task Force, Inc. All rights reserved.

The **OData CSDL validator** &mdash; [`odata_validator.py`](odata_validator.py "odata_validator.py") &mdash; is a Python tool that parses OData-formatted metadata to validate that it conforms to [OData V4.0](https://www.odata.org/documentation/ "https://www.odata.org/documentation/").

* [Installation](#installation)
* [Usage](#usage)
* [Processing](#processing)

## Installation

To install the OData CSDL validator, see [Installation](../README.md#installation "../README.md#installation").

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

<table>
   <thead>
      <tr>
         <th align="left" valign="top">Format</th>
         <th align="left" valign="top">Example</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td align="left" valign="top"><p>Local path to a single XML metadata file.</p></td>
         <td align="left" valign="top">
            <pre lang="bash">python3 odata_validator.py test_metadata/ServiceRoot.xml</pre>
         </td>
      </tr>
      <tr>
         <td align="left" valign="top"><p>Local path to a directory of XML metadata files.</p></td>
         <td align="left" valign="top">
            <pre lang="bash">python3 odata_validator.py test_metadata</pre>
         </td>
      </tr>
      <tr>
         <td align="left" valign="top"><p>URL of an XML metadata file.</p></td>
         <td align="left" valign="top">
            <pre lang="bash">python3 odata_validator.py http://redfish.dmtf.org/schemas/v1/ServiceRoot.xml</pre>
         </td>
      </tr>
   </tbody>
</table>

## Processing

The `odata_validator.py` tool parses and validates the files and all referenced files.

If the tool finds an error, it prints the path to the metadata file where it found the error and a simple explanation of the error.

Example:

```text
MetaData:http://redfish.dmtf.org/schemas/v1/ServiceRoot.xml->DataServices->Schema:ServiceRoot->EntityType:ServiceRoot->Resource.1.0.0.Resource is not a valid QualifiedName
```
