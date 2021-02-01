[![Build Status](https://travis-ci.com/DMTF/Redfish-Tools.svg?branch=master)](https://travis-ci.com/github/DMTF/Redfish-Tools)
<p align="center">
  <img src="http://redfish.dmtf.org/sites/all/themes/dmtf2015/images/dmtf-redfish-logo.png" alt="DMTF Redfish" width=180>

# Redfish doc generator: Property-index mode

Copyright 2018-2021 Distributed Management Task Force, Inc. All rights reserved.



## Contents

* [Usage](#usage)
* [Configuration](#configuration)
* [Configuration file output](#configuration-file-output)

## Usage

The following command-line options apply in property-index mode:

```text
usage: doc_generator.py [-h]
                        [--config CONFIG_FILE]
                        [-n]
                        [--format {markdown,html,csv}]
                        [--out OUTFILE]
                        [--profile PROFILE_DOC]
                        [--property_index_config_out CONFIG_FILE_OUT]
                        [import_from ...]

positional arguments:
  import_from           Name of a file or directory to process (wild cards are
                        acceptable). Default: json-schema

optional arguments:
  -h, --help            show this help message and exit
  -n, --normative       Produce normative (developer-focused) output
  --format {markdown,html,csv}
                        Output format
  --out OUTFILE         Output file (default depends on output format:
                        output.md for Markdown, index.html for HTML,
                        output.csv for CSV
  --property_index      Produce Property Index output.
  --property_index_config_out CONFIG_FILE_OUT
                        Generate updated config file, with specified filename
                        (property_index mode only).
  --config CONFIG_FILE  Path to a config file, containing configuration in
                        JSON format.

Example:
   doc_generator.py --property_index --format=html --config=pi_config.json
```

## Configuration

The configuration file for property-index mode contains these keys:

| Key         | Required | Description                                                    | Reference     | 
| :---------- | :------- | :------------------------------------------------------------- | :------------ |
| `boilerplate_intro` | Optional | Location of a Markdown file that contains content that appears at the beginning of the document before the generated Redfish Schema documentation. If a relative path, should be relative to the location of the configuration file. | |
| `boilerplate_postscript` | Optional | Location of a Markdown file that contains content that appears at the end of the document after the generated Redfish Schema documentation. If a relative path, should be relative to the location of the configuration file. | |
| `description_overrides` | Optional | An object keyed by property name, which can specify descriptions that ooverride those in the source Schemas. | [Description overrides](#description-overrides) |
| `excluded_properties` | Optional | List of property names to exclude from the output. | [Excluded properties](#excluded-properties) |
| `format` | Optional | Output format. Value is `markdown`, `slate`, `html`, or `csv`. | |
| `uri_mapping` | Required | Maps partial URIs without protocol prefix to local directories or files. | [URI mapping](#uri-mapping) |

Other properties may be included for the user's reference, and are ignored by the doc generator.

**Base configuration file:** <a href="sample_inputs/property_index/config.json"><code>sample_inputs/property_index/config.json</code></a>

<!-- An example configuration file:

```json
{
   "description": "Redfish Property Index generation file",
   "version": "2018.2",
   "uri_mapping": {
      "redfish.dmtf.org/schemas/v1": "./json-schema"
   },
   "excluded_properties": [
      "description", "Id",
      "@odata.context",
      "@odata.type", "@odata.id",
      "@odata.etag", "*@odata.count"
   ],
   "description_overrides": {
      "EventType": [{
         "overrideDescription": "This indicates the type of an event recorded in this log.",
         "globalOverride": true,
         "type": "string"
      }],
      "FirmwareVersion": [{
         "description": "Firmware version.",
         "type": "string",
         "knownException": true,
         "overrideDescription": "Override text for FirmwareVersion",
         "schemas": [
            "AttributeRegistry/SupportedSystems"
         ]
      }, {
         "overrideDescription": "The firmware version of this thingamajig.",
         "type": "string",
         "knownException": true,
         "schemas": [
            "Power/PowerSupplies",
            "Manager",
            "ComputerSystem/TrustedModules",
            "Storage/StorageControllers"
         ]
      }, {
         "description": "The version of firmware for this PCIe device.",
         "type": "string",
         "knownException": true,
         "schemas": ["PCIeDevice"]
      }]
   }
}
``` -->

* [Description overrides](#description-overrides)
* [Excluded properties](#excluded-properties)
* [URI mapping](#uri-mapping)

### Description overrides



### Excluded properties



### URI mapping



## Configuration file output


