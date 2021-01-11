# Redfish docs generator: Configuration

## Contents

* [Base configuration file: Supported keys](#base-configuration-file-supported-keys)
* [Attribute details](#attribute-details)
   * [combine_multiple_refs attribute](#combine_multiple_refs-attribute)
   * [object_reference_disposition attribute](#object_reference_disposition-attribute)
   * [payload_dir attribute](#payload_dir-attribute)
   * [profile_terse attribute](#profile_terse-attribute)
* [Content supplement configuration file: Supported attributes](#content-supplement-configuration-file-supported-attributes)
* [Attribute details](#attribute-details-1)
   * [schema_link_replacements attribute](#schema_link_replacements-attribute)
   * [schema_supplement attribute](#schema_supplement-attribute)
* [Examples](#examples)
   * [Produce full documentation, in HTML format](#produce-full-documentation-in-html-format)
   * [Produce full documentation, with normative descriptions and in HTML format](#produce-full-documentation-with-normative-descriptions-and-in-html-format)
   * [Produce Profile output (terse mode, markdown format)](#produce-profile-output-terse-mode-markdown-format)
   * [Produce Subset documentation (HTML format)](#produce-subset-documentation-html-format)
   * [Produce Property Index output (HTML format):](#produce-property-index-output-html-format)
   * [Produce CSV output:](#produce-csv-output)

The Redfish docs generator &mdash; [`doc_generator.py`](#doc_generator.py) &mdash; configuration files support most of the `doc_generator.py` command-line arguments except for the `--help` and `--config` arguments.

The configuration files support additional configuration options for some output modes.

If you specify an option in more than one way, command-line arguments override configuration file arguments.

You must format configuration files in valid JSON Schema format.

The [base configuration file](#base-configuration-file-supported-attributes) is a JSON file that can specify most of the options available for the doc generator, including the command-line options. You also specify the location of other configuration files, including the content supplement and introduction and postscript boilerplate files.

The [Content Supplement file](#content-supplement-config-file-supported-attributes) is a JSON file that contains text replacements and additions to be applied to the generated schema documentation. It includes text overrides for property descriptions, units translation (replacements for unit abbreviations), and schema-specific content including intros, postscripts, and property description substitutions.

## Base configuration file: Supported keys

Note that some configuration key names differ from their command-line counterparts. Unless otherwise noted, the meaning of the configuration key is the same as its command-line counterpart. The `uri_mapping` attribute is expected. All other attributes are optional in configuration files.

| Configuration key           | Command-line equivalent | Type    | Description                                   |
| :-------------------------- | :---------------------- | :------ | : ------------------------------------------- |
| `actions_in_property_table` |                         | Boolean | If `true`, omit `"Actions"` from the property tables. |
| `add_toc`                   |                         | Boolean | If `true`, generate a table of contents and either substitute it for `[add_toc]` in the boilerplate (intro or postscript), or place it at the beginning of the output document. Makes sense only for HTML mode. If `[add_toc]` appears anywhere in the boilerplate, default is `true`. |
| `boilerplate_intro`         |                         |         | Location of a Markdown file providing content to place at the beginning of the document (prior to the generated schema documentation). If a relative path, should be relative to the location of the configuration file. |
| `boilerplate_postscript`    |                         |         | Location of a Markdown file providing content to place at the end of the document (after to the generated schema documentation). If a relative path, should be relative to the location of the config file. |
<!-- | `combine_multiple_refs`     | | Integer | Threshold at which multiple references to the same object within a schema are moved into Property details, instead of expanded in place. For details, see [combine_multiple_refs attribute](#combine_multiple_refs-attribute). |
| `content_supplement`        | | | Location of a JSON-formatted content supplement file, which specifies content substitutions to be made within the generated schema documentation. If a relative path, must be relative to the location of the configuration file. |
| `escape_chars` | `escape` | | Characters to escape in generated Markdown. For example, use `--escape=@` if strings with embedded `@` are being converted to `mailto` links by your Markdown processor. |
| `excluded_annotations` | | List of annotation names (strings) to omit. Wildcard match is supported for strings that begin with `"*"`. |
| `excluded_pattern_properties` | | | Pattern properties to omit from output. Note that backslashes must be escaped in JSON (`"\"` becomes `"\\"`). |
| `excluded_properties` | | | List of property names (strings) to omit. Wildcard match is supported for strings that begin with `"*"` (`"*odata.count"` matches `"Members\@odata.count"` and others). |
| `excluded_schemas` | | | Schemas, by name, to omit from output. |
| `format` | `format` | | Output format. Value is `markdown`, `slate`, `html`, or `csv`. |
| `html_title` | | String | HTML `title` element in HTML output. |
| `import_from` | | | File name or directory that contains the JSON schemas to process. Wild cards are acceptable. Default: `json-schema`. |
| `locale`| | | Locale code (case-sensitive) for localized output. Localization of strings supplied by the doc generator code uses gettext. Locale files go in the `locale` directory in the `doc_generator` root. Translated descriptions and annotations may be supplied in localized JSON schema files. |
| `normative`| | | Produce normative (developer-focused) output. |
| `object_reference_disposition`| | | Data structure that specifies properties that should be moved to the **Common Objects** clause and/or objects that should be included inline where they are referenced, to override default behavior. For details, see [object_reference_disposition attribute](#object-reference-disposition-attribute) |
| `omit_version_in_headers`| | Boolean | If `true`, omit schema versions in clause headers. |
| `outfile` `out`| | | Output file (default depends on output format: `output.md` for Markdown, `index.html` for HTML, `output.csv` for CSV. |
| `payload_dir` | `payload_dir` | | Directory location for JSON payload and Action examples. Optional. For details, see [payload_dir attribute](#payload-dir-attribute) | 
| `profile_doc` | `profile` | | Path to a JSON profile document, for profile output. |
| `profile_terse` | `terse` | Boolean | Produce *terse* profile output; meaningful only in profile mode. For details, see [profile_terse attribute](#profile-terse-attribute) |
| `profile_uri_to_local` | | For profile mode only, an object like uri_mapping, for locations of profiles. |
| `property_index` | `property_index` |  Boolean | Produce **Property Index** output. For details, see [Redfish docs generator: Property index mode](README_Property_Index.md) |
| `property_index_config_out` | `property_index_config_out` | | Generate an updated configuration file, with specified file name (property_index mode only). |
| `registry_uri_to_local` | | For profile mode only, an object like uri_mapping, for locations of registries. |
| `subset` | `subset` | | Path to a JSON profile document. Generates **Schema subset** output, with the subset defined in the JSON profile document. |
| `uri_mapping` | Object | Partial URL of schema repositories as attributes, and local directory paths as values. | -->

## Attribute details

### combine_multiple_refs attribute

The `combine_multiple_refs` attribute specifies a threshold at which multiple references to the same object within a schema are moved into **Property details** instead of expanded in place. For example, to move an object to **Property details** if it is referred to three or more times:

```json
"combine_multiple_refs": 3,
```

### object_reference_disposition attribute

The `object_reference_disposition` attribute specifies a JSON object with either or both these fields:

* `common_object`. List of property names. For example `"Redundancy"`. 
* `include`. List of properties by their full path.

For example:

```json
"object_reference_disposition": {
  "common_object": ["Redundancy"],
  "include": [
    "http://redfish.dmtf.org/schemas/v1/PCIeDevice.json#/definitions/PCIeInterface"
  ]
}
```

### payload_dir attribute

The `payload_dir` attribute specifies a directory location for JSON payload and Action examples. If relative, this path is relative to the working directory in which the `doc_generator.py` script is run. Within the payload directory, use the following naming scheme for example files:

* &lt;schema_name&gt;-v&lt;major_version&gt;-example.json for JSON payloads
* &lt;schema_name&gt;-v&lt;major_version&gt;-action-&lt;action_name&gt;.json for action examples

### profile_terse attribute

The `profile_terse` attribute is meaningful only when a profile document is also specified. When `true`, *terse* output is produced. By default, profile output is verbose and includes all properties regardless of profile requirements. *Terse* output is intended for use by Service developers, including only the subset of properties with profile requirements.

## Content supplement configuration file: Supported attributes

| Attribute | Type | Description | Details |
| :-------- | :--- | :---------- | :------ |
| `property_description_overrides` | Dictionary | Maps property names to strings to use to replace the descripions of the named properties. |
| `property_fulldescription_overrides` | Dictionary | Just like `property_description_overrides`. These replacements are *full* in that any additional information the `doc_generator.py` normally appends, like a reference to the definition of the property in another schema, is omitted. |
| `schema_link_replacements` | Dictionary | Maps URIs of schema references to a structure specifying match type (full or partial) and replacement URIs. Use to substitute a link to documentation where a link to a specific schema would otherwise appear in the documentation. | [schema_link_replacements attribute](#schema-link-replacements-attribute)|
| `schema_supplement` | Dictionary | Maps schema names to a dictionary of structured content, including introductory text and schema-specific text replacements. | [schema_supplement attribute](#schema-supplement-attribute) |
| `units_translation` | Dictionary | Maps units as they appear in Redfish schemas to units as you want them to appear in the documentation. |

## Attribute details

### schema_link_replacements attribute

The `schema_link_replacements` attribute defines a dictionary mapping URIs of schema references to replacement URIs. Use to substitute a link to documentation where a link to a specific schema would otherwise appear in the documentation. The structure of this dictionary is:

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

### schema_supplement attribute

The `schema_supplement` attribute defines a dictionary of structured content, including text overrides for property descriptions, units translation (replacements for unit abbreviations), schema-specific intros, property description substitutions, and other supplementary data. The structure of this object looks like this (all fields are optional):

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

Here, `SchemaName` might be a bare schema name, or it might be a schema name with an underscore and major version appended. For example, `"ComputerSystem"` or `"ComputerSystem_2"`.

If `description` or `intro` are specified for a schema, that value replaces the description of the schema. If both are specified, the `description` is output, followed by the `intro`.

The `mockup` and `jsonpayload` attributes are mutually exclusive. If you specify both attributes, the content at `mockup` takes precedence. If you specify a `payload_dir` in the base configuration file, a payload directory is preferred over using these attributes.

## Examples

Several files in the `sample_inputs` directory provide examples of configuration files that you can use to produce different types of documentation. The following examples show some command-line invocations.

These examples assume that you have a clone of the DMTF/Redfish repo and the DMTF/Redfish-Tools repo in the same parent directory, and that your working directory is the Redfish clone, so that the schemas are in `./json-schema` and `doc_generator.py` is at `../Redfish-Tools/doc-generator/doc_generator.py` relative to your current working directory.

Note that the config files themselves contain references to other files in this directory.

### Produce full documentation, in HTML format

```
python ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/standard_html/config.json
```

Note that the `object_reference_disposition` in this config file identifies specific behavior for the `Redundancy` resource and for `PCIeInterface`, defined in `PCIeDevice`.

### Produce full documentation, with normative descriptions and in HTML format

```
python ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/standard_html/config_normative.json
```

### Produce Profile output (terse mode, markdown format)

```
python ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/profile_mode/config.json
```

Config file references the profile `OCPBasicServer.v1_0_0.json`, which in turn references `OCPManagedDevice.v1_0_0.json`.

### Produce Subset documentation (HTML format)

```
python ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/subset/config.json
```

Config file references the profile `OCPBasicServer.v1_0_0.json`, which in turn references `OCPManagedDevice.v1_0_0.json`.

### Produce Property Index output (HTML format):

```
python ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/property_index/config.json
```

Note that the Base Configuration file for property index output includes some elements that are specific to that mode: `description_overrides`.

### Produce CSV output:

```
python ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/csv/config.json
```
