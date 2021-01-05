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

1. Before any conversion occurs, the tool tries to locate the `Resource_v1.xml` schema to cache properties for base definitions that all resources use.
1. The tool checks whether the file is in the input directory. If it is not there, the tool accesses the file in the remote location.
1. After the tool caches the `Resource_v1.xml` definitions, it loops on all XML files in the input folder.

    For every namespace that the tool finds in the file, the tool generates a corresponding JSON file, as follows:

    | Definition                  | Tool generates JSON file for XML file that is in an...    |
    | :-------------------------- | :-------------------------------------------------------- |
    | `EntityType` element<br/>`ComplexType` element | <ul><li>Unversioned namespace and are marked as abstract and have a definition that contains an `anyOf` statement in the unversioned JSON Schema that points to all versioned definitions.</li><li>Unversioned namespace and are not marked as abstract and have their definition converted only to the unversioned JSON Schema file.</li><li>Versioned namespace have their definitions converted to that and newer versions of the JSON Schema file.</li></ul> |
    | `Action` property |<ul><li>Unversioned namespace are converted to all versioned JSON Schema files</li><li>... that are Versioned namespace and have their definitions converted to that and newer versions of the JSON Schema file.</li></ul> |
    | `EnumType` element<br/> `TypeDefinition` element | <ul><li>Unversioned namespace and are converted to the unversioned JSON Schema file.</li><li>Versioned namespace and have their definitions converted to that and newer versions of the JSON Schema file.</li></ul> |
