# CSDL-to-JSON converter

Copyright 2017-2021 Distributed Management Task Force, Inc. All rights reserved.

## About

The CSDL-to-JSON converter,`csdl-to-json.py`, is a Python tool that converts Redfish CSDL files to Redfish JSON Schema files.

To install the tool, see [Installation](https://github.com/DMTF/Redfish-Tools#installation "https://github.com/DMTF/Redfish-Tools#installation").

* [Usage](#usage)
* [Configuration](#configuration)
* [Assumptions](#assumptions)
* [Processing](#processing)

## Usage

```bash
$ python3 csdl-to-json.py --input INPUT --output OUTPUT --config CONFIG
```

For example:

```bash
$ python3 csdl-to-json.py --input ../../Redfish/metadata --output ../../Redfish/json-schema/ --config dmtf-config.json
```

where

| Argument           | Description                                                   | 
| :----------------- | :------------------------------------------------------------ |
| `--input INPUT`    | Input folder that contains the CSDL files to convert to JSON files. |
| `--output OUTPUT`  | Output folder for the generated JSON files.                         |
| `--config CONFIG`  | Name of [configuration](#configuration) file, from which the tool reads control parameters. |


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

The default configuration file is `dmtf-config.json`, which contains these statements:

<a id="default-values"></a>
```json
{
  "Copyright": 
     "Copyright 2014-2021 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright",
  "RedfishSchema": "http://redfish.dmtf.org/schemas/v1/redfish-schema-v1.json",
  "ODataSchema": "http://redfish.dmtf.org/schemas/v1/odata-v4.json",
  "Location": "http://redfish.dmtf.org/schemas/v1/",
  "ResourceLocation": "http://redfish.dmtf.org/schemas/v1/",
  "DoNotWrite": ["Volume.", "VolumeCollection.", "RedfishError.", "RedfishExtensions.", "Validation."]
}
```

The parameters are:

| Parameter          | Defines                                                                | 
| :----------------- | :--------------------------------------------------------------------- |
| `Copyright`        | Copyright string to include in the JSON Schema files.                  |
| `RedfishSchema`    | Location of Redfish Schema files.                                      |
| `ODataSchema`      | Location of OData Schema files.                                        |
| `Location`         | Output folder for the generated JSON files.                            |
| `ResourceLocation` | Location of Redfish resources.                                         |
| `DoNotWrite`       | List of one or more output files to exclude from generated JSON files. |

If you omit any parameters, the tool uses the [default values](#default-values) in the `dmtf-config.json` file.

## Assumptions

The CSDL-to-JSON converter makes these assumptions about the format of the Redfish CSDL files:

* Each file that defines a resource follows the Redfish model for inheritance by copy.

    Other than the base *Resource* definition, each resource definition is contained in one file.
* Any referenced external namespaces have proper `Include` statements at the top of each CSDL file.
* All annotations have their expected facets filled.

    For example, the `OData.Description` annotation must use the `String=` facet.
* All namespaces follow the Redfish-defined format, where a namespace is either unversioned or in the form, `<name>.v<X>_<Y>_<Z>`.
* References to another CSDL file assume that its JSON Schema file is in the same folder.

## Processing

To process CSDL files, the CSDL-to-JSON converter:

1. Locates the `Resource_v1.xml` schema to cache base definition properties that all resources use.

    If the file is not in the input directory, the tool accesses it in the remote location.
1. Loops on all XML files in the input folder.

    For the following elements and properties in every versioned and unversioned namespace in each XML file, the tool generates a corresponding JSON file:

    <table>
      <thead>
        <tr>
          <th align="left" valign="top">For&nbsp;every</th>
          <th align="left" valign="top">CSDL&#8209;to&#8209;JSON&nbsp;converter&nbsp;converts&nbsp;XML&nbsp;file&nbsp;to</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td align="left" valign="top"><code>EntityType</code> element in a versioned namespace that is marked abstract</td>
          <td align="left" valign="top">Unversioned JSON file that points to all JSON file versions by using <code>anyOf</code> statement.</td>
        </tr>
        <tr>
          <td align="left" valign="top"><code>EntityType</code> element in an unversioned namespace that is not marked abstract</td>
          <td align="left" valign="top">Unversioned JSON file.</td>
        </tr>
        <tr>
          <td align="left" valign="top"><code>EntityType</code> element in a versioned namespace</td>
          <td align="left" valign="top">That JSON file version and newer JSON file versions.</td>
        </tr>
        <tr>
          <td align="left" valign="top"><code>ComplexType</code> element in a versioned namespace that is marked abstract</td>
          <td align="left" valign="top">Unversioned JSON file that points to all JSON file versions by using <code>anyOf</code> statement.</td>
        </tr>
        <tr>
          <td align="left" valign="top"><code>ComplexType</code> element in an unversioned namespace that is not marked abstract</td>
          <td align="left" valign="top">Unversioned JSON file.</td>
        </tr>
        <tr>
          <td align="left" valign="top"><code>ComplexType</code> element in a versioned namespace</td>
          <td align="left" valign="top">That JSON file version and newer JSON file versions.</td>
        </tr>
        <tr>
          <td align="left" valign="top"><code>Action</code> property in an unversioned namespace</td>
          <td align="left" valign="top">All JSON file versions.</td>
        </tr>
        <tr>
          <td align="left" valign="top"><code>Action</code> property in versioned namespace</td>
          <td align="left" valign="top">That JSON file version and newer JSON file versions.</td>
        </tr>
        <tr>
          <td align="left" valign="top"><code>EnumType</code> element in an unversioned namespace</td>
          <td align="left" valign="top">Unversioned JSON file.</td>
        </tr>
        <tr>
          <td align="left" valign="top"><code>EnumType</code> element in a versioned namespace</td>
          <td align="left" valign="top">That JSON file version and newer JSON file versions.</td>
        </tr>
        <tr>
          <td align="left" valign="top"><code>TypeDefinition</code>&nbsp;element in an unversioned namespace</td>
          <td align="left" valign="top">Unversioned JSON file.</td>
        </tr>
        <tr>
          <td align="left" valign="top"><code>TypeDefinition</code>&nbsp;element in a versioned namespace</td>
          <td align="left" valign="top">That JSON file version and newer JSON file versions.</td>
        </tr>
      </tbody>
    </table>
