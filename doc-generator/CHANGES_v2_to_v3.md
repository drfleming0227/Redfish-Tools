# Redfish docs generator v3 changes

The Redfish docs generator v3 changes the inputs that the tool accepts.

> **Note:** These changes are not backward compatible so if you want to run the tool against an existing set of configuration files and you do not need v3 or later changes, use the latest [Redfish docs generator v2 release](https://github.com/DMTF/Redfish-Tools/releases/tag/doc_gen_v2.0.0 "https://github.com/DMTF/Redfish-Tools/releases/tag/doc_gen_v2.0.0").

## Contents

This document describes the changes and how to update your configuration files.

* [Configuration file changes](#configuration-file-changes)
* [Supplemental material changes](#supplemental-material-changes)
* [Fields removed from the base configuration](#fields-removed-from-the-base-configuration)
* [Fields renamed in the base configuration](#fields-renamed-in-the-base-configuration)
* [Content supplement JSON file](
#content-supplement-json-file)

## Configuration file changes

The Redfish docs generator v3 takes configuration input from the command line and the base configuration file. The base configuration file can include pointers to other files.

<!-- 		* (Optional) Boilerplate intro document. "boilerplate_intro &mdash; "./intro.md",
        * (Optional) Boilerplate postscript document. "boilerplate_postscript &mdash; "./postscript.md",
		* Schema supplement file. "content_supplement &mdash; "./content_supplement.json"
		* (Profile and subset modes only) Mode-specific configuration file -->

<table width="100%">
  <tbody>
    <tr>
      <th align="left" valign="top" colspan="2">File type</th>
      <th align="left" valign="top">Example</th>
      <th align="left" valign="top">Format</th>
      <th align="left" valign="top">Description</th>
    </tr>
    <tr>
      <td align="left" valign="top" colspan="2"><a href="doc-generator/README_config_files.md#base-configuration-file">Base&nbsp;configuration</a></td>
      <td align="left" valign="top"><a href="sample_inputs/standard_html/config.json"><code>config.json</code></a></td>
      <td align="left" valign="top">JSON</td>
      <td align="left" valign="top">Top-level configuration file, including all command-line options. Also specifies the locations of the following configuration files.</td>
    </tr>
    <tr>
      <td />
      <td align="left" valign="top">Boilerplate intro</td>
      <td align="left" valign="top"><a href="sample_inputs/standard_html/intro.md"><code>intro.md</code></a></td>
      <td align="left" valign="top">Markdown or HTML</td>
      <td align="left" valign="top">Content to place in the output verbatim before the generated documentation. Can include an `[add_toc]` directive that specifies location for the table of contents.</td>
    </tr>
    <tr>
      <td />
      <td align="left" valign="top">Boilerplate&nbsp;postscript</td>
      <td align="left" valign="top"><a href="sample_inputs/standard_html/postscript.md"><code>postscript.md</code></a></td>
      <td align="left" valign="top">Markdown or HTML</td>
      <td align="left" valign="top">Content to place in the output verbatim after the generated documentation. Can include an <code>[add_toc]</code> directive that specifies location for the table of contents.</td>
    </tr>
    <tr>
      <td />
      <td align="left" valign="top"><a href="doc-generator/README_config_files.md#content-supplement-configuration-file">Content supplement</a></td>
      <td align="left" valign="top"><a href="sample_inputs/standard_html/content_supplement.json"><code>content_supplement.json</code></a></td>
      <td align="left" valign="top">JSON</td>
      <td align="left" valign="top">Text replacements and additions. Includes text overrides for property descriptions, units translation (replacements for unit abbreviations), schema-specific intros, postscripts, and property description substitutions.</td>
    </tr>
    <tr>
      <td />
      <td align="left" valign="top">Subset document</td>
      <td align="left" valign="top"><a href="sample_inputs/subset/config.json"><code>config.json</code></a></td>
      <td align="left" valign="top">JSON</td>
      <td align="left" valign="top">Subset profile, unchanged for v3. _Link to spec for this?_</td>
    </tr>
  </tbody>
</table>

## Supplemental material changes

Features that previously were specified within the *Supplemental Material* Markdown document are all available elsewhere:

| Feature              | Description                                                       |
| :------------------- | :---------------------------------------------------------------- |
| Introduction | Replace with separate boilerplate intro file, file location specified in `config.json` as `boilerplate_intro`. Format is unchanged. |
| Postscript | Replace with separate boilerplate intro file, file location specified in `config.json` as `boilerplate_postscript`. Format is unchanged. |
| Keyword configuration | Specify individual fields in `config.json`: `omit_version_in_headers`, `add_toc`, `actions_in_property_table`, and `suppress_version_history`. |
| Description overrides | `property_description_overrides` in content supplement (in JSON syntax). |
| FullDescription Overrides | `property_fulldescription_overrides` in content supplement (in JSON syntax)
| Schema supplement | `schema_supplement` in content supplement (in JSON syntax). No longer supports JSON payloads (use a `payload_dir` instead). |
| Schema documentation | `schema_link_replacements` in content supplement (in JSON syntax). |

The `config.json` is your base configuration file, specified with the `--config` command-line argument.

The following features have had analogs in the base `config.json` for some time, and now can only be specified in that file:

| Feature                    | Configuration key              |
| :------------------------- | :----------------------------- |
| Excluded properties        | `excluded_properties`          |
| Excluded annotations       | `excluded_annotations`         |
| Excluded schemas           | `excluded_schemas`             |
| Excluded patternProperties | `excluded_pattern_properties`  |
| Schema URI mapping         | `uri_mapping`                  |
| Profile URI mapping        | `profile_uri_to_local`         |
| Registry URI mapping       | `registry_uri_to_local`        |

The `units_translation` field replaces the **Units Translation** table, which has been moved from `config.json` to the content supplement JSON file.

| Feature                    | Configuration key              |
| :------------------------- | :----------------------------- |
| Units translation | `units_translation` in content supplement |

## Fields removed from the base configuration

These fields have been moved from the base `config.json` into the content supplement:

* `property_description_overrides`
* `property_fulldescription_overrides`
* `units_translation`

## Fields renamed in the base configuration

These *Property Index* mode fields that are specified in `config.json` have been renamed:

| Old name               | New name                | Notes                                         |
| :--------------------- | :---------------------- | :-------------------------------------------- |
| `ExcludedProperties`   | `excluded_properties`   | As in other modes.                            |
| `DescriptionOverrides` | `description_overrides` | Distinct from the `property_description_overrides` in the content supplement for other modes, and is provided in the base configuration file rather than the content supplement. |

## Content supplement JSON file

The content supplement contains text replacements and insertions:

| Field                      | Description                     |
| :------------------------- | :------------------------------ |
| `units_translation` | Replacements for the units abbreviations used in the schema files. |
| `schema_supplement` | Schema-specific intros, postscripts, and property description overrides. | 
| `schema_link_replacements` | Mapping of URIs found in schemas to URIs to substitute. Used to replace links to external refs in documentation. | 
| `property_description_overrides` | Replacements for individual property descriptions, by property name. | 
| `property_fulldescription_overrides` | Replacements for individual property descriptions, by property name. These overrides also eliminate any auto-generated explanations, like references to the definition of a property in another schema. | 
