[![Build Status](https://travis-ci.com/DMTF/Redfish-Tools.svg?branch=master)](https://travis-ci.com/github/DMTF/Redfish-Tools)
<p align="center">
  <img src="http://redfish.dmtf.org/sites/all/themes/dmtf2015/images/dmtf-redfish-logo.png" alt="DMTF Redfish" width=180>

# Redfish doc generator: Content supplement configuration file

Contains text replacements and additions to apply to the generated schema documentation. Includes text overrides for property descriptions, replacements for unit abbreviations, and schema-specific content including introductions, postscripts, and property description substitutions.

* [Content supplement configuration file example](#content-supplement-configuration-file-example)
* [Supported keys](#supported-keys)
* [schema_link_replacements key](#schema_link_replacements-key)
* [schema_supplement key](#schema_supplement-key)

## Content supplement configuration file example

```json
{
   "description": "Redfish doc generator Example: content supplement config file for output of standard-mode documentation in HTML format.",
   "keywords": {
      "html_title": "Title from the supplemental doc"
   },
   "units_translation": {
      "s": "seconds",
      "Mb/s": "Mbits/second",
      "By": "bytes",
      "Cel": "Celsius",
      "MiBy": "mebibytes",
      "W": "Watts",
      "V": "Volts",
      "mW": "milliWatts",
      "m": "meters"
   },
   "property_description_overrides": {
      "Oem": "See the OEM object definition in the [Using this guide](#using-this-guide) section."
   },
   "schema_supplement": {
      "ComputerSystem": {
         "property_details": {
            "UUID": "\nThe UUID property contains a value that represents the universal unique identifier number (UUID) of a system.\n\nThe UUID property is a string data type. The format of the string is the 35-character string format specified in RFC4122: \"xxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx\". Each x represents a hexadecimal digit (0-f).\n\nRegarding the case of the hex values, RFC4122 specifies that the hex values should be lowercase characters. Most modern scripting languages typically also represent hex values in lowercase characters following the RFC. However, dmidecode, WMI and some Redfish implementations currently use uppercase characters for UUID on output."
         }
      }
   }
}
```

## Supported keys

The content supplement configuration file is supported in these output modes:

* [Profile mode](README.md#profile-mode "README.md#profile-mode")
* [Standard](README.md#standard-mode)&nbsp;HTML
* Normative&nbsp;standard&nbsp;HTML
* [Subset](README.md#subset-mode)

<table>
   <thead>
      <tr>
         <th align="left" valign="top">Configuration&nbsp;key</th>
         <th align="left" valign="top">Type</th>
         <th align="left" valign="top">Description</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td align="left" valign="top"><code>property_description_overrides</code></td>
         <td align="left" valign="top">Dictionary</td>
         <td align="left" valign="top">Maps property names to strings to use to replace the descriptions of the named properties.</td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>property_fulldescription_overrides</code></td>
         <td align="left" valign="top">Dictionary</td>
         <td align="left" valign="top">Just like <code>property_description_overrides</code>. These replacements are <i>full</i> in that any additional information the <code>doc_generator.py</code> normally appends, like a reference to the definition of the property in another schema, is omitted.</td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>schema_link_replacements</code></td>
         <td align="left" valign="top">Dictionary</td>
         <td align="left" valign="top">Maps URIs of schema references to a structure that specifies either the full or partial match type and replacement URIs. Use to substitute a link to documentation where a link to a specific schema would otherwise appear in the documentation. See <a href="#schema_link_replacements-key">schema_link_replacements key</a>.</td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>schema_supplement</code></td>
         <td align="left" valign="top">Dictionary</td>
         <td align="left" valign="top">Maps schema names to a dictionary of structured content, including introductory text and schema-specific text replacements.See <a href="#schema_supplement-key">schema_supplement key</a>.</td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>units_translation</code></td>
         <td align="left" valign="top">Dictionary</td>
         <td align="left" valign="top">Maps units as they appear in Redfish schemas to units as you want them to appear in the documentation.</td>
      </tr>
   </tbody>
</table>

For an example of the content supplement configuration file, see <a href="sample_inputs/standard_html/content_supplement.json"><code>content_supplement.json</code></a>.

## schema_link_replacements key

The `schema_link_replacements` key is a dictionary that maps reference URIs to replacement URIs. The match type is full or partial. Replaces one link with another link. The dictionary structure is:

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

## schema_supplement key

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
