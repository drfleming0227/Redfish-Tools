# Redfish doc generator v3 changes

The Redfish doc generator v3 changes the inputs that the tool accepts.

> **Note:** These changes are not backward compatible so if you want to run the tool against an existing set of configuration files and you do not need v3 or later changes, use [Redfish-Tools doc generator v2](https://github.com/DMTF/Redfish-Tools/releases/tag/doc_gen_v2.0.0 "https://github.com/DMTF/Redfish-Tools/releases/tag/doc_gen_v2.0.0").

The doc generator v3 configures the generated documentation by using command-line input and configuration key values from the base configuration file. The base configuration file can include pointers to other configuration files and supplementary HTML or Markdown files.

The files of interest are:

**Configuration files:**

* [Base configuration file](#base-configuration-file-changes)
* [Content supplement configuration file](#content-supplement-configuration-file-changes)
* [Subset configuration file](#subset-configuration-file-changes)

**Supplementary HTML or Markdown files:**

* [Boilerplate intro](#boilerplate-intro-file-changes)
* [Boilerplate postscript](#boilerplate-postscript-file-changes)

This document describes which files have been changed or added, and how to update your configuration.

## Base configuration file changes

The <a href="README_config_files.md#base-configuration-file">base&nbsp;configuration file</a> is a JSON configuration file that includes all command-line options and that can provide links to the following configuration files and supplementary Markdown files:

<ul>
  <li>Boilerplate intro file</li>
  <li>Boilerplate postscript file</li>
  <li>Content supplement configuration file</li>
  <li>(Profile and subset modes only) Subset configuration file</li>
</ul>

These fields have been moved from the base `config.json` into the [content supplement configuration file](#content-supplement-configuration-file-changes):

* `property_description_overrides`
* `property_fulldescription_overrides`
* `units_translation`

These *property index* mode fields that are specified in `config.json` have been renamed:

| Old name               | New name                | Notes                                         |
| :--------------------- | :---------------------- | :-------------------------------------------- |
| `ExcludedProperties`   | `excluded_properties`   | As in other modes.                            |
| `DescriptionOverrides` | `description_overrides` | Distinct from the `property_description_overrides` in the content supplement for other modes, and is provided in the base configuration file rather than the content supplement. |

For an example of the base configuration file, see <a href="sample_inputs/standard_html/config.json"><code>config.json</code></a>.

## Supplemental material changes

Features that previously were specified within the *Supplemental Material* Markdown document are available elsewhere:

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

## Content supplement configuration file changes

The <a href="README_config_files.md#content-supplement-configuration-file">content supplement configuration file</a> is a JSON file that contains text replacements and additions to apply to the generated schema documentation. It includes text overrides for property descriptions, replacements for unit abbreviations, and schema-specific content including introductions, postscripts, and property description substitutions.

| Configuration key | Type | Description | Change    |
| :---------------- | :--- | :---------- | :-------- |
| `property_description_overrides` | Dictionary | Maps property names to strings to use to replace the descriptions of the named properties. | Moved from base configuration file. |
| `property_fulldescription_overrides` | Dictionary | Just like `property_description_overrides`. These replacements are *full* in that any additional information the `doc_generator.py` normally appends, like a reference to the definition of the property in another schema, is omitted. | Moved from base configuration file. |
| `schema_link_replacements` | Dictionary | Maps URIs of schema references to a structure that specifies either the full or partial match type and replacement URIs. Use to substitute a link to documentation where a link to a specific schema would otherwise appear in the documentation. | [schema_link_replacements key](README_config_files.md/#schema-link-replacements-key) | |
| `schema_supplement` | Dictionary | Maps schema names to a dictionary of structured content, including introductory text and schema-specific text replacements. | [schema_supplement key](README_config_files.md/#schema-supplement-key) | |
| `units_translation` | Dictionary | Maps units as they appear in Redfish schemas to units as you want them to appear in the documentation. | Moved from base configuration file. |

For an example of the content supplement configuration file, see <a href="sample_inputs/standard_html/content_supplement.json"><code>content_supplement.json</code></a>.

## Subset configuration file changes

The subset configuration file is a JSON file that defines the subset profile. 
      
This file is unchanged for v3. _Link to spec for this?_

For an example subset configuration file, see <a href="sample_inputs/subset/config.json"><code>config.json</code></a>.

## Boilerplate intro file changes

The boilerplate intro file is a Markdown or HTML that contains the content to place in the output before the generated documentation. Can include an <code>[add_toc]</code> directive that specifies location for the table of contents.

For an example boilerplate intro file, see <a href="sample_inputs/standard_html/intro.md"><code>intro.md</code></a>.

## Boilerplate postscript file changes

The boilerplate postscript file is a Markdown or HTML that contains the content to place in the output after the generated documentation. 

For an example boilerplate postscript file, see <a href="sample_inputs/standard_html/postscript.md"><code>postscript.md</code></a>.
