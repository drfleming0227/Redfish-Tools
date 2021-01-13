# Redfish docs generator v3 changes

The Redfish docs generator v3 introduces changes to the inputs the tool accepts. These changes are not backward compatible so if you don't need v3 or later changes and you want to run the tool against an existing set of configuration files, use the latest [Redfish docs generator v2 release](https://github.com/DMTF/Redfish-Tools/releases/tag/doc_gen_v2.0.0 "https://github.com/DMTF/Redfish-Tools/releases/tag/doc_gen_v2.0.0").

This document describes the changes and how to update your configuration files.

* [Configuration file changes](#configuration-file-changes)
* [Supplemental material changes](#supplemental-material-changes)
* [Fields removed from the base configuration](#fields-removed-from-the-base-configuration)
* [Fields renamed in the base configuration](#fields-renamed-in-the-base-configuration)
* [Content supplement JSON file](
#content-supplement-json-file)

## Configuration file changes

The Redfish docs generator v3 takes configuration input from:

* The command line
* A configuration file. The configuration file can embed these files:

		* (Optional) Boilerplate intro document. "boilerplate_intro &mdash; "./intro.md",
        * (Optional) Boilerplate postscript document. "boilerplate_postscript &mdash; "./postscript.md",
		* Schema supplement file. "content_supplement &mdash; "./content_supplement.json"
		* (Profile and subset modes only) Mode-specific configuration file

| File type              | Example                   | Format           | Purpose                                                       |
| :--------------------- | :------------------------ | :--------------- | :------------------------------------------------------------ |
| Configuration          | `config.json`             | JSON             | Top-level configuration, including all command-line options. Also specifies the locations of other configuration files. |
| Boilerplate intro      | `intro.md`                | Markdown or HTML | Content to place in the output verbatim before the generated documentation. Can include an `[add_toc]` directive that specifies location for the table of contents. |
| Boilerplate postscript | `postscript.md`           | Markdown or HTML | Content to place in the output verbatim after the generated documentation. Can include an `[add_toc]` directive that specifies location for the table of contents. |
| Content supplement     | `content_supplement.json` | JSON             | Text replacements and additions. Includes text overrides for property descriptions, units translation (replacements for unit abbreviations), schema-specific intros, postscripts, and property description substitutions. |
| subset doc             |                           | JSON             | Subset profile, unchanged for v3. _Link to spec for this?_         |

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
