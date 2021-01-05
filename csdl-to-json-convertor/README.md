# CSDL-to-JSON converter

Copyright 2017-2021 Distributed Management Task Force, Inc. All rights reserved.

## About

The `csdl-to-json.py` tool is a Python tool that converts Redfish CSDL files to Redfish JSON Schema files.

To install the tool, see [Installation](https://github.com/DMTF/Redfish-Tools#installation "https://github.com/DMTF/Redfish-Tools#installation").

* [Usage](#usage)
* [Options](#options)
* [dmtf-config.json file](#dmtf-configjson-file)
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

| Option             | Description                                                   | 
| :----------------- | :------------------------------------------------------------ |
| `--input INPUT`    | Input folder that contains the CSDL files to convert to JSON files. |
| `--output OUTPUT`  | Output folder to which to write the generated JSON files.            |
| `--config CONFIG`  | Configuration file name. The tool reads control parameters from this file.<br/><br/>See [dmtf-config.json file](#dmtf-configjson-file). |

## Options

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

## dmtf-config.json file

<a id="default-values"></a>
```json
{
  "Copyright": "Copyright 2014-2021 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright",
  "RedfishSchema": "http://redfish.dmtf.org/schemas/v1/redfish-schema-v1.json",
  "ODataSchema": "http://redfish.dmtf.org/schemas/v1/odata-v4.json",
  "Location": "http://redfish.dmtf.org/schemas/v1/",
  "ResourceLocation": "http://redfish.dmtf.org/schemas/v1/",
  "DoNotWrite": ["Volume.", "VolumeCollection.", "RedfishError.", "RedfishExtensions.", "Validation."]
}
```

The `dmtf-config.json` file contains the following parameters.

| Parameter          | Description                                               | 
| :----------------- | :-------------------------------------------------------- |
| `Copyright`        | Copyright string to include in the JSON Schema files.     |
| `RedfishSchema`    | Redfish Schema files.                                     |
| `ODataSchema`      | OData Schema files.                                       |
| `Location`         | Output folder to which to write the generated JSON files. |
| `ResourceLocation` | Location of Redfish resources.                            |
| `DoNotWrite`       | Output files to exclude from generated JSON files.        |

If you omit any parameters, the tool uses the [default values](#default-values).

## Assumptions

The `csdl-to-json.py` tool makes these assumptions about the format of the Redfish CSDL files:

* Each file that defines a resource follows the Redfish model for inheritance by copy. Other than the base *Resource* definition, each resource definition is contained in one file.
* Any referenced external namespaces have proper `Include` statements at the top of each CSDL file.
* All annotations have their expected facets filled. For example, the `OData.Description` annotation must use the `String=` facet.
* All namespaces follow the Redfish-defined format, where a namespace is either:

    * Unversioned.
    * In the form, `<name>.v<X>_<Y>_<Z>`.
* If a reference is made to another CSDL file, its JSON Schema file is in the same folder.

## Processing

The `csdl-to-json.py` tool completes this processing:

1. Locates the `Resource_v1.xml` schema to cache base definition properties that all resources use.

    If the file is not in the input directory, the tool accesses it in the remote location.
1. Loops on all XML files in the input folder.

    For every namespace in each XML file, generates a corresponding JSON file for the following elements and properties:

    <table>
      <col width="30%">
      <col width="30%">
      <col width="40%">
      <thead>
        <tr>
          <th align="left" valign="top">For every</th>
          <th align="left" valign="top">In namespace</th>
          <th align="left" valign="top">Converts XML to</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td align="left" valign="top" rowspan="3"><code>EntityType</code> element</td>
          <td align="left" valign="top">Versioned and marked as abstract</td>
          <td align="left" valign="top">Unversioned JSON file that points to all versioned definitions with definition that contains an <code>anyOf</code> statement.</td>
        </tr>
        <tr>
          <td align="left" valign="top">Unversioned and not marked as abstract</td>
          <td align="left" valign="top">Unversioned JSON file.</td>
        </tr>
        <tr>
          <td align="left" valign="top">Versioned</td>
          <td align="left" valign="top">That version and newer versions of the JSON file.</td>
        </tr>
        <tr>
          <td align="left" valign="top" rowspan="3"><code>ComplexType</code> element</td>
          <td align="left" valign="top">Versioned and marked as abstract</td>
          <td align="left" valign="top">Unversioned JSON file that points to all versioned definitions with definition that contains an <code>anyOf</code> statement.</td>
        </tr>
        <tr>
          <td align="left" valign="top">Unversioned and not marked as abstract</td>
          <td align="left" valign="top">Unversioned JSON file.</td>
        </tr>
        <tr>
          <td align="left" valign="top">Versioned</td>
          <td align="left" valign="top">That version and newer versions of the JSON file.</td>
        </tr>
        <tr>
          <td align="left" valign="top" rowspan="2"><code>Action</code> property</td>
          <td align="left" valign="top">Unversioned</td>
          <td align="left" valign="top">All versioned JSON files.</td>
        </tr>
        <tr>
          <td align="left" valign="top">Versioned</td>
          <td align="left" valign="top">That version and newer versions of the JSON file.</td>
        </tr>
        <tr>
          <td align="left" valign="top" rowspan="2"><code>EnumType</code> element</td>
          <td align="left" valign="top">Unversioned</td>
          <td align="left" valign="top">Unversioned JSON file.</td>
        </tr>
        <tr>
          <td align="left" valign="top">Versioned</td>
          <td align="left" valign="top">That version and newer versions of the JSON file.</td>
        </tr>
        <tr>
          <td align="left" valign="top" rowspan="2"><code>TypeDefinition</code> element</td>
          <td align="left" valign="top">Unversioned</td>
          <td align="left" valign="top">Unversioned JSON file.</td>
        </tr>
        <tr>
          <td align="left" valign="top">Versioned</td>
          <td align="left" valign="top">That version and newer versions of the JSON file.</td>
        </tr>
      </tbody>
    </table>
