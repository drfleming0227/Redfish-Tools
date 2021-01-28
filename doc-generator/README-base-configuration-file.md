[![Build Status](https://travis-ci.com/DMTF/Redfish-Tools.svg?branch=master)](https://travis-ci.com/github/DMTF/Redfish-Tools)
<p align="center">
  <img src="http://redfish.dmtf.org/sites/all/themes/dmtf2015/images/dmtf-redfish-logo.png" alt="DMTF Redfish" width=180>

# Redfish doc generator: Base configuration file

The base configuration file is a JSON file that configures the generated documentation and can include pointers to the <a href="README-content-supplement-configuration-file.md" title="README-content-supplement-configuration-file.md">content supplement configuration file</a> and the [boilerplate intro](README-supplementary-files.md#boilerplate-intro-file "README-supplementary-files.md#boilerplate-intro-file") and [boilerplate postscript](README-supplementary-files.md#boilerplate-postscript-file "README-supplementary-files.md#boilerplate-postscript-file") supplementary content files.

The names of some configuration keys differ from their command&#8209;line argument equivalents. Unless otherwise noted, the configuration key has the same meaning as its command&#8209;line argument equivalent. The `uri_mapping` configuration key is required but all other configuration keys are optional.

The clauses briefly describes each key and the output modes that support the key:

* [actions_in_property_table key](#actions_in_property_table-key)
* [add_toc key](#add_toc-key)
* [boilerplate_intro key](#boilerplate_intro-key)
* [boilerplate_postscript key](#boilerplate_postscript-key)
* [combine_multiple_refs key](#combine_multiple_refs-key)
* [content_supplement key](#content_supplement-key)
* [description_overrides key](#description_overrides-key)
* [escape_chars key](#escape_chars-key)
* [excluded_annotations key](#excluded_annotations-key)
* [excluded_pattern_properties key](#excluded_pattern_properties-key)
* [excluded_properties key](#excluded_properties-key)
* [excluded_schemas key](#excluded_schemas-key)
* [format key](#format-key)
* [html_title key](#html_title-key)
* [import_from key](#import_from-key)
* [locale key](#locale-key)
* [normative key](#normative-key)
* [object_reference_disposition key](#object_reference_disposition-key)
* [omit_version_in_headers key](#omit_version_in_headers-key)
* [outfile key](#outfile-key)
* [payload_dir key](#payload_dir-key)
* [profile_doc key](#profile_doc-key)
* [profile_terse key](#profile_terse-key)
* [profile_uri_to_local key](#profile_uri_to_local-key)
* [property_index key](#property_index-key)
* [property_index_config_out key](#property_index_config_out-key)
* [registry_uri_to_local key](#registry_uri_to_local-key)
* [subset key](#subset-key)
* [uri_mapping key](#uri_mapping-key)

## actions_in_property_table key

**Output modes:** [Subset](README.md#subset-mode)

Boolean. Value is:

<ul>
   <li><code>true</code>. (Default) Include <code>Actions</code> in property tables. </li>
   <li><code>false</code>. Exclude <code>Actions</code> from property tables. </li>
</ul>

## add_toc key

**Output modes:** [Standard mode](README.md#standard-mode "README.md#standard-mode"), [Standard normative mode](README.md#standard-normative-mode "README.md#standard-normative-mode")

Boolean. By default, the table of contents (TOC) appears at the top of the HTML output. If the <code>[add_toc]</code> directive appears anywhere in the boilerplate intro or boilerplate postscript file, <code>add_toc</code> key is <code>true</code> by default.

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

## boilerplate_intro key

**Output modes:** [Profile mode](README.md#profile-mode "README.md#profile-mode"), [Standard mode](README.md#standard-mode "README.md#standard-mode"), [Standard normative mode](README.md#standard-normative-mode "README.md#standard-normative-mode"), [Subset mode](README.md#subset-mode "README.md#subset-mode")

String. No default. Location of the HTML or Markdown file that contains content to appear at the beginning of the document before the generated schema documentation. If a relative path, should be relative to the location of the configuration file.

## boilerplate_postscript key

**Output modes:** [Standard mode](README.md#standard-mode "README.md#standard-mode"), [Standard normative mode](README.md#standard-normative-mode "README.md#standard-normative-mode")

String. No default. Location of the HTML or Markdown file that contains content to appear at the end of the document after the generated schema documentation. If a relative path, should be relative to the location of the configuration file.

## combine_multiple_refs key

**Output modes:** [Standard mode](README.md#standard-mode "README.md#standard-mode"), [Standard normative mode](README.md#standard-normative-mode "README.md#standard-normative-mode")

Integer. No default. Threshold at which multiple references to the same object within a schema are moved into <b>Property details</b> instead of expanded in place.<br /><br />For details, see <a href="#combine_multiple_refs-key">combine_multiple_refs key</a>.

This setting specifies that multiple objects within a schema, that are defined by reference to the same definition, should have their definitions moved into the Property Details section, with a single-line (row) listing for each object in the main table. combine_multiple_refs is an integer threshold at which this behavior kicks in. If it is absent or 0, no combining occurs. If it is 2 or greater, combining occurs at that number of references to the same object. A setting of 1 does not make sense and should be prevented.

The `combine_multiple_refs` key specifies a threshold at which multiple references to the same object within a schema are moved into **Property details** instead of expanded in place. For example, to move an object to **Property details** if it is referred to three or more times:

```json
"combine_multiple_refs": 3,
```

## content_supplement key

**Output modes:** [Profile mode](README.md#profile-mode "README.md#profile-mode"), [Standard](README.md#standard-mode), [Standard normative mode](README.md#standard-normative-mode "README.md#standard-normative-mode"), [Subset](README.md#subset-mode)

String. No default. Location of a JSON-formatted content supplement file, which specifies content substitutions to be made within the generated schema documentation. If a relative path, must be relative to the location of the configuration file.

## description_overrides key

**Output modes:** [Property index mode](README.md#property-index-mode "README.md#property-index-mode")

String. ??

## escape_chars key

**Output modes:** ??

??. No default. Characters to escape in generated Markdown. For example, use <code>--escape=@</code> if your Markdown processor converts embedded <code>@</code> characters to <code>mailto</code> links.

<b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b> <code>escape</code>

## excluded_annotations key

**Output modes:** [CSV format](README.md#csv-format "README.md#csv-format"), [Profile mode](README.md#profile-mode "README.md#profile-mode"), [Standard](README.md#standard-mode), [Standard normative mode](README.md#standard-normative-mode "README.md#standard-normative-mode"), [Subset](README.md#subset-mode)

Array of strings. No default. List of annotation names to exclude.

Wildcard match is supported for strings that begin with <code>\*</code>.

## excluded_pattern_properties key

 **Output modes:** [CSV format](README.md#csv-format "README.md#csv-format"), [Profile mode](README.md#profile-mode "README.md#profile-mode"), [Standard](README.md#standard-mode), [Standard normative mode](README.md#standard-normative-mode "README.md#standard-normative-mode"), [Subset](README.md#subset-mode)

   ??. No default. List of pattern properties to exclude from output.<br /><br />In JSON, you must escape back slashes (<code>"\"</code> becomes <code>"\\"</code>).

## excluded_properties key

**Output modes:** [CSV format](README.md#csv-format "README.md#csv-format"), [Profile mode](README.md#profile-mode "README.md#profile-mode"), [Standard](README.md#standard-mode), [Standard normative mode](README.md#standard-normative-mode "README.md#standard-normative-mode"), [Subset](README.md#subset-mode)

  Array of strings. No default. List of property names to exclude. Wildcard match is supported for strings that begin with <code>*</code>. For example, <code>"*odata.count"</code> matches <code>"Members\@odata.count"</code> and others.

## excluded_schemas key

 **Output modes:** [CSV format](README.md#csv-format "README.md#csv-format"), [Profile mode](README.md#profile-mode "README.md#profile-mode"), [Standard](README.md#standard-mode), [Standard normative mode](README.md#standard-normative-mode "README.md#standard-normative-mode"), [Subset](README.md#subset-mode)

   Array of strings. No default. List of schemas, by name, to exclude from output.

## format key

**Output modes:** [CSV format](README.md#csv-format "README.md#csv-format"), [Profile mode](README.md#profile-mode "README.md#profile-mode"), [Standard](README.md#standard-mode), [Standard normative mode](README.md#standard-normative-mode "README.md#standard-normative-mode"), [Subset](README.md#subset-mode)

&nbsp;? Output format. Value is <code>markdown</code>, <code>slate</code>, <code>html</code>, or <code>csv</code>.

  **Equivalent&nbsp;command&#8209;line&nbsp;argument:** <code>format</code>

## html_title key

**Output modes:** [Standard](README.md#standard-mode), [Standard normative mode](README.md#standard-normative-mode "README.md#standard-normative-mode"), [Subset](README.md#subset-mode)

  String. No default. HTML <code>title</code> element in HTML output.

## import_from key

**Output modes:** [Standard](README.md#standard-mode), [Standard normative mode](README.md#standard-normative-mode "README.md#standard-normative-mode"), [Subset](README.md#subset-mode)

  String. File name or directory that contains the JSON schemas to process. Wild cards are acceptable. Default: <code>json-schema</code>.

<b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b>&nbsp;<code>import_from</code>

## locale key

**Output modes:** 

  No default. Case-sensitive locale code for localized output. Localization of strings supplied by the doc generator uses <a href="https://www.gnu.org/software/gettext/" title="https://www.gnu.org/software/gettext/"><code>gettext</code></a>. Locale files are in the <code>locale</code> directory in the <code>doc_generator</code> root. Translated descriptions and annotations may be supplied in localized JSON Schema files.

## normative key

**Output modes:** [Standard normative mode](README.md#standard-normative-mode "README.md#standard-normative-mode")

&nbsp;? No default. Produce normative (developer-focused) output.

## object_reference_disposition key

**Output modes:** [Standard](README.md#standard-mode), [Standard normative mode](README.md#standard-normative-mode "README.md#standard-normative-mode")

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

## omit_version_in_headers key

**Output modes:** 

 Boolean. Not used.

   <p>No default.</p>
   <p>Value is:</p>
   <ul>
      <li><code>true</code>. Exclude schema versions from clause headers.</li>
      <li><code>false</code>. Include schema versions in clause headers.</li>
   </ul>

## outfile key

**Output modes:** [CSV format](README.md#csv-format "README.md#csv-format"), [Profile mode](README.md#profile-mode "README.md#profile-mode"), [Property index mode](README.md#property-index-mode "README.md#property-index-mode"), [Standard](README.md#standard-mode), [Standard normative mode](README.md#standard-normative-mode "README.md#standard-normative-mode"), [Subset](README.md#subset-mode)

 &nbsp;? No default. Output file (default depends on output format: <code>output.md</code> for Markdown, <code>index.html</code> for HTML, <code>output.csv</code> for CSV.

 <b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b> <code>out</code>

## payload_dir key

**Output modes:** [Standard](README.md#standard-mode), [Standard normative mode](README.md#standard-normative-mode "README.md#standard-normative-mode")

 &nbsp;? No default. Directory location for JSON payload and Action examples. Optional.<br /><br />For details, see <a href="#payload_dir-key">payload_dir key</a>.

   The `payload_dir` key specifies a directory location for JSON payload and Action examples. If relative, this path is relative to the working directory in which the `doc_generator.py` script is run. Within the payload directory, use the following naming scheme for example files:

   * &lt;schema_name&gt;-v&lt;major_version&gt;-example.json for JSON payloads
   * &lt;schema_name&gt;-v&lt;major_version&gt;-action-&lt;action_name&gt;.json for action examples

 <b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b>&nbsp;<code>payload_dir</code>

## profile_doc key

**Output modes:** [Profile mode](README.md#profile-mode "README.md#profile-mode")

 &nbsp;? No default. Path to a JSON profile document, for profile output.

 <b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b> <code>profile</code>

## profile_terse key

**Output modes:** [Profile mode](README.md#profile-mode "README.md#profile-mode")

 Boolean. No default. Produce <i>terse</i> profile output; meaningful only in profile mode. For details, see <a href="#profile_terse-key">profile_terse key</a>.

   The `profile_terse` key is meaningful only when a profile document is also specified. When `true`, *terse* output is produced. By default, profile output is verbose and includes all properties regardless of profile requirements. *Terse* output is intended for use by Service developers, including only the subset of properties with profile requirements.

 <b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b> <code>terse</code>

## profile_uri_to_local key

**Output modes:** [Profile mode](README.md#profile-mode "README.md#profile-mode"), [Subset](README.md#subset-mode)

&nbsp;? No default. For profile mode only, an object like <code>uri_mapping</code>, for locations of profiles.

## property_index key

**Output modes:** [Property index mode](README.md#property-index-mode "README.md#property-index-mode")

Boolean. No default. Produce <b>Property Index</b> output. For details, see <a href="README-property-index-mode.md">Redfish doc generator: Property index mode</a>.

<b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b> <code>property_index</code>

## property_index_config_out key

**Output modes:** 

&nbsp;? Not used. No default. Generate an updated configuration file, with specified file name (property_index mode only).

<b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b> <code>property_index_config_out</code>

## registry_uri_to_local key

**Output modes:** [Profile mode](README.md#profile-mode "README.md#profile-mode")

&nbsp;? No default. For profile mode only, an object like <code>uri_mapping</code>, for locations of registries.

## subset key

**Output modes:** [Subset](README.md#subset-mode)

&nbsp;? No default. Path to a JSON profile document. Generates <b>Schema subset</b> output, with the subset defined in the JSON profile document.

<b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b> <code>subset</code>

## uri_mapping key

**Output modes:** [CSV format](README.md#csv-format "README.md#csv-format"), [Profile mode](README.md#profile-mode "README.md#profile-mode"), [Property index mode](README.md#property-index-mode "README.md#property-index-mode"), [Standard](README.md#standard-mode), [Standard normative mode](README.md#standard-normative-mode "README.md#standard-normative-mode"), [Subset](README.md#subset-mode)

Object. No default. Partial URL of schema repositories as attributes, and local directory paths as values.

## Subset configuration file

Used in <b>subset mode</b> to generate <b>Schema subset</b> output, with the subset defined in the JSON profile document.

```json
{
   "version": "The version string is optional. It may have (future?) meaning in property index mode.",
   "description": "Redfish doc generator Example: config file for output of subset documentation in HTML format.",
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

See [Redfish doc generator: Property index configuration](README-property-index-mode.md).