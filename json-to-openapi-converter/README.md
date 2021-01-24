[![Build Status](https://travis-ci.com/DMTF/Redfish-Tools.svg?branch=master)](https://travis-ci.com/github/DMTF/Redfish-Tools)
<p align="center">
  <img src="http://redfish.dmtf.org/sites/all/themes/dmtf2015/images/dmtf-redfish-logo.png" alt="DMTF Redfish" width=180>

# JSON Schema-to-OpenAPI converter

Copyright 2018-2021 DMTF. All rights reserved.

The **JSON Schema-to-OpenAPI converter** &mdash; [`json-to-yaml.py`](json-to-yaml.py) &mdash; is a Python tool that converts specified Redfish JSON Schema files to Redfish OpenAPI files.

For information about OpenAPI, see [https://swagger.io/specification/](https://swagger.io/specification/ "https://swagger.io/specification/").

## Contents

* [Installation](#installation)
* [Usage](#usage)
* [Example](#example)
* [Configuration](#configuration)
* [Processing](#processing)

## Installation

To install the JSON Schema-to-OpenAPI convertor, see [Installation](../README.md#installation "../README.md#installation").

## Usage

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

## Example

```bash
% python3 json-to-yaml.py --input INPUT --output OUTPUT --config CONFIG --base BASE
```

where

* `--input INPUT`. Required. The folder that contains the JSON files to convert.
* `--output OUTPUT`. Required. The folder in which to write the converted YAML files.
* `--config CONFIG`. Required. The JSON file that configures the output. See [Configuration](#configuration).
* `--base BASE`. Optional. The base OpenAPI service document that you want to extend.

```bash
% python3 json-to-yaml.py --input ../../Redfish/json-schema --output ../../Redfish/yaml --config dmtf-config.json
```

## Configuration

Sample configuration file: [`dmtf-config.json`](dmtf-config.json)

The configuration file is a JSON file that contains the following keys at the root of the object:

| Key          | Required | Default | Description                                |
| :----------- | :------- | :------ | :----------------------------------------- |
| `info`       | Required | None.   | Object for the OpenAPI service document. |
| `OutputFile` | Required | None.   | Name of the output file for the OpenAPI service document. |
| `TaskRef`    | Required | None.   | Pointer to the JSON Schema definition of `Task`. |
| `MessageRef` | Required | None.   | Pointer to the JSON Schema definition of `Message`. |
| `DoNotWrite` | Required | None.   | List of the output files to exclude when writing the YAML files. |
| `Extensions` | Required | None.   | Structure containing additional URIs to apply to a resource type if provided in the base OpenAPI service document. |

## Processing

The JSON Schema-to-OpenAPI converter processes and converts all JSON Schema files in the `--input` folder to OpenAPI YAML files, which it saves to the `--output` folder.  It also produces the OpenAPI service document to describe the URIs of the Redfish Service.

If you include the `--base` argument, the tool begins with the definitions in the specified OpenAPI service document. The tool loads the base OpenAPI service document and caches the provided definitions.  If the configuration file contains any URI extensions, the tool maps the new URIs as needed.

The tool iterates over the JSON Schema files. During each iteration, it completes these steps:

1. Scans the JSON file for and caches the URI and HTTP method information.
1. Scans the JSON file for and caches action definitions.
1. Translates JSON data to create the corresponding OpenAPI YAML file. This is largely a one-to-one conversion process over all properties and objects found in the JSON Schema file.
    
    | JSON data              | OpenAPI YAML data                         |
    | :--------------------- | :---------------------------------------- |
    | `longDescription`      | `x-longDescription`                       |
    | `enumDescriptions`     | `x-enumDescriptions`                      |
    | `enumLongDescriptions` | `x-enumLongDescriptions`                  |
    | `enumDeprecated`       | `x-enumDeprecated`                        |
    | `units`                | `x-units`                                 |
    | `requiredOnCreate`     | `x-requiredOnCreate`                      |
    | `parameters`           | `x-parameters`                            |
    | `readonly`             | `readOnly`                                |
    | `deprecated`           | `x-deprecated`, and also adds `"deprecated: true"` |
    | `patternProperties`    | `x-patternProperties`, and removes the nested type object. |
    | Properties that contain an `anyOf` statement showing `null` | Adds `"nullable: true"` to those properties and removes the `anyOf` statement. |
    | `"definitions"`        | `"components/schemas"`                    |

1. After the tool converts the JSON Schema files to YAML files, it constructs the OpenAPI service document.  To accomplish this, the tool processes the cached URI, HTTP, and action information in the converted JSON Schema files. For each URI, the tool creates the path entry with its HTTP methods, request body, and responses.
