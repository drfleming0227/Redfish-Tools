[![Build Status](https://travis-ci.com/DMTF/Redfish-Tools.svg?branch=master)](https://travis-ci.com/github/DMTF/Redfish-Tools)
<p align="center">
  <img src="http://redfish.dmtf.org/sites/all/themes/dmtf2015/images/dmtf-redfish-logo.png" alt="DMTF Redfish" width=180>

# Redfish doc generator: Configuration and supplementary files

To configure output, the **Redfish doc generator** accepts input from the command line and configuration and supplementary content files.

This topic describes:

* Configuration input from JSON configuration files:

   * <a href="#base-configuration-file">Base configuration file</a> defines configuration options including pointers to the content supplement configuration file and the supplementary content files.

       Depending on the <a href="#output-modes">output mode</a>, the configuration keys in the base configuration file can change. Some output modes, such as the property index mode, support additional configuration keys.
   * <a href="#content-supplement-configuration-file">Content&nbsp;supplement&nbsp;configuration&nbsp;file</a> defines text overrides for property descriptions, replacements for unit abbreviations, and schema-specific content including introductions, postscripts, and property description substitutions. The base configuration file contains a pointer to this file.

* Supplementary content from HTML or Markdown files:

   * The <a href="#boilerplate-intro-supplementary-file">boilerplate&nbsp;intro supplementary file</a> defines content to include in the output before the generated documentation.
   * The <a href="#boilerplate-postscript-supplementary-file">boilerplate&nbsp;postscript&nbsp;supplementary&nbsp;file</a> defines content to include in the output after the generated documentation.

If you specify an option in more than one way, command&#8209;line arguments override the configuration file keys.

## Contents

* [Output modes](#output-modes)
* [Base configuration file](#base-configuration-file)
* [Content supplement configuration file](#content-supplement-configuration-file)
* [Subset configuration file](#subset-configuration-file)
* [Property index configuration file](#property-index-configuration-file)
* [Boilerplate intro supplementary file](#boilerplate-intro-supplementary-file)
* [Boilerplate postscript supplementary file](#boilerplate-postscript-supplementary-file)
* [Redfish doc generator examples](#redfish-doc-generator-examples)

## Output modes

An output mode is a combination of an output format, such as Markdown or HTML, and a specific type of output, such as a developer-focused, or normative, document or a property index. So you could produce a normative HTML document or a standard HTML document.

The doc generator supports several output modes through various command-line or configuration options. The following table:

* Lists the supported output modes.
* Provides links to sample versions of the base configuration file.
* Provides links to examples of `doc_generator.py` command usage.

| Output mode        | Sample base configuration file | Example command usage |
| :----------------- | :----------------------------- | :-------------------- |
| CSV                | [`sample_inputs/csv/config.json`](sample_inputs/csv/config.json) | [CSV](#csv) |
| Profile            | [`sample_inputs/profile_mode/config.json`](sample_inputs/profile_mode/config.json) | [Profile index Markdown in terse mode](##profile-index-markdown-in-terse-mode) |
| Property index     | [`sample_inputs/property_index/config.json`](sample_inputs/property_index/config.json) | [Property index HTML](##property-index-html) |
| Standard           | [`sample_inputs/standard_html/config.json`](sample_inputs/standard_html/config.json) | [Standard HTML](##standard-html) |
| Standard normative | [`sample_inputs/standard_html/config_normative.json`](sample_inputs/standard_html/config_normative.json) | [Standard with normative descriptions HTML](##standard-html-with-normative-descriptions) |
| Subset             | [`sample_inputs/subset/config.json`](sample_inputs/subset/config.json) | [Subset HTML](##subset-html) |

Depending on the output mode, the configuration keys in the base configuration file can change. Some output modes, such as the property index mode, support additional configuration keys.

## Base configuration file

The base configuration file is a JSON file that configures the generated output and can include pointers to the <a href="#content-supplement-configuration-file-overview">content supplement configuration file</a> and the [boilerplate intro](#boilerplate-intro-file) and [boilerplate postscript](#boilerplate-postscript-file) supplementary content files.

* [Supported keys](#supported-keys)
* [combine_multiple_refs key](#combine_multiple_refs-key)
* [object_reference_disposition key](#object_reference_disposition-key)
* [payload_dir key](#payload_dir-key)
* [profile_terse key](#profile_terse-key)

### Supported keys

The names of some configuration keys differ from their command&#8209;line argument equivalents. Unless otherwise noted, the configuration key has the same meaning as its command&#8209;line argument equivalent. The `uri_mapping` configuration key is required but all other configuration keys are optional.

The clauses briefly describes each key and the output modes that support the key:

* `actions_in_property_table` key

  **Supported output modes:** Subset

   Boolean. Value is:

   <ul>
      <li><code>true</code>. (Default) Include <code>Actions</code> in property tables. </li>
      <li><code>false</code>. Exclude <code>Actions</code> from property tables. </li>
   </ul>

* `add_toc` key

  **Supported output modes:** Standard, standard normative

  Boolean. By default, the table of contents (TOC) appears at the top of the HTML output. If the <code>[add_toc]</code> directive appears anywhere in the boilerplate intro or boilerplate postscript file, <code>add_toc</code> key is <code>true</code> by default.</p>
  <p>Value is:</p>
  <ul>
      <li>
         <p><code>true</code>. (Default) Generate a TOC and place it either:</p>
         <ul>
            <li>At the beginning of the generated HTML file.</li>
            <li>In the <code>[add_toc]</code>location if that directive appears in the boilerplate intro or boilerplate postscript file.</li>
         </ul>
      </li>
      <li><code>false</code>. Do not generate a TOC.</li>
   </ul>

* `boilerplate_intro` key

  **Supported output modes:** Profile, standard, standard normative, subset

  String. No default. Location of the HTML or Markdown file that contains content to appear at the beginning of the document before the generated schema documentation. If a relative path, should be relative to the location of the configuration file.

* `boilerplate_postscript` key

  **Supported output modes:** Standard, standard normative

  String. No default. Location of the HTML or Markdown file that contains content to appear at the end of the document after the generated schema documentation. If a relative path, should be relative to the location of the configuration file.

* `combine_multiple_refs` key

  **Supported output modes:** Standard, standard normative

   Integer. No default. Threshold at which multiple references to the same object within a schema are moved into <b>Property details</b> instead of expanded in place.<br /><br />For details, see <a href="#combine_multiple_refs-key">combine_multiple_refs key</a>.

   This setting specifies that multiple objects within a schema, that are defined by reference to the same definition, should have their definitions moved into the Property Details section, with a single-line (row) listing for each object in the main table. combine_multiple_refs is an integer threshold at which this behavior kicks in. If it is absent or 0, no combining occurs. If it is 2 or greater, combining occurs at that number of references to the same object. A setting of 1 does not make sense and should be prevented.

   The `combine_multiple_refs` key specifies a threshold at which multiple references to the same object within a schema are moved into **Property details** instead of expanded in place. For example, to move an object to **Property details** if it is referred to three or more times:

   ```json
   "combine_multiple_refs": 3,
   ```

* `content_supplement` key

  **Supported output modes:** Profile, standard, standard normative, subset

  String. No default. Location of a JSON-formatted content supplement file, which specifies content substitutions to be made within the generated schema documentation. If a relative path, must be relative to the location of the configuration file.

* `description_overrides` key

  **Supported output modes:** Property index

  String. ??

* `escape_chars` key

  **Supported output modes:** ??

   ??. No default. Characters to escape in generated Markdown. For example, use <code>--escape=@</code> if your Markdown processor converts embedded <code>@</code> characters to <code>mailto</code> links.

   <b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b> <code>escape</code>

* `excluded_annotations` key

  **Supported output modes:** CSV, profile, standard, standard normative, subset

   Array of strings. No default. List of annotation names to exclude.

   Wildcard match is supported for strings that begin with <code>\*</code>.

* `excluded_pattern_properties` key

   **Supported output modes:** CSV, profile, standard, standard normative, subset

   ??. No default. List of pattern properties to exclude from output.<br /><br />In JSON, you must escape back slashes (<code>"\"</code> becomes <code>"\\"</code>).

* `excluded_properties` key

  **Supported output modes:** CSV, profile, standard, standard normative, subset

  Array of strings. No default. List of property names to exclude. Wildcard match is supported for strings that begin with <code>*</code>. For example, <code>"*odata.count"</code> matches <code>"Members\@odata.count"</code> and others.

* `excluded_schemas` key

   **Supported output modes:** CSV, profile, standard, standard normative, subset

   Array of strings. No default. List of schemas, by name, to exclude from output.

* `format` key

  **Supported output modes:** CSV, profile, standard, standard normative, subset

  &nbsp;? Output format. Value is <code>markdown</code>, <code>slate</code>, <code>html</code>, or <code>csv</code>.

  **Equivalent&nbsp;command&#8209;line&nbsp;argument:** <code>format</code>

* `html_title` key

  **Supported output modes:** Standard, standard normative, subset

  String. No default. HTML <code>title</code> element in HTML output.

* `import_from` key

  **Supported output modes:** Standard, standard normative, subset

  String. File name or directory that contains the JSON schemas to process. Wild cards are acceptable. Default: <code>json-schema</code>.

  <b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b>&nbsp;<code>import_from</code>

* `locale` key

  **Supported output modes:** 

  No default. Case-sensitive locale code for localized output. Localization of strings supplied by the doc generator uses <a href="https://www.gnu.org/software/gettext/" title="https://www.gnu.org/software/gettext/"><code>gettext</code></a>. Locale files are in the <code>locale</code> directory in the <code>doc_generator</code> root. Translated descriptions and annotations may be supplied in localized JSON Schema files.

* `normative` key

  **Supported output modes:** Standard normative

  &nbsp;? No default. Produce normative (developer-focused) output.

* `object_reference_disposition` key

  **Supported output modes:** Standard, standard normative

  &nbsp;? No default. Data structure that specifies properties that should be moved to the <b>Common Objects</b> clause and/or objects that should be included in-line where they are referenced, to override default behavior. For details, see <a href="#object_reference_disposition-key">object_reference_disposition key</a>.

  The `object_reference_disposition` key specifies a JSON object with either or both these fields:

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

* `omit_version_in_headers` key

  **Supported output modes:** 

   Boolean. Not used.

   <p>No default.</p>
   <p>Value is:</p>
   <ul>
      <li><code>true</code>. Exclude schema versions from clause headers.</li>
      <li><code>false</code>. Include schema versions in clause headers.</li>
   </ul>

* `outfile` key

  **Supported output modes:** CSV, profile, property index, standard, standard normative, subset

   &nbsp;? No default. Output file (default depends on output format: <code>output.md</code> for Markdown, <code>index.html</code> for HTML, <code>output.csv</code> for CSV.

   <b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b> <code>out</code>

* `payload_dir` key

  **Supported output modes:** Standard, standard normative

   &nbsp;? No default. Directory location for JSON payload and Action examples. Optional.<br /><br />For details, see <a href="#payload_dir-key">payload_dir key</a>.

   The `payload_dir` key specifies a directory location for JSON payload and Action examples. If relative, this path is relative to the working directory in which the `doc_generator.py` script is run. Within the payload directory, use the following naming scheme for example files:

   * &lt;schema_name&gt;-v&lt;major_version&gt;-example.json for JSON payloads
   * &lt;schema_name&gt;-v&lt;major_version&gt;-action-&lt;action_name&gt;.json for action examples

   <b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b>&nbsp;<code>payload_dir</code>

* `profile_doc` key

  **Supported output modes:** Profile

   &nbsp;? No default. Path to a JSON profile document, for profile output.

   <b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b> <code>profile</code>

* `profile_terse` key

  **Supported output modes:** Profile

   Boolean. No default. Produce <i>terse</i> profile output; meaningful only in profile mode. For details, see <a href="#profile_terse-key">profile_terse key</a>.

   The `profile_terse` key is meaningful only when a profile document is also specified. When `true`, *terse* output is produced. By default, profile output is verbose and includes all properties regardless of profile requirements. *Terse* output is intended for use by Service developers, including only the subset of properties with profile requirements.

   <b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b> <code>terse</code>

* `profile_uri_to_local` key

  **Supported output modes:** Profile, subset

  &nbsp;? No default. For profile mode only, an object like <code>uri_mapping</code>, for locations of profiles.

* `property_index` key

  **Supported output modes:** Property index

  Boolean. No default. Produce <b>Property Index</b> output. For details, see <a href="README_Property_Index.md">Redfish doc generator: Property index mode</a>.

  <b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b> <code>property_index</code>

* `property_index_config_out` key

  **Supported output modes:** 

  &nbsp;? Not used. No default. Generate an updated configuration file, with specified file name (property_index mode only).

  <b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b> <code>property_index_config_out</code>

* `registry_uri_to_local` key

  **Supported output modes:** Profile

  &nbsp;? No default. For profile mode only, an object like <code>uri_mapping</code>, for locations of registries.

* `subset` key

  **Supported output modes:** Subset

  &nbsp;? No default. Path to a JSON profile document. Generates <b>Schema subset</b> output, with the subset defined in the JSON profile document.

  <b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b> <code>subset</code>

* `uri_mapping` key

  **Supported output modes:** CSV, profile, property index, standard, standard normative, subset

  Object. No default. Partial URL of schema repositories as attributes, and local directory paths as values.

## Content supplement configuration file

Contains text replacements and additions to apply to the generated schema documentation. Includes text overrides for property descriptions, replacements for unit abbreviations, and schema-specific content including introductions, postscripts, and property description substitutions.

* [Content supplement configuration file example](#content-supplement-configuration-file-example)
* [Supported keys](#supported-keys-1)
* [schema_link_replacements key](#schema_link_replacements-key)
* [schema_supplement key](#schema_supplement-key)

### Content supplement configuration file example

```json
{
   "description": "Redfish Documentation Generator Example: content supplement config file for output of standard-mode documentation in HTML format.",
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

### Supported keys

The content supplement configuration file is supported in these output modes:

* Profile
* Standard&nbsp;HTML
* Normative&nbsp;standard&nbsp;HTML
* Subset

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

### schema_link_replacements key

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

### schema_supplement key

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

## Subset configuration file

Used in <b>subset mode</b> to generate <b>Schema subset</b> output, with the subset defined in the JSON profile document.

```json
{
   "version": "The version string is optional. It may have (future?) meaning in property index mode.",
   "description": "Redfish Documentation Generator Example: config file for output of subset documentation in HTML format.",
   "format": "html",
   "import_from": ["./json-schema"],
   "outfile": "subset.html",
   "uri_mapping": {
      "redfish.dmtf.org/schemas/v1": "./json-schema"
   },
   "profile_uri_to_local": {
      "redfish.dmtf.org/profiles": "../Redfish-Tools/doc-generator/sample_inputs"
   },
   "suppress_version_history": true,
   "html_title": "Sample Profile-focused Document",
   "subset_doc": "../Redfish-Tools/doc-generator/sample_inputs/OCPBasicServer.v1_0_0.json",
   "excluded_annotations": ["*@odata.count", "*@odata.navigationLink"],
   "excluded_properties": ["@odata.context", "@odata.type", "@odata.id"],
   "excluded_schemas": ["*Collection"],
   "boilerplate_intro": "./intro.md",
   "content_supplement": "./content_supplement.json"
}
```

## Property index configuration file

<p>Used in <b>property index mode</b> to generate <b>Property index</b> output, which is an index of property names and descriptions that includes property name, type, schemas where found, and descriptions found.</p>
<p>When you run run the doc generator in <b>property index mode</b>:</p>
<ul>
   <li>Only a few of <code>doc_generator.py</code> arguments apply.</li>
   <li>The <a href="#configuration">configuration file</a> takes a different form than the one used for the other output modes.</li>
</ul>

See [Redfish doc generator: Property index configuration](README_Property_Index.md).

## Boilerplate intro supplementary file

The boilerplate intro file is a Markdown or HTML that contains supplementary content to include in the output before the generated documentation. Can include an <code>[add_toc]</code> directive that specifies location for the table of contents.

For an example boilerplate intro file, see <a href="sample_inputs/standard_html/intro.md"><code>intro.md</code></a>.

## Boilerplate postscript supplementary file

The boilerplate postscript file is a Markdown or HTML that contains supplementary content to include in the output after the generated documentation. 

For an example boilerplate postscript file, see <a href="sample_inputs/standard_html/postscript.md"><code>postscript.md</code></a>.

## Redfish doc generator examples

Several files in the `sample_inputs` directory provide examples of configuration files that you can use to produce different types of documentation. The following examples show some command&#8209;line invocations.

These examples assume that you have a clone of the DMTF/Redfish repo and the DMTF/Redfish-Tools repo in the same parent directory, and that your working directory is the Redfish clone, so that the schemas are in `./json-schema` and `doc_generator.py` is at `../Redfish-Tools/doc-generator/doc_generator.py` relative to your current working directory.

> **Note:** The configuration files reference other files in this directory.

* [CSV](#csv)
* [Standard HTML](#standard-html)
* [Standard with normative descriptions HTML](#standard-html-with-normative-descriptions)
* [Profile index Markdown in terse mode](#profile-index-markdown-in-terse-mode)
* [Subset HTML](#subset-html)
* [Property index HTML](#property-index-html)

### CSV

**Not implemented**

```bash
% python3 ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/csv/config.json
```

### Standard HTML

```bash
% python3 ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/standard_html/config.json
```

Note that the `object_reference_disposition` in this config file identifies specific behavior for the `Redundancy` resource and for `PCIeInterface`, defined in `PCIeDevice`.

### Standard with normative descriptions HTML

```bash
% python3 ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/standard_html/config_normative.json
```

### Profile Markdown in terse mode

```bash
% python3 ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/profile_mode/config.json
```

Configuration file references the profile `OCPBasicServer.v1_0_0.json`, which in turn references `OCPManagedDevice.v1_0_0.json`.

### Subset HTML

```bash
% python3 ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/subset/config.json
```

Configuration file references the profile `OCPBasicServer.v1_0_0.json`, which in turn references `OCPManagedDevice.v1_0_0.json`.

### Property index HTML

```bash
% python3 ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/property_index/config.json
```

> **Note:** The base configuration file for property index output includes some elements that are specific to that mode: `description_overrides`.

