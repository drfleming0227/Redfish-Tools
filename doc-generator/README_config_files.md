# Redfish docs generator: Configuration and supplementary files

## Contents

* [About configuration and supplementary files](#about-configuration-and-supplementary-files)
* [Base configuration file](#base-configuration-file)
* [Content supplement configuration file](#content-supplement-configuration-file)
* [Subset configuration file](#subset-configuration-file)
* [Property index configuration file](#property-index-configuration-file)
* [Boilerplate intro file](#boilerplate-intro-file)
* [Boilerplate postscript file](#boilerplate-postscript-file)
* [Redfish docs generator examples](#redfish-docs-generator-examples)

## About configuration and supplementary files

The **Redfish docs generator** accepts:

* Configuration input from JSON configuration files
* Supplementary content from HTML or Markdown files

These files are:

<table width="100%">
   <col width="46%">
   <col width="8%"
   <col width="46%">
   <thead>
      <tr>
         <th align="left" valign="top">File</th>
         <th align="left" valign="top">Format</th>
         <th align="left" valign="top">Defines</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td align="left" valign="top"><a href="#base-configuration-file">Base&nbsp;configuration</a></td>
         <td align="left" valign="top">JSON</td>
         <td align="left" valign="top">Docs generator configuration options including pointers to the content supplement configuration file and the supplementary content files.</td>
      </tr>
      <tr id="content-supplement-configuration-file-overview">
         <td align="left" valign="top"><a href="#content-supplement-configuration-file">Content&nbsp;supplement&nbsp;configuration</a></td>
         <td align="left" valign="top">JSON</td>
         <td align="left" valign="top">Text replacements and additions to apply to the generated schema documentation. Includes text overrides for property descriptions, replacements for unit abbreviations, and schema-specific content including introductions, postscripts, and property description substitutions.</td>
      </tr>
      <tr>
         <td align="left" valign="top"><a href="#subset-configuration-file">Subset configuration</a></td>
         <td align="left" valign="top">JSON</td>
         <td align="left" valign="top">Subset information to include in a <i>Schema subset</i> document.</td>
      </tr>
      <tr>
         <td align="left" valign="top"><a href="#property-index-configuration-file">Property&nbsp;index configuration</a></td>
         <td align="left" valign="top">JSON</td>
         <td align="left" valign="top">Property index information to include in a <i>Property index</i> document.</td>
      </tr>
      <tr>
         <td align="left" valign="top"><a href="#boilerplate-intro-file">Boilerplate intro supplementary content</a></td>
         <td align="left" valign="top">HTML or Markdown</td>
         <td align="left" valign="top">Content to place in the output before the generated documentation.</td>
      </tr>
      <tr>
         <td align="left" valign="top"><a href="#boilerplate-postscript-file">Boilerplate&nbsp;postscript&nbsp;supplementary&nbsp;content</a></td>
         <td align="left" valign="top">HTML or Markdown</td>
         <td align="left" valign="top">Content to place in the output after the generated documentation.</td>
      </tr>
   </tbody>
</table>

Some output modes, such as the property index mode, support additional configuration options.

If you specify an option in more than one way, command&#8209;line arguments override the configuration file keys.

For examples of `doc_generator.py` command usage with various configuration files, see [Redfish docs generator examples](#redfish-docs-generator-examples).

## Base configuration file

The base configuration file is a JSON file that defines most of the docs generator confirmation options including pointers to the <a href="#content-supplement-configuration-file-overview">content supplement configuration file</a> and the [boilerplate intro](#boilerplate-intro-file) and [boilerplate postscript](#boilerplate-postscript-file) supplementary content files.

* [Supported keys](#supported-keys)
* [combine_multiple_refs key](#combine_multiple_refs-key)
* [object_reference_disposition key](#object_reference_disposition-key)
* [payload_dir key](#payload_dir-key)
* [profile_terse key](#profile_terse-key)

### Base configuration file example

[`config.json`](sample_inputs/standard_html/config.json)

```json
{
   "version": "The version string is optional. It may have (future?) meaning in property index mode.",
   "description": "Redfish Documentation Generator Example: config file for output of standard-mode documentation in HTML format.",
   "uri_mapping": {
      "redfish.dmtf.org/schemas/v1": "./json-schema"
   },
   "format": "html",
   "import_from": ["./json-schema"],
   "outfile": "standard.html",
   "payload_dir": "./mockups/DSP2046-examples",
   "add_toc": true,
   "html_title": "Sample Standard Output",
   "combine_multiple_refs": 3,
   "excluded_properties": [
      "@odata.context",
      "@odata.type", "@odata.id",
      "@odata.etag", "Name", "Id",
      "Description", "Oem"
   ],
   "excluded_annotations": [
      "*@odata.count",
      "*@odata.navigationLink"
   ],
   "excluded_schemas": ["*Collection",
      "HostedStorageServices",
      "StorageService",
      "StorageSystem", "idRef", "Oem"
   ],
   "excluded_pattern_properties": [
      "^([a-zA-Z_][a-zA-Z0-9_]*)?@(odata|Redfish|Message)\\.[a-zA-Z_][a-zA-Z0-9_]*$"
   ],
   "object_reference_disposition": {
      "common_object": ["Redundancy"],
      "include": [
         "http://redfish.dmtf.org/schemas/v1/PCIeDevice.json#/definitions/PCIeInterface"
      ]
   },
   "boilerplate_intro": "./intro.md",
   "boilerplate_postscript": "./postscript.md",
   "content_supplement": "./content_supplement.json"
}
```

### Supported keys

Note that some configuration keys differ from their command&#8209;line argument equivalents. Unless otherwise noted, the configuration key has the same meaning as its command&#8209;line argument equivalent. The `uri_mapping` configuration key is required but all other configuration keys are optional.

| Configuration key           | Type    |  Description                                        |
| :-------------------------- | :------ | :-------------------------------------------------- |
| `actions_in_property_table` | Boolean | <p>Subset mode.</p><p>Value is:</p><ul><li><code>true</code>. (Default) Include <code>Actions</code> in property tables.</li><li><code>false</code>. Exclude <code>Actions</code> from property tables.</li></ul> |
| `add_toc` | Boolean | <p>Standard HTML, normative.</p><p>By default, the table of contents (TOC) appears at the top of the HTML output. If the <code>[add_toc]</code> directive appears anywhere in the boilerplate intro or boilerplate postscript file, `add_toc` key is <code>true</code> by default.</p><p>Value is:</p><ul> <li> <p><code>true</code>. (Default) Generate a TOC and place it either:</p> <ul> <li>At the beginning of the generated HTML file.</li> <li>In the <code>[add_toc]</code>location if that directive appears in the boilerplate intro or boilerplate postscript file. </li> </ul> <li><code>false</code>. Do not generate a TOC.</li> </ul> |
| `boilerplate_intro` | String | <p>Profile mode, subset mode, standard HTML, normative.</p>No default. Location of the HTML or Markdown file that contains content to appear at the beginning of the document before the generated schema documentation. If a relative path, should be relative to the location of the configuration file. |
| `boilerplate_postscript` | String | <p>Standard HTML, normative.</p>No default. Location of the HTML or Markdown file that contains content to appear at the end of the document after the generated schema documentation. If a relative path, should be relative to the location of the config file. |
| `combine_multiple_refs` | Integer | <p>Standard HTML, normative.</p>No default. Threshold at which multiple references to the same object within a schema are moved into **Property details** instead of expanded in place.<br/><br/>For details, see [combine_multiple_refs key](#combine_multiple_refs-key). |
| `content_supplement` | String | <p>Profile mode, subset mode, standard HTML, normative.</p>No default. Location of a JSON-formatted content supplement file, which specifies content substitutions to be made within the generated schema documentation. If a relative path, must be relative to the location of the configuration file. |
| `escape_chars` |       | <p>Nowhere</p>No default. Characters to escape in generated Markdown. For example, use `--escape=@` if your Markdown processor converts embedded `@` characters to `mailto` links.<br/><br/>**Equivalent&nbsp;command&#8209;line&nbsp;argument:** `escape` |
| `excluded_annotations` | Array of strings | <p>Profile mode, subset mode, standard HTML, normative, CSV.</p>No default. List of annotation names to exclude.<br/><br/>Wildcard match is supported for strings that begin with `*`. |
| `excluded_pattern_properties` |       | <p>Profile mode, subset mode, standard HTML, normative, CSV.</p>No default. List of pattern properties to exclude from output.<br/><br/>In JSON, you must escape back slashes (`"\"` becomes `"\\"`). |
| `excluded_properties` | Array of strings | <p>Profile mode, subset mode, standard HTML, normative, CSV.</p>No default. List of property names to exclude. Wildcard match is supported for strings that begin with `*`. For example, `"*odata.count"` matches `"Members\@odata.count"` and others. |
| `excluded_schemas` | Array of strings | <p>Profile mode, subset mode, standard HTML, normative, CSV.</p>No default. List of schemas, by name, to exclude from output. |
| `format` |        | | <p>Profile mode, subset mode, standard HTML, normative, CSV.</p>Output format. Value is `markdown`, `slate`, `html`, or `csv`.<br/><br/>**Equivalent&nbsp;command&#8209;line&nbsp;argument:** `format` |
| `html_title` | String | <p>Standard HTML, normative,subset,content supplement.</p>No default. HTML `title` element in HTML output. |
| `import_from` | String | | <p>Profile mode, property index, subset mode, standard HTML, normative, CSV.</p>File name or directory that contains the JSON schemas to process. Wild cards are acceptable. Default: `json-schema`.<br/><br/>**Equivalent&nbsp;command&#8209;line&nbsp;argument:**&nbsp;`import_from` |
| `locale` |       | <p>Not used.</p>No default. Case-sensitive locale code for localized output. Localization of strings supplied by the docs generator uses [`gettext`](https://www.gnu.org/software/gettext/ "https://www.gnu.org/software/gettext/"). Locale files are in the `locale` directory in the `doc_generator` root. Translated descriptions and annotations may be supplied in localized JSON Schema files. |
| `normative` |       | <p>normative standard-mode.</p>No default. Produce normative (developer-focused) output. |
| `object_reference_disposition` |       | <p>Standard HTML, normative.</p>No default. Data structure that specifies properties that should be moved to the **Common Objects** clause and/or objects that should be included in-line where they are referenced, to override default behavior.<br/><br/>For details, see [object_reference_disposition key](#object_reference_disposition-key). |
| `omit_version_in_headers` | Boolean | <p>Not used.</p>No default. <p>Value is:</p><ul><li><code>true</code>. Exclude schema versions from clause headers.</li><li><code>false</code>. Include schema versions in clause headers.</li></ul> |
| `outfile` |       | <p>All</p>No default. Output file (default depends on output format: `output.md` for Markdown, `index.html` for HTML, `output.csv` for CSV.<br/><br/>**Equivalent&nbsp;command&#8209;line&nbsp;argument:** `out` |
| `payload_dir` |     | <p>Standard HTML, normative.</p>No default. Directory location for JSON payload and Action examples. Optional.<br/><br/>For details, see [payload_dir key](#payload_dir-key).<br/><br/>**Equivalent&nbsp;command&#8209;line&nbsp;argument:**&nbsp;`payload_dir` | 
| `profile_doc` |       | <p>Profile mode.</p>No default. Path to a JSON profile document, for profile output.<br/><br/>**Equivalent&nbsp;command&#8209;line&nbsp;argument:** `profile` |
| `profile_terse` | Boolean | <p>Profile mode.</p>No default. Produce *terse* profile output; meaningful only in profile mode. For details, see [profile_terse key](#profile_terse-key).<br/><br/>**Equivalent&nbsp;command&#8209;line&nbsp;argument:** `terse` |
| `profile_uri_to_local` | | <p>Profile mode, subset.</p>No default. For profile mode only, an object like `uri_mapping`, for locations of profiles. |
| `property_index` | Boolean | <p>Property index</p>No default. Produce **Property Index** output. For details, see [Redfish docs generator: Property index mode](README_Property_Index.md).<br/><br/>**Equivalent&nbsp;command&#8209;line&nbsp;argument:** `property_index` |
| `property_index_config_out` | | <p>Not used</p>No default. Generate an updated configuration file, with specified file name (property_index mode only).<br/><br/>**Equivalent&nbsp;command&#8209;line&nbsp;argument:** `property_index_config_out` |
| `registry_uri_to_local` |       | <p>Profile mode.</p>No default. For profile mode only, an object like uri_mapping, for locations of registries. |
| `subset`|       | <p>Subset</p>No default. Path to a JSON profile document. Generates **Schema subset** output, with the subset defined in the JSON profile document.<br/><br/>**Equivalent&nbsp;command&#8209;line&nbsp;argument:** `subset` |
| `uri_mapping` | Object | <p>All</p>No default. Partial URL of schema repositories as attributes, and local directory paths as values. |

### combine_multiple_refs key

This setting specifies that multiple objects within a schema, that are defined by reference to the same definition, should have their definitions moved into the Property Details section, with a single-line (row) listing for each object in the main table. combine_multiple_refs is an integer threshold at which this behavior kicks in. If it is absent or 0, no combining occurs. If it is 2 or greater, combining occurs at that number of references to the same object. A setting of 1 does not make sense and should be prevented.

The `combine_multiple_refs` key specifies a threshold at which multiple references to the same object within a schema are moved into **Property details** instead of expanded in place. For example, to move an object to **Property details** if it is referred to three or more times:

```json
"combine_multiple_refs": 3,
```

### object_reference_disposition key

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

### payload_dir key

The `payload_dir` key specifies a directory location for JSON payload and Action examples. If relative, this path is relative to the working directory in which the `doc_generator.py` script is run. Within the payload directory, use the following naming scheme for example files:

* &lt;schema_name&gt;-v&lt;major_version&gt;-example.json for JSON payloads
* &lt;schema_name&gt;-v&lt;major_version&gt;-action-&lt;action_name&gt;.json for action examples

### profile_terse key

The `profile_terse` key is meaningful only when a profile document is also specified. When `true`, *terse* output is produced. By default, profile output is verbose and includes all properties regardless of profile requirements. *Terse* output is intended for use by Service developers, including only the subset of properties with profile requirements.

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

| Configuration key | Type | Description | Details |
| :---------------- | :--- | :---------- | :------ |
| `property_description_overrides` | Dictionary | Maps property names to strings to use to replace the descriptions of the named properties. | |
| `property_fulldescription_overrides` | Dictionary | Just like `property_description_overrides`. These replacements are *full* in that any additional information the `doc_generator.py` normally appends, like a reference to the definition of the property in another schema, is omitted. | |
| `schema_link_replacements` | Dictionary | Maps URIs of schema references to a structure that specifies either the full or partial match type and replacement URIs. Use to substitute a link to documentation where a link to a specific schema would otherwise appear in the documentation. | [schema_link_replacements key](#schema-link-replacements-key) |
| `schema_supplement` | Dictionary | Maps schema names to a dictionary of structured content, including introductory text and schema-specific text replacements. | [schema_supplement key](#schema-supplement-key) |
| `units_translation` | Dictionary | Maps units as they appear in Redfish schemas to units as you want them to appear in the documentation. | |

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
         "YetAnotherPropertyName": "a string, plain text or markdown. This string will also eliminate any additional data the docs generator would normally append to the description."
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
<p>When you run run the docs generator in <b>property index mode</b>:</p>
<ul>
   <li>Only a few of <code>doc_generator.py</code> arguments apply.</li>
   <li>The <a href="#configuration">configuration file</a> takes a different form than the one used for the other output modes.</li>
</ul>

See [Redfish docs generator: Property index configuration](README_Property_Index.md).

## Boilerplate intro supplementary file

The boilerplate intro file is a Markdown or HTML that contains supplementary content to place in the output before the generated documentation. Can include an <code>[add_toc]</code> directive that specifies location for the table of contents.

For an example boilerplate intro file, see <a href="sample_inputs/standard_html/intro.md"><code>intro.md</code></a>.

## Boilerplate postscript supplementary file

The boilerplate postscript file is a Markdown or HTML that contains supplementary content to place in the output after the generated documentation. 

For an example boilerplate postscript file, see <a href="sample_inputs/standard_html/postscript.md"><code>postscript.md</code></a>.

## Redfish docs generator examples

Several files in the `sample_inputs` directory provide examples of configuration files that you can use to produce different types of documentation. The following examples show some command&#8209;line invocations.

These examples assume that you have a clone of the DMTF/Redfish repo and the DMTF/Redfish-Tools repo in the same parent directory, and that your working directory is the Redfish clone, so that the schemas are in `./json-schema` and `doc_generator.py` is at `../Redfish-Tools/doc-generator/doc_generator.py` relative to your current working directory.

> **Note:** The configuration files reference other files in this directory.

* [Standard HTML](#standard-html)
* [Standard HTML with normative descriptions](#standard-html-with-normative-descriptions)
* [Profile index Markdown in terse mode](#profile-index-markdown-in-terse-mode)
* [Subset HTML](#subset-html)
* [Property index HTML](#property-index-html)
* [CSV](#csv)

### Standard HTML

```bash
% python ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/standard_html/config.json
```

Note that the `object_reference_disposition` in this config file identifies specific behavior for the `Redundancy` resource and for `PCIeInterface`, defined in `PCIeDevice`.

### Standard HTML with normative descriptions

```bash
% python ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/standard_html/config_normative.json
```

### Profile index Markdown in terse mode

```bash
% python ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/profile_mode/config.json
```

Configuration file references the profile `OCPBasicServer.v1_0_0.json`, which in turn references `OCPManagedDevice.v1_0_0.json`.

### Subset HTML

```bash
% python ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/subset/config.json
```

Configuration file references the profile `OCPBasicServer.v1_0_0.json`, which in turn references `OCPManagedDevice.v1_0_0.json`.

### Property index HTML

```bash
% python ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/property_index/config.json
```

> **Note:** The Base Configuration file for property index output includes some elements that are specific to that mode: `description_overrides`.

### CSV

```bash
% python ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/csv/config.json
```
