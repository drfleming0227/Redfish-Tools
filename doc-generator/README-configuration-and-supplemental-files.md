[![Build Status](https://travis-ci.com/DMTF/Redfish-Tools.svg?branch=master)](https://travis-ci.com/github/DMTF/Redfish-Tools)
<p align="center">
  <img src="http://redfish.dmtf.org/sites/all/themes/dmtf2015/images/dmtf-redfish-logo.png" alt="DMTF Redfish" width=180>

# Redfish doc generator: Configuration and supplemental files

Copyright 2016-2021 Distributed Management Task Force, Inc. All rights reserved.

To configure the generated documentation, you specify configuration keys in the base configuration file and command-line arguments.

If you specify a configuration option in more than one way, command-line arguments take precedence over configuration keys.

The doc generator reads configuration keys from the [base configuration file](#base-configuration-file). if the base configuration file includes a pointer to the [content supplement configuration file](#content-supplement-configuration-file), the doc generator also reads configuration keys from it. 

Additionally, if the base configuration file includes pointers to the <a href="#boilerplate-intro-file">boilerplate&nbsp;intro</a> and <a href="#boilerplate-postscript-file">boilerplate&nbsp;postscript</a> supplemental files, the doc generator includes content from these files in the generated output.

## Contents

* [Base configuration file](#base-configuration-file)
* [Content supplement configuration file](#content-supplement-configuration-file)
* [Boilerplate intro file](#boilerplate-intro-file)
* [Boilerplate postscript file](#boilerplate-postscript-file)

## Base configuration file

The base configuration file is a JSON file that configures the generated documentation and can include pointers to the [content supplement configuration file](#content-supplement-configuration-file) and the [boilerplate intro](README-supplementary-files.md#boilerplate-intro-file "README-supplementary-files.md#boilerplate-intro-file") and [boilerplate postscript](README-supplementary-files.md#boilerplate-postscript-file "README-supplementary-files.md#boilerplate-postscript-file") supplemental files.

Depending on the [output mode](README.md#output-modes "README.md#output-modes"), the configuration keys in the base configuration file can change. Some output modes, such as the property index mode, support additional configuration keys.

The names of some configuration keys differ from their command&#8209;line argument equivalents. Unless otherwise noted, the configuration key has the same meaning as its command&#8209;line argument equivalent. The `uri_mapping` configuration key is required but all other configuration keys are optional.

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

### Contents

* [Example base configuration files](#example-base-configuration-files)
* [actions_in_property_table](#actions_in_property_table)
* [add_toc](#add_toc)
* [boilerplate_intro](#boilerplate_intro)
* [boilerplate_postscript](#boilerplate_postscript)
* [combine_multiple_refs](#combine_multiple_refs)
* [content_supplement](#content_supplement)
* [description_overrides](#description_overrides)
* [escape_chars](#escape_chars)
* [excluded_annotations](#excluded_annotations)
* [excluded_pattern_properties](#excluded_pattern_properties)
* [excluded_properties](#excluded_properties)
* [excluded_schemas](#excluded_schemas)
* [format](#format)
* [html_title](#html_title)
* [import_from](#import_from)
* [locale](#locale)
* [normative](#normative)
* [object_reference_disposition](#object_reference_disposition)
* [omit_version_in_headers](#omit_version_in_headers)
* [outfile](#outfile)
* [payload_dir](#payload_dir)
* [profile_doc](#profile_doc)
* [profile_terse](#profile_terse)
* [profile_uri_to_local](#profile_uri_to_local)
* [property_index](#property_index)
* [property_index_config_out](#property_index_config_out)
* [registry_uri_to_local](#registry_uri_to_local)
* [subset](#subset)
* [uri_mapping](#uri_mapping)
* [Subset configuration file](#subset-configuration-file)
* [Property index configuration file](#property-index-configuration-file)

### Example base configuration files

| Output format or mode | Sample base configuration file | Example command usage |
| :-------------------- | :----------------------------- | :-------------------- |
| CSV format            | [`sample_inputs/csv/config.json`](sample_inputs/csv/config.json) | [CSV format](README-configuration-files.md#csv-format) |
| Profile mode          | [`sample_inputs/profile_mode/config.json`](sample_inputs/profile_mode/config.json) | [Terse profile mode in Markdown format](README-configuration-files.md#terse-profile-mode-in-markdown-format) |
| Property index mode   | [`sample_inputs/property_index/config.json`](sample_inputs/property_index/config.json) | [Property index mode in HTML format](README-configuration-files.md#property-index-mode-in-html-format) |
| Standard mode         | [`sample_inputs/standard_html/config.json`](sample_inputs/standard_html/config.json) | [Standard mode in HTML format](README-configuration-files.md#standard-mode-in-html-format) |
| Standard normative | [`sample_inputs/standard_html/config_normative.json`](sample_inputs/standard_html/config_normative.json) | [Standard normative mode in HTML format](README-configuration-files.md#standard-normative-mode-in-html-format) |
| Schema subset mode   | [`sample_inputs/subset/config.json`](sample_inputs/subset/config.json) | [Schema subset mode in HTML format](README-configuration-files.md#schema-subset-mode-in-html-format) |

<table>
   <thead>
      <tr>
         <th align="left" valign="top">Key</th>
         <th align="left" valign="top">Output modes</th>
         <th align="left" valign="top">Description</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td align="left" valign="top"><code>actions_in_property_table</code></td>
         <td align="left" valign="top"><a href="README.md#schema-subset-mode">Schema subset</a></td>
         <td align="left" valign="top"><p>Boolean</p>
            <p>Value is:</p>
            <ul>
               <li><code>true</code>. (Default) Include <code>Actions</code> in property tables.</li>
               <li><code>false</code>. Exclude <code>Actions</code> from property tables.</li>
            </ul>
         </td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>add_toc</code></td>
         <td align="left" valign="top"><ul><li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard&nbsp;normative</a></li></ul></td>
         <td align="left" valign="top"><p>Boolean</p>
            <p>By default, the table of contents (TOC) appears at the top of the HTML output. If the <code>[add_toc]</code> directive appears anywhere in the boilerplate intro or boilerplate postscript file, <code>add_toc</code> key is <code>true</code> by default.</p>
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
         </td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>boilerplate_intro</code></td>
         <td align="left" valign="top"><ul><li><a href="README.md#profile-mode" title="README.md#profile-mode">Profile mode</a></li><li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard mode</a></li><li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a></li><li><a href="README.md#subset-mode" title="README.md#subset-mode">Subset mode</a></li></ul></td>
         <td align="left" valign="top"><p>String</p>
         <p>No default. Location of the HTML or Markdown file that contains content to appear at the beginning of the document before the generated schema documentation. If a relative path, should be relative to the location of the configuration file.</p></td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>boilerplate_postscript</code></td>
         <td align="left" valign="top"><ul><li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard&nbsp;normative</a></li></ul></td>
         <td align="left" valign="top"><p>String</p><p>No default. Location of the HTML or Markdown file that contains content to appear at the end of the document after the generated schema documentation. If a relative path, should be relative to the location of the configuration file.</p></td>
      </tr>
      <!-- <tr>
         <td align="left" valign="top"><code>combine_multiple_refs</code></td>
         <td align="left" valign="top"><li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a></td>
         <td align="left" valign="top"> Integer</td>
         <td align="left" valign="top">
            <p>No default. Threshold at which multiple references to the same object within a schema are moved into <b>Property details</b> instead of expanded in place.</p>
            <p>For details, see <a href="#combine_multiple_refs-key">combine_multiple_refs key</a>.</p>
            <p> This setting specifies that multiple objects within a schema, that are defined by reference to the same definition, should have their definitions moved into the Property Details section, with a single-line (row) listing for each object in the main table. combine_multiple_refs is an integer threshold at which this behavior kicks in. If it is absent or 0, no combining occurs. If it is 2 or greater, combining occurs at that number of references to the same object. A setting of 1 does not make sense and should be prevented.</p>
            <p>The <code>combine_multiple_refs</code> key specifies a threshold at which multiple references to the same object within a schema are moved into <b>Property details</b> instead of expanded in place. For example, to move an object to <b>Property details</b> if it is referred to three or more times:</p>
            <pre lang="json">"combine_multiple_refs": 3</pre>
         </td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>content_supplement</code></td>
         <td align="left" valign="top"><a href="README.md#profile-mode" title="README.md#profile-mode">Profile mode</a>, <li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a>, <a href="README.md#schema-subset-mode">Schema subset</a></td>
         <td align="left" valign="top">String</td>
         <td align="left" valign="top">No default. Location of a JSON-formatted content supplement file, which specifies content substitutions to be made within the generated schema documentation. If a relative path, must be relative to the location of the configuration file.</td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>description_overrides</code></td>
         <td align="left" valign="top"><a href="README.md#property-index-mode" title="README.md#property-index-mode">Property index mode</a></td>
         <td align="left" valign="top">Object</td>
         <td align="left" valign="top">
            <p>An object keyed by property name, which can specify descriptions that override those in the source schemas.</p>
            <p>You can override descriptions for individual properties. The <code>description_overrides</code> object is keyed by property name. Values are lists, which enable different overrides for the same property in different schemas. Each object in the list can have the following entries:</p> | Key | Value | | :-------------------- | :------------- | | `type` | Property type. | | `schemas` | List of schemas to which this element applies. | | `overrideDescription` | String that replaces the description in the schema. | | `globalOverride` | The `overrideDescription` in this element applies to all instances of the property name that match the `type`. | | `description` | Description in the schema. | | `knownException` | A variant description is expected. | <p>The `description` and `knownException` keys are primarily for user reference. When generating configuration output, the doc generator includes the description and set `knownException` to `false`. The user can edit the resulting output to distinguish expected exceptions from those that need attention. Neither field affects the property index document itself.</p>
            <blockquote><b>Note:</b> Although `description_overrides` has a similar function to `property_description_overrides` in other modes, it has a different structure.</blockquote>
            <p>Some examples:</p>
            <pre lang="json">"EventType": [{
   "overrideDescription": "This indicates the type of an event recorded in this log.",
   "globalOverride": true,
   "type": "string"
}]</pre>
            <p>The combination of `globalOverride` and `overrideDescription` indicates that all instances of the `EventType` property that have type `string` should have their description replaced with `"This indicates the type of an event recorded in this log."`</p>
            <pre lang="json">
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
}]</pre>
            <p>The first two entries in this `FirmwareVersion` example override the description for `FirmwareVersion` with type `string`, in the listed schemas. The third entry identifies another instance of `FirmwareVersion` with another description, which is expected but should not be overridden.</p>
         </td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>escape_chars</code></td>
         <td align="left" valign="top">??</td>
         <td align="left" valign="top">??</td>
         <td align="left" valign="top">
            <p>No default. Characters to escape in generated Markdown. For example, use <code>--escape=@</code> if your Markdown processor converts embedded <code>@</code> characters to <code>mailto</code> links.</p>
            <p><b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b> <code>escape</code></p>
         </td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>excluded_annotations</code></td>
         <td align="left" valign="top"><a href="README.md#csv-formnat" title="README.md#csv-format">CSV format</a>, <a href="README.md#profile-mode" title="README.md#profile-mode">Profile mode</a>, <li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a>, <a href="README.md#schema-subset-mode">Schema subset</a></td>
         <td align="left" valign="top">Array of strings</td>
         <td align="left" valign="top">No default. List of annotation names to exclude. Strings that begin with <code>\*</code> define wildcards.</td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>excluded_pattern_properties</code></td>
         <td align="left" valign="top"><a href="README.md#csv-formnat" title="README.md#csv-format">CSV format</a>, <a href="README.md#profile-mode" title="README.md#profile-mode">Profile mode</a>, <li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a>, <a href="README.md#schema-subset-mode">Schema subset</a></td>
         <td align="left" valign="top">??</td>
         <td align="left" valign="top">No default. List of pattern properties to exclude from output.<br /><br />In JSON, you must escape back slashes (<code>"\"</code> becomes <code>"\\"</code>).</td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>excluded_properties</code></td>
         <td align="left" valign="top"><a href="README.md#csv-formnat" title="README.md#csv-format">CSV format</a>, <a href="README.md#profile-mode" title="README.md#profile-mode">Profile mode</a>, <li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a>, <a href="README.md#schema-subset-mode">Schema subset</a></td>
         <td align="left" valign="top">Array of strings</td>
         <td align="left" valign="top">
            <p>No default. List of property names to exclude from the generated documentation. Strings that begin with <code>*</code> define wildcards. For example, <code>"*odata.count"</code> matches <code>"Members\@odata.count"</code> and others.</p>
            <p>To exclude properties from the output, include them in the `excluded_properties` list. An asterisk (`*`) as the first character in a property acts as a wild card. In the following example, any property name that ends with `"@odata.count"` is omitted:</p>
            <pre lang="json">"excluded_properties": ["description",
   "Id", "@odata.context",
   "@odata.type", "@odata.id",
   "@odata.etag", "*@odata.count"
]</pre>
         </td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>excluded_schemas</code></td>
         <td align="left" valign="top"><a href="README.md#csv-formnat" title="README.md#csv-format">CSV format</a>, <a href="README.md#profile-mode" title="README.md#profile-mode">Profile mode</a>, <li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a>, <a href="README.md#schema-subset-mode">Schema subset</a></td>
         <td align="left" valign="top">Array of strings</td>
         <td align="left" valign="top">No default. List of schemas, by name, to exclude from output.</td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>format</code></td>
         <td align="left" valign="top"><a href="README.md#csv-formnat" title="README.md#csv-format">CSV format</a>, <a href="README.md#profile-mode" title="README.md#profile-mode">Profile mode</a>, <li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a>, <a href="README.md#schema-subset-mode">Schema subset</a></td>
         <td align="left" valign="top">&nbsp;?</td>
         <td align="left" valign="top">
            <p>Output format. Value is <code>markdown</code>, <code>slate</code>, <code>html</code>, or <code>csv</code>.</p>
            <p><b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b> <code>format</code></p>
         </td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>html_title</code></td>
         <td align="left" valign="top"><li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a>, <a href="README.md#schema-subset-mode">Schema subset</a></td>
         <td align="left" valign="top">String</td>
         <td align="left" valign="top">No default. HTML <code>title</code> element in HTML output.</td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>import_from</code></td>
         <td align="left" valign="top"><li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a>, <a href="README.md#schema-subset-mode">Schema subset</a></td>
         <td align="left" valign="top">String</td>
         <td align="left" valign="top">
            <p>File name or directory that contains the JSON schemas to process. Wild cards are acceptable. Default: <code>json-schema</code>.</p>
            <p><b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b>&nbsp;<code>import_from</code></p>
         </td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>locale</code></td>
         <td align="left" valign="top">??</td>
         <td align="left" valign="top">No default. Case-sensitive locale code for localized output. Localization of strings supplied by the doc generator uses <a href="https://www.gnu.org/software/gettext/" title="https://www.gnu.org/software/gettext/"><code>gettext</code></a>. Locale files are in the <code>locale</code> directory in the <code>doc_generator</code> root. Translated descriptions and annotations may be supplied in localized JSON Schema files.</td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>normative</code></td>
         <td align="left" valign="top"><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a></td>
         <td align="left" valign="top">&nbsp;?</td>
         <td align="left" valign="top">No default. Produce normative (developer-focused) output.</td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>object_reference_disposition</code></td>
         <td align="left" valign="top"><li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a></td>
         <td align="left" valign="top">&nbsp;?</td>
         <td align="left" valign="top">
            <p>No default. Data structure that specifies properties that should be moved to the <b>Common Objects</b> clause and/or objects that should be included in-line where they are referenced, to override default behavior. For details, see <a href="#object_reference_disposition-key">object_reference_disposition key</a>.</p>
            <p>The `object_reference_disposition` key specifies a JSON object with either or both these fields:</p>
            <ul>
               <li>`common_object`. List of property names. For example `"Redundancy"`.</li>
               <li>`include`. List of properties by their full path.</li>
            </ul>
            <p>For example:</p>
            <pre lang="json">
"object_reference_disposition": {
   "common_object": ["Redundancy"],
   "include": [
    "http://redfish.dmtf.org/schemas/v1/PCIeDevice.json#/definitions/PCIeInterface"
  ]
}
</pre>
         </td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>omit_version_in_headers</code></td>
         <td align="left" valign="top"></td>
         <td align="left" valign="top">Boolean.</td>
         <td align="left" valign="top">
            <p>Not used.</p>
            <p>No default.</p>
            <p>Value is:</p>
            <ul>
               <li><code>true</code>. Exclude schema versions from clause headers.</li>
               <li><code>false</code>. Include schema versions in clause headers.</li>
            </ul>
         </td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>outfile</code></td>
         <td align="left" valign="top"><a href="README.md#csv-formnat" title="README.md#csv-format">CSV format</a>, <a href="README.md#profile-mode" title="README.md#profile-mode">Profile mode</a>, <a href="README.md#property-index-mode" title="README.md#property-index-mode">Property index mode</a>, <li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a>, <a href="README.md#schema-subset-mode">Schema subset</a> &nbsp;? No default. Output file (default depends on output format: <code>output.md</code> for Markdown, <code>index.html</code> for HTML, <code>output.csv</code> for CSV. <b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b> <code>out</code>
      <tr>
         <td align="left" valign="top"><code>payload_dir</code></td>
         <td align="left" valign="top"><li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a> &nbsp;? No default. Directory location for JSON payload and Action examples. Optional.<br /><br />For details, see <a href="#payload_dir-key">payload_dir key</a>. The `payload_dir` key specifies a directory location for JSON payload and Action examples. If relative, this path is relative to the working directory in which the `doc_generator.py` script is run. Within the payload directory, use the following naming scheme for example files: * &lt;schema_name&gt;-v&lt;major_version&gt;-example.json for JSON payloads * &lt;schema_name&gt;-v&lt;major_version&gt;-action-&lt;action_name&gt;.json for action examples <b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b>&nbsp;<code>payload_dir</code>
      <tr>
         <td align="left" valign="top"><code>profile_doc</code></td>
         <td align="left" valign="top"><a href="README.md#profile-mode" title="README.md#profile-mode">Profile mode</a> &nbsp;? No default. Path to a JSON profile document, for profile output. <b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b> <code>profile</code>
      <tr>
         <td align="left" valign="top"><code>profile_terse</code></td>
         <td align="left" valign="top"><a href="README.md#profile-mode" title="README.md#profile-mode">Profile mode</a> Boolean. No default. Produce <i>terse</i> profile output; meaningful only in profile mode. For details, see <a href="#profile_terse-key">profile_terse key</a>. The `profile_terse` key is meaningful only when a profile document is also specified. When `true`, *terse* output is produced. By default, profile output is verbose and includes all properties regardless of profile requirements. *Terse* output is intended for use by Service developers, including only the subset of properties with profile requirements. <b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b> <code>terse</code>
      <tr>
         <td align="left" valign="top"><code>profile_uri_to_local</code></td>
         <td align="left" valign="top"><a href="README.md#profile-mode" title="README.md#profile-mode">Profile mode</a>, <a href="README.md#schema-subset-mode">Schema subset</a></td>
         <td align="left" valign="top">&nbsp;?</td>
         <td align="left" valign="top">No default. For profile mode only, an object like <code>uri_mapping</code>, for locations of profiles.</td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>property_index</code></td>
         <td align="left" valign="top"><a href="README.md#property-index-mode" title="README.md#property-index-mode">Property index mode</a></td>
         <td align="left" valign="top">Boolean</td>
         <td align="left" valign="top">
            <p>No default. Produces <b>property index mode</b> output.</p>
            <p><b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b> <code>property_index</code></p>
         </td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>property_index_config_out</code></td>
         <td align="left" valign="top"><a href="README.md#property-index-mode" title="README.md#property-index-mode">Property index mode</a></td>
         <td align="left" valign="top">String</td>
         <td align="left" valign="top">
            <p>No default. Generates an updated configuration file with the specified file name. The doc generator adds entries for any properties where the property name appears with more than one type or description to extend the input configuration.</p>
            <p>If you specify `globalOverride` for a property name or property name and type, no data is added for matching instances.</p>
            <p>All added entries include `"knownException": false`. In addition, if an entry includes `"knownException": true` in the input configuration but the description no longer matches, `knownException` is set to `false`.</p>
            <p>In the previous example, if `FirmwareVersion` in the `PCIeDevice` schema had a different description than the one listed in the example input, it appears in the output with its new description and `"knownException": false`.</p>
            <p><b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b> <code>property_index_config_out</code></p>
         </td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>registry_uri_to_local</code></td>
         <td align="left" valign="top"><a href="README.md#profile-mode" title="README.md#profile-mode">Profile mode</a></td>
         <td align="left" valign="top">&nbsp;?</td>
         <td align="left" valign="top">No default. For profile mode only, an object like <code>uri_mapping</code>, for locations of registries.</td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>subset</code></td>
         <td align="left" valign="top"><a href="README.md#schema-subset-mode">Schema subset</a></td>
         <td align="left" valign="top">&nbsp;?</td>
         <td align="left" valign="top">
            <p>No default. Path to a JSON profile document. Generates <b>Schema subset</b> output, with the subset defined in the JSON profile document.</p>
            <p><b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b> <code>subset</code></p>
         </td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>uri_mapping</code></td>
         <td align="left" valign="top"><a href="README.md#csv-formnat" title="README.md#csv-format">CSV format</a>, <a href="README.md#profile-mode" title="README.md#profile-mode">Profile mode</a>, <a href="README.md#property-index-mode" title="README.md#property-index-mode">Property index mode</a>, <li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a>, <a href="README.md#schema-subset-mode">Schema subset</a></td>
         <td align="left" valign="top">Object</td>
         <td align="left" valign="top">
            <p>No default. Partial URL of schema repositories as attributes, and local directory paths as values.</p>
            <p>This object maps partial URIs, as found in the schemas, to local directories. The partial URI should include the domain part of the URI but can omit the protocol (http:// or https://).</p>
            <pre lang="json">
"uri_mapping": { "redfish.dmtf.org/schemas/v1": "./json-schema" }
</pre>
         </td>
      </tr> -->
   </tbody>
</table>

<!-- ### actions_in_property_table

**Output modes:** <a href="README.md#schema-subset-mode">Schema subset</a>

Boolean. Value is:

<ul>
   <li><code>true</code>. (Default) Include <code>Actions</code> in property tables. </li>
   <li><code>false</code>. Exclude <code>Actions</code> from property tables. </li>
</ul>

### add_toc

**Output modes:** <li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a>

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

### boilerplate_intro

**Output modes:** <a href="README.md#profile-mode" title="README.md#profile-mode">Profile mode</a>, <li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a>, <a href="README.md#subset-mode" title="README.md#subset-mode">Subset mode</a>

String. No default. Location of the HTML or Markdown file that contains content to appear at the beginning of the document before the generated schema documentation. If a relative path, should be relative to the location of the configuration file.

### boilerplate_postscript

**Output modes:** <li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a>

String. No default. Location of the HTML or Markdown file that contains content to appear at the end of the document after the generated schema documentation. If a relative path, should be relative to the location of the configuration file.

### combine_multiple_refs

**Output modes:** <li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a>

Integer. No default. Threshold at which multiple references to the same object within a schema are moved into <b>Property details</b> instead of expanded in place.<br /><br />For details, see <a href="#combine_multiple_refs-key">combine_multiple_refs key</a>.

This setting specifies that multiple objects within a schema, that are defined by reference to the same definition, should have their definitions moved into the Property Details section, with a single-line (row) listing for each object in the main table. combine_multiple_refs is an integer threshold at which this behavior kicks in. If it is absent or 0, no combining occurs. If it is 2 or greater, combining occurs at that number of references to the same object. A setting of 1 does not make sense and should be prevented.

The `combine_multiple_refs` key specifies a threshold at which multiple references to the same object within a schema are moved into **Property details** instead of expanded in place. For example, to move an object to **Property details** if it is referred to three or more times:

```json
"combine_multiple_refs": 3,
```

### content_supplement

**Output modes:** <a href="README.md#profile-mode" title="README.md#profile-mode">Profile mode</a>, <li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a>, <a href="README.md#schema-subset-mode">Schema subset</a>

String. No default. Location of a JSON-formatted content supplement file, which specifies content substitutions to be made within the generated schema documentation. If a relative path, must be relative to the location of the configuration file.

### description_overrides

**Output modes:** <a href="README.md#property-index-mode" title="README.md#property-index-mode">Property index mode</a>

Object. An object keyed by property name, which can specify descriptions that override those in the source schemas.

You can override descriptions for individual properties. The `description_overrides` object is keyed by property name. Values are lists, which enable different overrides for the same property in different schemas. Each object in the list can have the following entries:

| Key                   | Value          |
| :-------------------- | :------------- |
| `type`                | Property type. |
| `schemas`             | List of schemas to which this element applies. |
| `overrideDescription` | String that replaces the description in the schema. |
| `globalOverride`      | The `overrideDescription` in this element applies to all instances of the property name that match the `type`. |
| `description`         | Description in the schema. |
| `knownException`      | A variant description is expected. |

The `description` and `knownException` keys are primarily for user reference. When generating configuration output, the doc generator includes the description and set `knownException` to `false`. The user can edit the resulting output to distinguish expected exceptions from those that need attention. Neither field affects the property index document itself.

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

### escape_chars

**Output modes:** ??

??. No default. Characters to escape in generated Markdown. For example, use <code>--escape=@</code> if your Markdown processor converts embedded <code>@</code> characters to <code>mailto</code> links.

<b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b> <code>escape</code>

### excluded_annotations

**Output modes:** <a href="README.md#csv-formnat" title="README.md#csv-format">CSV format</a>, <a href="README.md#profile-mode" title="README.md#profile-mode">Profile mode</a>, <li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a>, <a href="README.md#schema-subset-mode">Schema subset</a>

Array of strings. No default. List of annotation names to exclude.

Strings that begin with <code>\*</code> define wildcards.

### excluded_pattern_properties

**Output modes:** <a href="README.md#csv-formnat" title="README.md#csv-format">CSV format</a>, <a href="README.md#profile-mode" title="README.md#profile-mode">Profile mode</a>, <li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a>, <a href="README.md#schema-subset-mode">Schema subset</a>

??. No default. List of pattern properties to exclude from output.<br /><br />In JSON, you must escape back slashes (<code>"\"</code> becomes <code>"\\"</code>).

### excluded_properties

**Output modes:** <a href="README.md#csv-formnat" title="README.md#csv-format">CSV format</a>, <a href="README.md#profile-mode" title="README.md#profile-mode">Profile mode</a>, <li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a>, <a href="README.md#schema-subset-mode">Schema subset</a>

Array of strings. No default. List of property names to exclude from the generated documentation. Strings that begin with <code>*</code> define wildcards. For example, <code>"*odata.count"</code> matches <code>"Members\@odata.count"</code> and others.

To exclude properties from the output, include them in the `excluded_properties` list. An asterisk (`*`) as the first character in a property acts as a wild card. In the following example, any property name that ends with `"@odata.count"` is omitted:

```json
"excluded_properties": ["description",
   "Id", "@odata.context",
   "@odata.type", "@odata.id",
   "@odata.etag", "*@odata.count"
]
```

### excluded_schemas

**Output modes:** <a href="README.md#csv-formnat" title="README.md#csv-format">CSV format</a>, <a href="README.md#profile-mode" title="README.md#profile-mode">Profile mode</a>, <li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a>, <a href="README.md#schema-subset-mode">Schema subset</a>

Array of strings. No default. List of schemas, by name, to exclude from output.

### format

**Output modes:** <a href="README.md#csv-formnat" title="README.md#csv-format">CSV format</a>, <a href="README.md#profile-mode" title="README.md#profile-mode">Profile mode</a>, <li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a>, <a href="README.md#schema-subset-mode">Schema subset</a>

&nbsp;? Output format. Value is <code>markdown</code>, <code>slate</code>, <code>html</code>, or <code>csv</code>.

**Equivalent&nbsp;command&#8209;line&nbsp;argument:** <code>format</code>

### html_title

**Output modes:** <li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a>, <a href="README.md#schema-subset-mode">Schema subset</a>

String. No default. HTML <code>title</code> element in HTML output.

### import_from

**Output modes:** <li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a>, <a href="README.md#schema-subset-mode">Schema subset</a>

String. File name or directory that contains the JSON schemas to process. Wild cards are acceptable. Default: <code>json-schema</code>.

<b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b>&nbsp;<code>import_from</code>

### locale

**Output modes:** 

No default. Case-sensitive locale code for localized output. Localization of strings supplied by the doc generator uses <a href="https://www.gnu.org/software/gettext/" title="https://www.gnu.org/software/gettext/"><code>gettext</code></a>. Locale files are in the <code>locale</code> directory in the <code>doc_generator</code> root. Translated descriptions and annotations may be supplied in localized JSON Schema files.

### normative

**Output modes:** <a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a>

&nbsp;? No default. Produce normative (developer-focused) output.

### object_reference_disposition

**Output modes:** <li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a>

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

### omit_version_in_headers

**Output modes:** 

 Boolean. Not used.

   <p>No default.</p>
   <p>Value is:</p>
   <ul>
      <li><code>true</code>. Exclude schema versions from clause headers.</li>
      <li><code>false</code>. Include schema versions in clause headers.</li>
   </ul>

### outfile

**Output modes:** <a href="README.md#csv-formnat" title="README.md#csv-format">CSV format</a>, <a href="README.md#profile-mode" title="README.md#profile-mode">Profile mode</a>, <a href="README.md#property-index-mode" title="README.md#property-index-mode">Property index mode</a>, <li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a>, <a href="README.md#schema-subset-mode">Schema subset</a>

 &nbsp;? No default. Output file (default depends on output format: <code>output.md</code> for Markdown, <code>index.html</code> for HTML, <code>output.csv</code> for CSV.

 <b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b> <code>out</code>

### payload_dir

**Output modes:** <li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a>

 &nbsp;? No default. Directory location for JSON payload and Action examples. Optional.<br /><br />For details, see <a href="#payload_dir-key">payload_dir key</a>.

The `payload_dir` key specifies a directory location for JSON payload and Action examples. If relative, this path is relative to the working directory in which the `doc_generator.py` script is run. Within the payload directory, use the following naming scheme for example files:

* &lt;schema_name&gt;-v&lt;major_version&gt;-example.json for JSON payloads
* &lt;schema_name&gt;-v&lt;major_version&gt;-action-&lt;action_name&gt;.json for action examples

 <b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b>&nbsp;<code>payload_dir</code>

### profile_doc

**Output modes:** <a href="README.md#profile-mode" title="README.md#profile-mode">Profile mode</a>

&nbsp;? No default. Path to a JSON profile document, for profile output.

<b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b> <code>profile</code>

### profile_terse

**Output modes:** <a href="README.md#profile-mode" title="README.md#profile-mode">Profile mode</a>

Boolean. No default. Produce <i>terse</i> profile output; meaningful only in profile mode. For details, see <a href="#profile_terse-key">profile_terse key</a>.

The `profile_terse` key is meaningful only when a profile document is also specified. When `true`, *terse* output is produced. By default, profile output is verbose and includes all properties regardless of profile requirements. *Terse* output is intended for use by Service developers, including only the subset of properties with profile requirements.

<b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b> <code>terse</code>

### profile_uri_to_local

**Output modes:** <a href="README.md#profile-mode" title="README.md#profile-mode">Profile mode</a>, <a href="README.md#schema-subset-mode">Schema subset</a>

&nbsp;? No default. For profile mode only, an object like <code>uri_mapping</code>, for locations of profiles.

### property_index

**Output modes:** <a href="README.md#property-index-mode" title="README.md#property-index-mode">Property index mode</a>

Boolean. No default. Produces <b>property index mode</b> output.

<b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b> <code>property_index</code>

### property_index_config_out

**Output modes:** <a href="README.md#property-index-mode" title="README.md#property-index-mode">Property index mode</a>

String. No default. Generates an updated configuration file with the specified file name. The doc generator adds entries for any properties where the property name appears with more than one type or description to extend the input configuration.

If you specify `globalOverride` for a property name or property name and type, no data is added for matching instances.

All added entries include `"knownException": false`. In addition, if an entry includes `"knownException": true` in the input configuration but the description no longer matches, `knownException` is set to `false`. 

In the previous example, if `FirmwareVersion` in the `PCIeDevice` schema had a different description than the one listed in the example input, it appears in the output with its new description and `"knownException": false`.

<b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b> <code>property_index_config_out</code>

### registry_uri_to_local

**Output modes:** <a href="README.md#profile-mode" title="README.md#profile-mode">Profile mode</a>

&nbsp;? No default. For profile mode only, an object like <code>uri_mapping</code>, for locations of registries.

### subset

**Output modes:** <a href="README.md#schema-subset-mode">Schema subset</a>

&nbsp;? No default. Path to a JSON profile document. Generates <b>Schema subset</b> output, with the subset defined in the JSON profile document.

<b>Equivalent&nbsp;command&#8209;line&nbsp;argument:</b> <code>subset</code>

### uri_mapping

**Output modes:** <a href="README.md#csv-formnat" title="README.md#csv-format">CSV format</a>, <a href="README.md#profile-mode" title="README.md#profile-mode">Profile mode</a>, <a href="README.md#property-index-mode" title="README.md#property-index-mode">Property index mode</a>, <li><a href="README.md#standard-mode" title="README.md#standard-mode">Standard</a></li><a href="README.md#standard-normative-mode" title="README.md#standard-normative-mode">Standard normative mode</a>, <a href="README.md#schema-subset-mode">Schema subset</a>

Object. No default. Partial URL of schema repositories as attributes, and local directory paths as values.

This object maps partial URIs, as found in the schemas, to local directories. The partial URI should include the domain part of the URI but can omit the protocol (http:// or https://).

```json
"uri_mapping": { "redfish.dmtf.org/schemas/v1": "./json-schema" }
``` -->

### Subset configuration file

Used in <b>schema subset mode</b> to generate <b>Schema subset</b> output, with the subset defined in the JSON profile document.

```json
{
   "version": "The version string is optional. It may have (future?) meaning in property index mode.",
   "description": "Redfish doc generator: Example: config file for output of subset documentation in HTML format.",
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

### Property index configuration file

<p>Used in <b>property index mode</b> to generate <b>Property index</b> output, which is an index of property names and descriptions that includes property name, type, schemas where found, and descriptions found.</p>
<p>When you run run the doc generator in <b>property index mode</b>:</p>
<ul>
   <li>Only a few of <code>doc_generator.py</code> arguments apply.</li>
   <li>The <a href="#configuration">configuration file</a> takes a different form than the one used for the other output modes.</li>
</ul>

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

Other properties may be included for the user's reference, and are ignored by the doc generator.

**Base configuration file:** <a href="sample_inputs/property_index/config.json"><code>sample_inputs/property_index/config.json</code></a>

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

Dictionary. Maps property names to strings that replace the descriptions of the named properties.

### property_fulldescription_overrides

Dictionary. Maps property names to strings that replace the descriptions of the named properties. These replacements are *full* in that the doc generator omits any additional information that it normally appends, like a reference to the definition of the property in another schema.

### schema_link_replacements

Dictionary. Maps reference URIs to replacement URIs. The match type is full or partial. Replaces one link with another link. The dictionary structure is:

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

Dictionary. Maps schema names to a dictionary of structured content, including text overrides for property descriptions, replacements for unit abbreviations, schema-specific introductions, property description substitutions, and other supplementary data. All elements in this structure are optional. 

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

Dictionary. Maps Redfish schema units to units as you want them to appear in the documentation.

## Boilerplate intro file

**Sample boilerplate intro file:** <a href="sample_inputs/standard_html/intro.md"><code>intro.md</code></a>

The boilerplate intro file is a Markdown or HTML file that contains supplementary content to include in the output before the generated documentation.

This file can include an <code>[add_toc]</code> directive that specifies location for the table of contents.

## Boilerplate postscript file

**Sample boilerplate postscript file:** <a href="sample_inputs/standard_html/postscript.md"><code>postscript.md</code></a>

The boilerplate postscript file is a Markdown or HTML file that contains supplementary content to include in the output after the generated documentation.

This file can include an <code>[add_toc]</code> directive that specifies location for the table of contents.
