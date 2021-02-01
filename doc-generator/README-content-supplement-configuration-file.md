[![Build Status](https://travis-ci.com/DMTF/Redfish-Tools.svg?branch=master)](https://travis-ci.com/github/DMTF/Redfish-Tools)
<p align="center">
  <img src="http://redfish.dmtf.org/sites/all/themes/dmtf2015/images/dmtf-redfish-logo.png" alt="DMTF Redfish" width=180>

# Redfish doc generator: Content supplement configuration file

Copyright 2016-2021 Distributed Management Task Force, Inc. All rights reserved.

The content supplement configuration file is a JSON file that defines text overrides for property descriptions, replacements for unit abbreviations, and schema-specific content to apply to the generated schema documentation.

These output modes support the content supplement configuration file:

| Output mode | Sample content supplement configuration file |
| :---------- | :------------------------------------------- |
| [Profile mode](README.md#profile-mode "README.md#profile-mode") | [`sample_inputs/profile_mode/content_supplement.json`](sample_inputs/profile_mode/content_supplement.json "sample_inputs/profile_mode/content_supplement.json") |
| [Standard mode](README.md#standard-mode "README.md#standard-mode") | [`sample_inputs/standard_html/content_supplement.json`](sample_inputs/standard_html/content_supplement.json "sample_inputs/standard_html/content_supplement.json") |
| [Standard normative mode](README.md#standard-normative-mode "README.md#standard-normative-mode") | [`sample_inputs/standard_html/content_supplement.json`](sample_inputs/standard_html/content_supplement.json "sample_inputs/standard_html/content_supplement.json") |
| [Subset mode](README.md#subset-mode "README.md#subset-mode") | [`sample_inputs/subset/content_supplement.json`](sample_inputs/subset/content_supplement.json "sample_inputs/subset/content_supplement.json") |

## Configuration keys

* [property_description_overrides](#property_description_overrides)
* [property_fulldescription_overrides](#property_fulldescription_overrides)
* [schema_link_replacements](#schema_link_replacements)
* [schema_supplement](#schema_supplement)
* [units_translation](#units_translation)

| Key | Type | Description |
| :-- | :--- | :---------- |
| `property_description_overrides` | Dictionary | Maps property names to strings that replace the descriptions of the named properties. |
| `property_fulldescription_overrides` | Dictionary | Maps property names to strings that replace the descriptions of the named properties. These replacements are <i>full</i> in that the doc generator omits any additional information that it normally appends, like a reference to the definition of the property in another schema. |
| `schema_link_replacements` | Dictionary | Maps reference URIs to replacement URIs. The match type is full or partial. Replaces one link with another link. The dictionary structure is:<pre lang="json">schema_link_replacements": {
   "https://somewhere.example.com/some/path/to/a/some_schema.json": {
      "full_match": true,
      "replace_with": "https://docserver.example.org/some_schema_doc.html"
   },
   "fancy": {
      "full_match": false,
      "replace_with": "https://docserver.example.org/fancy_schemas.html"
   }
}</pre> |
| `schema_supplement` | Dictionary | Maps schema names to a dictionary of structured content, including text overrides for property descriptions, replacements for unit abbreviations, schema-specific introductions, property description substitutions, and other supplementary data. All elements in this structure are optional.<br/><br/>The structure of this object is:<pre lang="json">schema_supplement": {
   "SchemaName": {
      "description": "A string to replace the schema description. Plain text or markdown.",
      "mockup": "A path or URI to a mockup file.",
      "jsonpayload": "A chunk of JSON.",
      "intro": "",
      "property_description_overrides": {
         "PropertyName": "a string, plain text or markdown.",
         "AnotherPropertyName": "a string, plain text or markdown."
      },
      "property_fulldescription_overrides": {
         "YetAnotherPropertyName": "a string, plain text or markdown. This string will also eliminate any additional data the doc generator would normally append to the description."
      },
      "property_details": {
         "EnumPropertyName": "A string, plain text or markdown. This will be inserted after the property description and prior to the table of enum details in the property information under Property Details.",
         "property_details": {
            "UUID": "\nThe UUID property contains a value that represents the universal unique identifier number (UUID) of a system.\n\nThe UUID property is a string data type. The format of the string is the 35-character string format specified in RFC4122: \"xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx\". Each x represents a hexadecimal digit (0-f).\n\nRegarding the case of the hex values, RFC4122 specifies that the hex values should be lowercase characters. Most modern scripting languages typically also represent hex values in lowercase characters following the RFC. However, dmidecode, WMI and some Redfish implementations currently use uppercase characters for UUID on output."
         }
      }
   }
}</pre><br/><br/>In this structure:<br/><br/>
| Attribute    | Description                                                   |
| :----------- | :------------------------------------------------------------ |
| `SchemaName` | Defines the schema name as either a bare schema name or a schema name with an underscore and an appended major version.<br/><br/>For example, `"ComputerSystem"` or `"ComputerSystem_2"`. |
| `description` | Replaces the description of the schema. |
| `intro`  | Defines a string to replace the description or append to the `description` string, if provided. |
| `mockup` | Mutually exclusive with `jsonpayload`. If you specify both attributes, `mockup` takes precedence.<blockquote><b>Note:</b> If you specify a <code>payload_dir</code> key in the <a href="README-base-configuration-file.md" title="README-base-configuration-file">base configuration file</a>, the payload directory takes precedence over <code>mockup</code>.</blockquote> |
| `jsonpayload` | Mutually exclusive with `mockup`. If you specify both attributes, `mockup` takes precedence.<blockquote><b>Note:</b> If you specify a <code>payload_dir</code> key in the <a href="README-base-configuration-file.md" title="README-base-configuration-file">base configuration file</a>, the payload directory takes precedence over <code>jsonpayload</code>.</blockquote> | |
| `units_translation` | Dictionary | Maps Redfish schema units to units as you want them to appear in the documentation. |
<!-- ### property_description_overrides

**Data type:** Dictionary

Maps property names to strings that replace the descriptions of the named properties.

### property_fulldescription_overrides

**Data type:** Dictionary

Maps property names to strings that replace the descriptions of the named properties. These replacements are <i>full</i> in that the doc generator omits any additional information that it normally appends, like a reference to the definition of the property in another schema.

### schema_link_replacements

**Data type:** Dictionary

Maps reference URIs to replacement URIs. The match type is full or partial. Replaces one link with another link. The dictionary structure is:

```json
"schema_link_replacements": {
   "https://somewhere.example.com/some/path/to/a/some_schema.json": {
      "full_match": true,
      "replace_with": "https://docserver.example.org/some_schema_doc.html"
   },
   "fancy": {
      "full_match": false,
      "replace_with": "https://docserver.example.org/fancy_schemas.html"
   }
}
```

### schema_supplement

**Data type:** Dictionary

Maps schema names to a dictionary of structured content, including text overrides for property descriptions, replacements for unit abbreviations, schema-specific introductions, property description substitutions, and other supplementary data. All elements in this structure are optional. 

The structure of this object is:

```json
"schema_supplement": {
   "SchemaName": {
      "description": "A string to replace the schema description. Plain text or markdown.",
      "mockup": "A path or URI to a mockup file.",
      "jsonpayload": "A chunk of JSON.",
      "intro": "",
      "property_description_overrides": {
         "PropertyName": "a string, plain text or markdown.",
         "AnotherPropertyName": "a string, plain text or markdown."
      },
      "property_fulldescription_overrides": {
         "YetAnotherPropertyName": "a string, plain text or markdown. This string will also eliminate any additional data the doc generator would normally append to the description."
      },
      "property_details": {
         "EnumPropertyName": "A string, plain text or markdown. This will be inserted after the property description and prior to the table of enum details in the property information under Property Details.",
         "property_details": {
            "UUID": "\nThe UUID property contains a value that represents the universal unique identifier number (UUID) of a system.\n\nThe UUID property is a string data type. The format of the string is the 35-character string format specified in RFC4122: \"xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx\". Each x represents a hexadecimal digit (0-f).\n\nRegarding the case of the hex values, RFC4122 specifies that the hex values should be lowercase characters. Most modern scripting languages typically also represent hex values in lowercase characters following the RFC. However, dmidecode, WMI and some Redfish implementations currently use uppercase characters for UUID on output."
         }
      }
   }
}
```

In this structure:

| Attribute    | Description                                                   |
| :----------- | :------------------------------------------------------------ |
| `SchemaName` | Defines the schema name as either a bare schema name or a schema name with an underscore and an appended major version.<br/><br/>For example, `"ComputerSystem"` or `"ComputerSystem_2"`. |
| `description` | Replaces the description of the schema. |
| `intro`  | Defines a string to replace the description or append to the `description` string, if provided. |
| `mockup` | Mutually exclusive with `jsonpayload`. If you specify both attributes, `mockup` takes precedence.<blockquote><b>Note:</b> If you specify a <code>payload_dir</code> key in the <a href="README-base-configuration-file.md" title="README-base-configuration-file">base configuration file</a>, the payload directory takes precedence over <code>mockup</code>.</blockquote> |
| `jsonpayload` | Mutually exclusive with `mockup`. If you specify both attributes, `mockup` takes precedence.<blockquote><b>Note:</b> If you specify a <code>payload_dir</code> key in the <a href="README-base-configuration-file.md" title="README-base-configuration-file">base configuration file</a>, the payload directory takes precedence over <code>jsonpayload</code>.</blockquote> |

### units_translation

**Data type:** Dictionary

Maps Redfish schema units to units as you want them to appear in the documentation. -->
