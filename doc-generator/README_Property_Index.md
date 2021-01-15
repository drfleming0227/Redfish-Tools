# Redfish docs generator: Property index configuration

Copyright 2018-2021 Distributed Management Task Force, Inc. All rights reserved.

## About

You can use the **Redfish docs generator** &mdash; [`doc_generator.py`](doc_generator.py) &mdash; to produce an index of property names and descriptions.

The output includes property name, type, schemas where found, and descriptions found.

When you run run the docs generator in *property index* mode:

* Only a few of `doc_generator.py` arguments apply.
* The [configuration file](#configuration) takes a different form than the one used for the other output modes.

Arguments:

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

The configuration file for this mode is a JSON document with the following elements:

| Element     | Required | Description                                                    | Reference     | 
| :---------- | :------- | :------------------------------------------------------------- | :------------ |
| `boilerplate_intro` | Optional | Location of a Markdown file that contains content that appears at the beginning of the document before the generated Redfish Schema documentation. If a relative path, should be relative to the location of the configuration file. | |
| `boilerplate_postscript` | Optional | Location of a Markdown file that contains content that appears at the end of the document after the generated Redfish Schema documentation. If a relative path, should be relative to the location of the configuration file. | |
| `description_overrides` | Optional | An object keyed by property name, which can specify descriptions that ooverride those in the source Schemas. | [Description overrides](#description-overrides) |
| `excluded_properties` | Optional | List of property names to exclude from the output. | [Excluded properties](#excluded-properties) |
| `format` | Optional | Output format. Value is `markdown`, `slate`, `html`, or `csv`. | |
| `uri_mapping` | Required | Maps partial URIs without protocol prefix to local directories or files. | [URI mapping](#uri-mapping) |

Other properties may be included for the user's reference, and are ignored by the Documentation Generator.

An example configuration file:

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
```

### Description overrides

You can override descriptions for individual properties. The `description_overrides` object is keyed by property name. Values are lists, which enable you to specify different overrides for the same property in different schemas. Each object in the list can have the following entries:

| Key                   | Value          |
| :-------------------- | :------------- |
| `type`                | Property type. |
| `schemas`             | List of schemas to which this element applies. |
| `overrideDescription` | String that replaces the description in the schema. |
| `globalOverride`      | The `overrideDescription` in this element applies to all instances of the property name that match the `type`. |
| `description`         | Description in the schema. |
| `knownException`      | A variant description is expected. |

The `description` and `knownException` keys are primarily for user reference. When generating configuration output, the Documentation Generator includes the description and set `knownException` to `false`. The user can edit the resulting output to distinguish expected exceptions from those that need attention. Neither field affects the property index document itself.

> **Note:** Although `description_overrides` has a similar function to `property_description_overrides` in other modes, it has a different structure.

Some examples:

```json
"EventType": [{
   "overrideDescription": "This indicates the type of an event recorded in this log.",
   "globalOverride": true,
   "type": "string"
}]
```

The combination of `globalOverride` and `overrideDescription` indicates that all instances of the `EventType` property that have type `string` should have their description replaced with `"This indicates the type of an event recorded in this log."`

```json
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
   "schemas": ["Power/PowerSupplies",
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
```

The first two entries in this `FirmwareVersion` example override the description for `FirmwareVersion` with type `string`, in the listed schemas. The third entry identifies another instance of `FirmwareVersion` with another description, which is expected but should not be overridden.

### Excluded properties

To exclude properties from the output, include them in the `excluded_properties` list. An asterisk (`*`) as the first character in a property acts as a wild card. In the following example, any property name that ends with `"@odata.count"` is omitted:

```json
"excluded_properties": ["description",
   "Id", "@odata.context",
   "@odata.type", "@odata.id",
   "@odata.etag", "*@odata.count"
]
```

### URI mapping

This object maps partial URIs, as found in the schemas, to local directories. The partial URI should include the domain part of the URI but can omit the protocol (http:// or https://).

```json
"uri_mapping": { "redfish.dmtf.org/schemas/v1": "./json-schema" }
```

## Configuration file output

Use the `--property_index_config_out` option to specify an output file for updated configuration information. The Documentation Generator extends the input configuration by adding entries for any properties where the property name appears with more than one type or description.

If you specify `globalOverride` for a property name or property name and type, no data is added for matching instances.

All added entries include `"knownException": false`. In addition, if an entry includes `"knownException": true` in the input configuration but the description no longer matches, `knownException` is set to `false`. 

In the previous example, if `FirmwareVersion` in the `PCIeDevice` schema had a different description than the one listed in the example input, it appears in the output with its new description and `"knownException": false`.
