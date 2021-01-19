# JSON Schema-to-OpenAPI converter

Copyright 2018-2021 DMTF. All rights reserved.

## About

The `json-to-yaml.py` tool is a Python tool that processes and converts Redfish JSON Schema files to Redfish OpenAPI files.

## Installation

To install the JSON Schema-to-OpenAPI convertor, see [Installation](Redfish-Tools#installation "Redfish-Tools#installation").

## Usage

Example: `python3 json-to-yaml.py --input <JSON-Dir> --output <YAML-Dir> --config <Config-File> --base <Base-OpenAPI-Doc>`

The tool processes all files in the folder specified by the *input* argument.  It converts the contents of the files to create OpenAPI YAML files and save them to the folder specified by the *output* argument.  It also produces the OpenAPI Service Document to describe the URIs of the Redfish Service.  If the *base* argument is given, the tool starts from the definitions in the specified OpenAPI service document.  [Processing](#processing) describes this process in more detail.

### Options

```
usage: json-to-yaml.py [-h] --input INPUT --output OUTPUT --config CONFIG
                       [--base BASE] [--overwrite OVERWRITE]

A tool used to convert Redfish JSON Schema files to Redfish OpenAPI YAML files
along with the OpenAPI Service Document

required arguments:
  --input INPUT, -I INPUT
                        The folder containing the JSON files to convert
  --output OUTPUT, -O OUTPUT
                        The folder to write the converted YAML files
  --config CONFIG, -C CONFIG
                        The JSON file that describes configuration options for
                        the output

optional arguments:
  -h, --help            show this help message and exit
  --base BASE, -B BASE  The base OpenAPI Service Document if extending an
                        existing one
  --overwrite OVERWRITE, -W OVERWRITE
                        Overwrite the versioned files in the output directory
                        if they already exist (default is True)
```

### Configuration

The configuration file is a JSON file that contains five properties at the root of the object:

* info: The object for the OpenAPI service document
    * This property is required and does not have a default
* OutputFile: The name of the output file for the OpenAPI Service Document
* TaskRef: A pointer to the JSON Schema definition of Task
* MessageRef: A pointer to the JSON Schema definition of Message
* DoNotWrite: A list of the output files to filter out when writing the YAML files
* Extensions: A structure containing additional URIs to apply to a given resource type if provided in the base OpenAPI Service Document

Sample file:

```json
{
   "info": {
      "title": "Redfish",
      "x-copyright": "Copyright 2020-2021 DMTF. For the full DMTF copyright policy, see http://www.dmtf.org/about/policies/copyright",
      "description": "This contains the definition of a Redfish service.",
      "version": "2020.4",
      "contact": {
         "name": "DMTF",
         "url": "https://www.dmtf.org/standards/redfish"
      }
   },
   "OutputFile": "openapi.yaml",
   "TaskRef": "http://redfish.dmtf.org/schemas/v1/Task.v1_5_1.yaml#/components/schemas/Task_v1_5_1_Task",
   "MessageRef": "http://redfish.dmtf.org/schemas/v1/Message.v1_1_2.yaml#/components/schemas/Message_v1_1_2_Message",
   "ODataSchema": "http://redfish.dmtf.org/schemas/v1/odata-v4.yaml",
   "DoNotWrite": ["Volume.",
      "VolumeCollection.",
      "redfish-error.",
      "redfish-payload-annotations.",
      "redfish-schema.",
      "redfish-schema-"
   ]
}
```

## Processing

If provided, the tool loads the referenced base OpenAPI Service Document and caches the provided definitions.  If any URI extensions are provided in the configuration file, it also maps the new URIs as needed.

The tool then interates over all JSON Schema files.  During each iteration, it performs the following steps:

1. Scan the JSON file for the URI and HTTP method information and cache them
1. Scan the JSON file for action definitions and cache them
1. Perform a translation of the JSON data to create the corresponding OpenAPI YAML file.  This is largely a one to one conversion process over all properties and objects found in the JSON Schema file.
    * longDescription becomes x-longDescription
    * enumDescriptions becomes x-enumDescriptions
    * enumLongDescriptions becomes x-enumLongDescriptions
    * enumDeprecated becomes x-enumDeprecated
    * units becomes x-units
    * requiredOnCreate becomes x-requiredOnCreate
    * parameters becomes x-parameters
    * readonly becomes readOnly
    * deprecated becomes x-depcrecated, and also adds "deprecated: true"
    * patternProperties becomes x-patternProperties, and the nested type object is removed
    * "nullable: true" is added to properties that contain an anyOf statement showing null, and the anyOf statement is removed
    * "definitions" becomes "components/schemas"

After each JSON file has been processed and converted to YAML, the OpenAPI service document is then constructed.  This is done by processing the cached URI, HTTP, and action information found in the converted JSON files.  For each URI, it creates the path entry with its HTTP methods, request body, and responses.
