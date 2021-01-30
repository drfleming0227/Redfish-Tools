[![Build Status](https://travis-ci.com/DMTF/Redfish-Tools.svg?branch=master)](https://travis-ci.com/github/DMTF/Redfish-Tools)
<p align="center">
  <img src="http://redfish.dmtf.org/sites/all/themes/dmtf2015/images/dmtf-redfish-logo.png" alt="DMTF Redfish" width=180>

# Redfish doc generator: Content supplement configuration file

The content supplement configuration file is a JSON file that defines text overrides for property descriptions, replacements for unit abbreviations, and schema-specific content to apply to the generated schema documentation.

These output modes support the content supplement configuration file:

| Output mode | Sample content supplement configuration file |
| :---------- | :------------------------------------------- |
| [Profile mode](README.md#profile-mode "README.md#profile-mode") | [`sample_inputs/profile_mode/content_supplement.json`](sample_inputs/profile_mode/content_supplement.json "sample_inputs/profile_mode/content_supplement.json") |
| [Standard mode](README.md#standard-mode "README.md#standard-mode") | [`sample_inputs/standard_html/content_supplement.json`](sample_inputs/standard_html/content_supplement.json "sample_inputs/standard_html/content_supplement.json") |
| [Standard normative mode](README.md#standard-normative-mode "README.md#standard-normative-mode") | [`sample_inputs/standard_html/content_supplement.json`](sample_inputs/standard_html/content_supplement.json "sample_inputs/standard_html/content_supplement.json") |
| [Subset mode](README.md#subset-mode "README.md#subset-mode") | [`sample_inputs/subset/content_supplement.json`](sample_inputs/subset/content_supplement.json "sample_inputs/subset/content_supplement.json") |

## Configuration keys

* [property_description_overrides key](#property_description_overrides-key)
* [property_fulldescription_overrides key](#property_fulldescription_overrides-key)
* [schema_link_replacements key](#schema_link_replacements-key)
* [schema_supplement key](#schema_supplement-key)
* [units_translation key](#units_translation-key)

### property_description_overrides key

A dictionary, this key maps property names to strings to use to replace the descriptions of the named properties.

### property_fulldescription_overrides key

A dictionary, this key maps property names to strings to use to replace the descriptions of the named properties. These replacements are <i>full</i> in that the doc generator omits any any additional information that it normally appends, like a reference to the definition of the property in another schema.

### schema_link_replacements key

A dictionary, this key maps URIs of schema references to a structure that specifies either the full or partial match type and replacement URIs. Use to substitute a link to documentation where a link to a specific schema would otherwise appear in the documentation. See <a href="#schema_link_replacements-key">schema_link_replacements key</a>.The `schema_link_replacements` key is a dictionary that maps reference URIs to replacement URIs. The match type is full or partial. Replaces one link with another link. The dictionary structure is:

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

### schema_supplement key

A dictionary, this key maps schema names to a dictionary of structured content, including introductory text and schema-specific text replacements.

The `schema_supplement` key defines a dictionary of structured content, including text overrides for property descriptions, units translation (replacements for unit abbreviations), schema-specific intros, property description substitutions, and other supplementary data. The structure of this object looks like this (all fields are optional):

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

In this file, `SchemaName` might be either a bare schema name or a schema name with an underscore and major version appended. For example, `"ComputerSystem"` or `"ComputerSystem_2"`.

If `description` or `intro` are specified for a schema, that value replaces the description of the schema. If both are specified, the `description` is output, followed by the `intro`.

The `mockup` and `jsonpayload` attributes are mutually exclusive. If you specify both attributes, the content at `mockup` takes precedence. If you specify a `payload_dir` in the base configuration file, a payload directory is preferred over using these attributes.

### units_translation key

A dictionary, this key maps units as they appear in Redfish schemas to units as you want them to appear in the documentation.
