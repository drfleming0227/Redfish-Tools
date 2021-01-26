[![Build Status](https://travis-ci.com/DMTF/Redfish-Tools.svg?branch=master)](https://travis-ci.com/github/DMTF/Redfish-Tools)
<p align="center">
  <img src="http://redfish.dmtf.org/sites/all/themes/dmtf2015/images/dmtf-redfish-logo.png" alt="DMTF Redfish" width=180>

# JSON Schema-to-OpenAPI converter

Copyright 2018-2021 DMTF. All rights reserved.

## Contents

* [About](#about)
* [Installation](#installation)
* [Usage](#usage)
* [Example](#example)
* [Configuration](#configuration)
* [Processing](#processing)

## About

The **JSON Schema-to-OpenAPI converter** &mdash; [`json-to-yaml.py`](json-to-yaml.py) &mdash; is a Python tool that converts specified Redfish JSON Schema files to Redfish OpenAPI files.

For information about OpenAPI, see the *OpenAPI Specification* at [https://swagger.io/specification/](https://swagger.io/specification/ "https://swagger.io/specification/").

## Installation

1. Clone the `Redfish-Tools` repository:

   ```bash
   % git clone git@github.com:DMTF/Redfish-Tools.git
   % git remote add upstream git@github.com:DMTF/Redfish-Tools.git
   ```
1. [Download and install Python](https://www.python.org/downloads/ "https://www.python.org/downloads/") on the machine from which you will run this tool.
1. Install YAML for Python:

    ```bash
    % pip install pyyaml
    ```

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
% cd Redfish-Tools/json-to-openapi-converter
% python3 json-to-yaml.py --input ../../Redfish/json-schema --output ../../Redfish/openapi --config dmtf-config.json
```

In this example, the **JSON Schema-to-OpenAPI converter** converts the JSON Schema files in the `Redfish/json-schema` input directory to YAML files in the `/Redfish/openapi` output directory. The converter reads the configuration keys from the `dmtf-config.json` configuration file to configure the output, including the OpenAPI service document that it generates.

## Configuration

Sample configuration file: [`dmtf-config.json`](dmtf-config.json)

The configuration file is a JSON file that contains the following keys at the root of the object:

| Key          | Required | Description                        | Default value |
| :----------- | :------- | :--------------------------------- | :------------ |
| `info`       | Required | Object for the OpenAPI service document. | None |
| `OutputFile` | Optional | Output file for the constructed OpenAPI service document. | `openapi.yaml` in the directory from where you run the tool |
| `TaskRef`    | Optional | Pointer to the JSON Schema definition of `Task`. | |
| `MessageRef` | Optional | Pointer to the JSON Schema definition of `Message`. | |
| `DoNotWrite` | Optional | List of the output files to exclude when writing the YAML files. | None |
| `Extensions` | Optional | Structure of additional URIs to apply to a resource type if provided in the base OpenAPI service document. | |

## Processing

* [Summary](#summary)
* [Details](#details)

### Summary

The JSON Schema-to-OpenAPI converter processes and converts all JSON Schema files in the input folder to OpenAPI YAML files in the output folder. It also produces the OpenAPI service document to describe the URIs of the Redfish service.

(Optional) The JSON Schema-to-OpenAPI converter begins with the definitions in the OpenAPI service document that you specify in the optional `--base` argument. The JSON Schema-to-OpenAPI converter loads and caches the base OpenAPI service document definitions. If the configuration file contains any URI extensions, the JSON Schema-to-OpenAPI converter maps the new URIs, as needed.

### Details

The tool iterates over the JSON Schema files. During each iteration, it completes these steps:

1. Scans the JSON file for and caches the URI and HTTP method information.
1. Scans the JSON file for and caches action definitions.
1. Completes a one-to-one conversion of all properties and objects found in the JSON Schema file to create OpenAPI YAML files, as follows:
    
    | JSON data               | OpenAPI YAML data                         |
    | :---------------------- | :---------------------------------------- |
    | `longDescription`       | `x-longDescription` |
    | `enumDescriptions`      | `x-enumLongDescriptions` |
    | `enumDeprecated`        | `x-enumDeprecated` |
    | `enumVersionDeprecated` | `x-enumVersionDeprecated` |
    | `enumVersionAdded`      | `x-enumVersionAdded` |
    | `units`                 | `x-units` |
    | `requiredOnCreate`      | `x-requiredOnCreate` |
    | `owningEntity`          | `x-owningEntity` |
    | `autoExpand`            | `x-autoExpand` |
    | `release`               | `x-release` |
    | `versionDeprecated`     | `x-versionDeprecated` |
    | `versionAdded`          | `x-versionAdded` |
    | `filter`                | `x-filter` |            
    | `excerpt`               | `x-excerpt` |
    | `excerptCopy`           | `x-excerptCopy` |
    | `excerptCopyOnly`       | `x-excerptCopyOnly` |
    | `translation`           | `x-translation` |
    | `enumTranslations`      | `x-enumTranslations` |
    | `language`              | `x-language` |
    | `insertable`<br/>`updatable`<br/>`deletable`<br/>`uris`<br/>`parameters`<br/>`requiredParameter`<br/>`actionResponse` | Removes these terms from the file. |
    | `readonly`              | `readOnly`                                |
    | `deprecated`            | `x-deprecated`, and also adds `deprecated: true` |
    | `patternProperties`     | `x-patternProperties`, and removes the nested type object. |
    | Properties with an `anyOf` statement of `null` | Adds `nullable: true` to those properties and removes the `anyOf` statement. |
    | `definitions`         | `components/schemas` |

1. Processes the cached URI, HTTP, and action information in the converted JSON Schema files to construct the OpenAPI service document. For each URI, the tool creates the path entry with its HTTP methods, request body, and responses.
