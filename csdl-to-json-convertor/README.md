# CSDL-to-JSON converter

Copyright 2017-2021 Distributed Management Task Force, Inc. All rights reserved.

The **CSDL-to-JSON converter** &mdash; [`csdl-to-json.py`](csdl-to-json.py) &mdash; is a Python tool that converts Redfish CSDL files to Redfish JSON Schema files.

> **Note:** The Common Schema Definition Language (CSDL) defines an Extensible Markup Language (XML) representation of the entity data model that an OData service exposes.

## Contents

* [Installation](#installation)
* [Usage](#usage)
* [Configuration](#configuration)
* [Assumptions](#assumptions)
* [Processing](#processing)

## Installation

To install the CSDL-to-JSON converter, see [Installation](https://github.com/DMTF/Redfish-Tools#installation "https://github.com/DMTF/Redfish-Tools#installation").

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

The default configuration file is `dmtf-config.json`, which contains these configuration keys and values:

<a id="default-values"></a>
```json
{
   "Copyright":
      "Copyright 2014-2021 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright",
   "RedfishSchema": "http://redfish.dmtf.org/schemas/v1/redfish-schema-v1.json",
   "ODataSchema": "http://redfish.dmtf.org/schemas/v1/odata-v4.json",
   "Location": "http://redfish.dmtf.org/schemas/v1/",
   "ResourceLocation": "http://redfish.dmtf.org/schemas/v1/",
   "DoNotWrite": ["Volume.",
      "VolumeCollection.",
      "RedfishError.",
      "RedfishExtensions.",
      "Validation."
   ]
}
```

The configuration keys are:

| Key              | Description                                                             | 
| :--------------- | :---------------------------------------------------------------------- |
| `Copyright`      | Copyright string to include in the generated JSON Schema files.         |
| `RedfishSchema`  | Location of Redfish Schema files.                                       |
| `ODataSchema`    | Location of OData Schema files.                                         |
| `Location`       | Output folder for the generated JSON files.                             |
| `ResourceLocation` | Location of Redfish resources.                                        |
| `DoNotWrite`     | Array of one or more output files to exclude from generated JSON files. |

If you omit any keys, the CSDL-to-JSON converter uses the [default values](#default-values) in the `dmtf-config.json` file.

## Assumptions

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

## Processing

To process CSDL files, the CSDL-to-JSON converter:

1. Locates the `Resource_v1.xml` schema to cache base definition properties that all resources use.

    If the file is not in the input directory, the tool accesses it in the remote location.
1. Loops on all XML files in the input folder.

    For the following elements and properties in every versioned and unversioned namespace in each XML file, the CSDL-to-JSON converter generates corresponding JSON file or files, as follows:

    <table>
      <col width="40%">
      <col width="20%">
      <col width="40%">
      <thead>
        <tr>
          <th align="left" valign="top"> For&nbsp;every</th>
          <th align="left" valign="top"> In namespace of type</th>
          <th align="left" valign="top"> Marked abstract</th>
          <th align="left" valign="top"> Tool&nbsp;generates JSON file of type</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td align="left" valign="top">
            <code>EntityType</code> and <code>ComplexType</code> element
          </td>
          <td align="left" valign="top"> Versioned </td>
          <td align="left" valign="top"> Yes </td>
          <td align="left" valign="top"> Unversioned that uses <code>anyOf</code> statement to point to all JSON file versions </td>
        </tr>
        <tr>
          <td align="left" valign="top">
            <code>EntityType</code> and <code>ComplexType</code> element
          </td>
          <td align="left" valign="top"> Unversioned </td>
          <td align="left" valign="top"> No </td>
          <td align="left" valign="top"> Unversioned </td>
        </tr>
        <tr>
          <td align="left" valign="top">
            <code>EntityType</code> and <code>ComplexType</code> element
          </td>
          <td align="left" valign="top" colspan="2">Versioned </td>
          <td align="left" valign="top"> Current and newer versions </td>
        </tr>
        <tr>
          <td align="left" valign="top">
            <code>Action</code> property
          </td>
          <td align="left" valign="top" colspan="2">Unversioned </td>
          <td align="left" valign="top"> All versions</td>
        </tr>
        <tr>
          <td align="left" valign="top">
            <code>Action</code> property
          </td>
          <td align="left" valign="top" colspan="2">Versioned </td>
          <td align="left" valign="top"> Current and newer versions </td>
        </tr>
        <tr>
          <td align="left" valign="top">
            <code>EnumType</code> and <code>TypeDefinition</code>&nbsp;element
          </td>
          <td align="left" valign="top" colspan="2">Unversioned </td>
          <td align="left" valign="top"> Unversioned </td>
        </tr>
        <tr>
          <td align="left" valign="top">
            <code>EnumType</code> and <code>TypeDefinition</code>&nbsp;element
          </td>
          <td align="left" valign="top" colspan="2">Versioned </td>
          <td align="left" valign="top"> Current and newer versions </td>
        </tr>
      </tbody>
    </table>
