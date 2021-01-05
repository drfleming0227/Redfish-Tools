# CSDL-to-JSON converter

Copyright 2017-2021 Distributed Management Task Force, Inc. All rights reserved.

## About

The `csdl-to-json.py` tool is a Python tool that processes and converts Redfish CSDL files to Redfish JSON Schema files.

## Installation



## Usage

Example: 

```
$ python3 csdl-to-json.py --input <csdl-dir> --output <json-dir> --config <config-file>
```

where

* `--input <csdl-dir>` is the path to the CSDL files from which you want to generate JSON files.

    The tool processes all files in this folder. 
* `--output <json-dir>` is the location for the generated JSON files.

    The tool creates and saves JSON Schema files to this folder.
* `--config <config-file>` is the location of the `dmtf-config.json` file.

    The tool reads some control parameters from this JSON file. For more information, see [dmtf-config.json file](#dmtf-configjson-file).

For more information, see [Assumptions](#assumptions) and [Processing](#processing).

### Options

```
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

### dmtf-config.json file

The `dmtf-config.json` file contains the following parameters.

| Parameter | Description | 
| :-------- | :---------- |
| `Copyright` | Copyright string to include in the JSON Schema files. |
| `RedfishSchema` | Redfish Schema files. |
| `ODataSchema`  | OData Schema files. |
| `Location` | Web folder in which to publish the generated JSON Schema files. |
| `ResourceLocation` | Location of Redfish resources. |
| `DoNotWrite` | Output files to exclude from generated JSON files. |

If you omit any parameters, the tool uses the [default values](#default-values), which [Sample config file and default values](#default-values) shows.

**Sample config file and default values:**<a id="default-values"></a>

```
{
    "Copyright": "Copyright 2014-2021 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright",
    "RedfishSchema": "http://redfish.dmtf.org/schemas/v1/redfish-schema-v1.json",
    "ODataSchema": "http://redfish.dmtf.org/schemas/v1/odata-v4.json",
    "Location": "http://redfish.dmtf.org/schemas/v1/",
    "ResourceLocation": "http://redfish.dmtf.org/schemas/v1/",
    "DoNotWrite": [ "Volume.", "VolumeCollection.", "RedfishError.", "RedfishExtensions.", "Validation." ]
}
```

## Assumptions

The `csdl-to-json.py` tool makes the following assumptions about the format of the Redfish CSDL files:

* Each file that defines a resource follows the Redfish model for inheritance by copy. Other than the base *Resource* definition, each resource definition is contained in one file.
* Any referenced external namespaces have proper *Include* statements at the top of each CSL file.
* All annotations have their expected facets filled. For example, the `OData.Description` annotation must use the *String=* facet.
* All namespaces follow the Redfish-defined format, where a namespace is either unversioned or is in the form *name.vX_Y_Z*.
* If a reference is made to another CSDL file, its JSON Schema file is in the same folder.

## Processing

Before any translation occurs, the tool tries to locate the `Resource_v1.xml` schema to cache properties for base definitions that all resources use. The tool checks whether the file is in the input directory. If it is not there, the tool accesses the file in the remote location.

After the tool caches the `Resource_v1.xml` definitions, it loops on all `.xml` files in the input directory.

For every namespace defined in the file, the tool generates a corresponding `.json` file, as follows:

| Namespace definitions       | Tool generates JSON file for XML file that is in an...                             |
| :-------------------------- | :--------------------------------------------------------------------------------- |
| `EntityType`<br/>`ComplexType` | <ul><li>Unversioned namespace and are marked as abstract and have a definition that contains an `anyOf` statement in the unversioned JSON Schema that points to all versioned definitions.</li><li>Unversioned namespace and are not marked as abstract and have their definition translated only to the unversioned JSON Schema file.</li><li>Versioned namespace have their definitions translated to that and newer versions of the JSON Schema file.</li></ul> |
| `Action` |<ul><li>Unversioned namespace are translated to all versioned JSON Schema files</li><li>... that are Versioned namespace and have their definitions translated to that and newer versions of the JSON Schema file.</li></ul> |
| `EnumType`<br/> `TypeDefinition` | <ul><li>Unversioned namespace and are translated to the unversioned JSON Schema file.</li><li>Versioned namespace and have their definitions translated to that and newer versions of the JSON Schema file.</li></ul> |
