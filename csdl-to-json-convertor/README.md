# CSDL-to-JSON converter

Copyright 2017-2021 Distributed Management Task Force, Inc. All rights reserved.

The **CSDL-to-JSON converter** &mdash; [`csdl-to-json.py`](csdl-to-json.py) &mdash; is a Python tool that converts Redfish Common Schema Definition Language (CSDL) files to Redfish JSON Schema files.

> **Note:** The CSDL defines an Extensible Markup Language (XML) representation of the entity data model that an OData service exposes.

## Contents

* [Installation](#installation)
* [Usage](#usage)
* [Configuration](#configuration)
* [Processing](#processing)
   * [Assumptions](#assumptions)
   * [Processing details](#processing-details)

## Installation

To install the CSDL-to-JSON converter, see [Installation](README.md#installation "README.md#installation").

## Usage

```bash
% python3 csdl-to-json.py --input INPUT --output OUTPUT --config CONFIG
```

For example:

```bash
% python3 csdl-to-json.py --input ../../Redfish/metadata --output ../../Redfish/json-schema/ --config dmtf-config.json
```

For more information about the configuration file, see [Configuration](#configuration).

The `csdl-to-json.py` arguments are:

```text
usage: csdl-to-json.py [-h] --input INPUT --output OUTPUT [--config CONFIG]
                       [--overwrite OVERWRITE]

A tool used to convert Redfish CSDL files to Redfish JSON Schema files

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT, -I INPUT
                        The folder containing the CSDL files to convert
  --output OUTPUT, -O OUTPUT
                        The folder to write the converted JSON files
  --config CONFIG, -C CONFIG
                        The configuration file containing definitions for
                        various links and user strings
  --overwrite OVERWRITE, -W OVERWRITE
                        Overwrite the versioned files in the output directory
                        if they already exist (default is True)
```

## Configuration

The configuration keys are:

| Key              | Description                                                             | 
| :--------------- | :---------------------------------------------------------------------- |
| `Copyright`      | Copyright string to include in the generated JSON Schema files.         |
| `RedfishSchema`  | Location of Redfish Schema files.                                       |
| `ODataSchema`    | Location of OData Schema files.                                         |
| `Location`       | Output folder for the generated JSON files.                             |
| `ResourceLocation` | Location of Redfish resources.                                        |
| `DoNotWrite`     | Array of one or more output files to exclude from generated JSON files. |

If you omit any keys, the CSDL-to-JSON converter uses the values in the default [`dmtf-config.json`](dmtf-config.json) configuration file.

## Processing

### Assumptions

The CSDL-to-JSON converter makes these assumptions about the format of the Redfish CSDL files:

* Each file that defines a resource follows the Redfish model for inheritance by copy.

    Other than the base `Resource` definition, each resource definition is contained in one file.
* Any referenced external namespaces have proper `Include` statements at the top of each CSDL file.
* All annotations have their expected facets filled.

    For example, the `OData.Description` annotation must use the `String=` facet.
* All namespaces follow the Redfish-defined format where a namespace is either:

    * Unversioned.
    * In the form, `<name>.v<X>_<Y>_<Z>`.
* References to another CSDL file assume that its JSON Schema file is in the same folder.

### Processing details

To process CSDL files, the CSDL-to-JSON converter:

1. Locates the `Resource_v1.xml` schema to cache base definition properties that all resources use.

    If the file is not in the input directory, the tool accesses it in the remote location.
1. Loops on all XML files in the input folder.

    For the following definitions in every versioned and unversioned namespace in each XML file, the CSDL-to-JSON converter generates corresponding JSON Schema file or files, as follows:


    <table width="100%">
      <col width="4%">
      <col width="48%">
      <col width="48%">
      <tbody>
        <tr>
          <th align="left" valign="top" colspan="3"><code>EntityType</code>&nbsp;and&nbsp;<code>ComplexType</code> definitions</th>
        </tr>
        <tr>
          <th rowspan="4"/>
          <th align="left" valign="top">That are in</th>
          <th align="left" valign="top">Tool converts definitions to</th>
        </tr>
        <tr>
          <td align="left" valign="top">Unversioned namespace and marked as abstract</td>
          <td align="left" valign="top">Unversioned JSON Schema file, which uses <code>anyOf</code> statement to point to all versioned definitions</td>
        </tr>
        <tr>
          <td align="left" valign="top">Unversioned&nbsp;namespace&nbsp;and&nbsp;not&nbsp;marked&nbsp;as&nbsp;abstract</td>
          <td align="left" valign="top">Unversioned JSON Schema file</td>
        </tr>
        <tr>
          <td align="left" valign="top">Versioned namespace</td>
          <td align="left" valign="top">That JSON Schema file version and newer JSON Schema file verions</td>
        </tr>
        <tr>
          <th align="left" valign="top" colspan="3"><code>Action</code> definitions</th>
        </tr>
        <tr>
          <th rowspan="3"/>
          <th align="left" valign="top">That are in</th>
          <th align="left" valign="top">Tool converts definitions to</th>
        </tr>
        <tr>
          <td align="left" valign="top">Unversioned namespace</td>
          <td align="left" valign="top">All versioned JSON Schema files</td>
        </tr>
        <tr>
          <td align="left" valign="top">Versioned namespace</td>
          <td align="left" valign="top">That JSON Schema file version and newer JSON Schema file verions</td>
        </tr>
        <tr>
          <th align="left" valign="top" colspan="3"><code>EnumType</code> and <code>TypeDefinition</code> definitions</th>
        </tr>
        <tr>
          <th rowspan="3"/>
          <th align="left" valign="top">That are in</th>
          <th align="left" valign="top">Tool converts definitions to</th>
        </tr>
        <tr>
          <td align="left" valign="top">Unversioned namespace</td>
          <td align="left" valign="top">Unversioned JSON Schema file</td>
        </tr>
        <tr>
          <td align="left" valign="top">Versioned namespace</td>
          <td align="left" valign="top">That JSON Schema file version and newer JSON Schema file verions</td>
        </tr>
      </tbody>
    </table>
