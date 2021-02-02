[![Build Status](https://travis-ci.com/DMTF/Redfish-Tools.svg?branch=master)](https://travis-ci.com/github/DMTF/Redfish-Tools)
<p align="center">
  <img src="http://redfish.dmtf.org/sites/all/themes/dmtf2015/images/dmtf-redfish-logo.png" alt="DMTF Redfish" width=180></p>

# Redfish doc generator: Configuration and supplemental files

Copyright 2016-2021 Distributed Management Task Force, Inc. All rights reserved.

To configure the generated documentation, you specify configuration keys in the [base configuration file](#base-configuration-file "#base-configuration-file") and command-line arguments. If you specify a configuration option in more than one way, command-line arguments take precedence over configuration keys.

## Contents

* [Base configuration file](#base-configuration-file)
* [Content supplement configuration file](#content-supplement-configuration-file)
* [Boilerplate intro file](#boilerplate-intro-file)
* [Boilerplate postscript file](#boilerplate-postscript-file)

## Base configuration file

The base configuration file is a JSON file that configures the generated documentation and can include pointers to the [content supplement configuration file](#content-supplement-configuration-file "#content-supplement-configuration-file") and the [boilerplate intro](#boilerplate-intro-file "#boilerplate-intro-file") and [boilerplate postscript](#boilerplate-postscript-file "#boilerplate-postscript-file") supplemental files.

The doc generator reads configuration keys from the [base configuration file](#base-configuration-file). If the base configuration file includes a pointer to the [content supplement configuration file](#content-supplement-configuration-file), the doc generator also reads configuration keys from it. 

Additionally, if the base configuration file includes pointers to the [boilerplate intro](#boilerplate-intro-file "#boilerplate-intro-file") and [boilerplate&nbsp;postscript](#boilerplate-postscript-file "#boilerplate-postscript-file") supplemental files, the doc generator includes content from these files in the generated output.

Depending on the [output mode](README.md#output-modes "README.md#output-modes"), the configuration keys in the base configuration file can change. Some output modes, such as the property index mode, support additional configuration keys.

To include supplemental files and the content supplement configuration file:

1. Add a pointer to these files at the bottom of the base configuration file:

    ```json
    {
    	...
    	"boilerplate_intro": "./intro.md",
    	"boilerplate_postscript": "./postscript.md", 
    	"content_supplement": "./content_supplement.json"
    }
    ``` 

For the descriptions of the keys in the base configuration file, see [Redfish doc generator: Base configuration file keys](README-base-configuration-file.md "README-base-configuration-file.md").

## Content supplement configuration file

The content supplement configuration file is a JSON file that that defines text overrides for property descriptions, replacements for unit abbreviations, and schema-specific content to apply to the generated schema documentation. The base configuration file contains a pointer to this file.

The content supplement configuration file is a JSON file that defines text overrides for property descriptions, replacements for unit abbreviations, and schema-specific content to apply to the generated schema documentation.

These output modes support the content supplement configuration file:

| Output mode | Sample content supplement configuration file |
| :---------- | :------------------------------------------- |
| <a href="README.md#profile-mode" title="README.md#profile-mode">Profile mode</a> | [`sample_inputs/profile_mode/content_supplement.json`](sample_inputs/profile_mode/content_supplement.json "sample_inputs/profile_mode/content_supplement.json") |
| [Standard mode](README.md#standard-mode "README.md#standard-mode") | [`sample_inputs/standard_html/content_supplement.json`](sample_inputs/standard_html/content_supplement.json "sample_inputs/standard_html/content_supplement.json") |
| <a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a> | [`sample_inputs/standard_html/content_supplement.json`](sample_inputs/standard_html/content_supplement.json "sample_inputs/standard_html/content_supplement.json") |
| [Subset mode](README.md#subset-mode "README.md#subset-mode") | [`sample_inputs/subset/content_supplement.json`](sample_inputs/subset/content_supplement.json "sample_inputs/subset/content_supplement.json") |

### Content supplement configuration file keys

* [property_description_overrides](#property_description_overrides)
* [property_fulldescription_overrides](#property_fulldescription_overrides)
* [schema_link_replacements](#schema_link_replacements)
* [schema_supplement](#schema_supplement)
* [units_translation](#units_translation)

### property_description_overrides

Dictionary

Maps property names to strings that replace the descriptions of the named properties.

### property_fulldescription_overrides

Dictionary. Maps property names to strings that replace the descriptions of the named properties. These replacements are *full* in that the doc generator omits any additional information that it normally appends, like a reference to the definition of the property in another schema.

### schema_link_replacements

Dictionary

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

In this structure:

| Attribute    | Description                                                   |
| :----------- | :------------------------------------------------------------ |
| URI | Defines the URI to replace. |
| `full_match` | Boolean. If `true`, the match is full. Otherwise, the match is partial. |
| `replace_with`  | Defines the replacement URI. |

### schema_supplement

Dictionary

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
| `mockup` | Mutually exclusive with `jsonpayload`. If you specify both attributes, `mockup` takes precedence.<blockquote><b>Note:</b> If you specify a <code>payload_dir</code> key in the <a href="#base-configuration-file" title="#base-configuration-file">base configuration file</a>, the payload directory takes precedence over <code>mockup</code>.</blockquote> |
| `jsonpayload` | Mutually exclusive with `mockup`. If you specify both attributes, `mockup` takes precedence.<blockquote><b>Note:</b> If you specify a <code>payload_dir</code> key in the <a href="#base-configuration-file" title="#base-configuration-file">base configuration file</a>, the payload directory takes precedence over <code>jsonpayload</code>.</blockquote> |

### units_translation

Dictionary

Maps Redfish schema units to units as you want them to appear in the documentation.

## Boilerplate intro file

**Sample boilerplate intro file:** <a href="sample_inputs/standard_html/intro.md"><code>intro.md</code></a>

The boilerplate intro file is a Markdown or HTML file that contains supplementary content to include in the output before the generated documentation.

This file can include an <code>[add_toc]</code> directive that specifies location for the table of contents.

## Boilerplate postscript file

**Sample boilerplate postscript file:** <a href="sample_inputs/standard_html/postscript.md"><code>postscript.md</code></a>

The boilerplate postscript file is a Markdown or HTML file that contains supplementary content to include in the output after the generated documentation.

This file can include an <code>[add_toc]</code> directive that specifies location for the table of contents.
