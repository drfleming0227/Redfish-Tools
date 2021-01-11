# Documentation generator v3 changes

The Documentation generator version 3 introduces changes to the inputs the tool accepts. These changes are not backward compatible so if you don't need v3 or later changes and you need to run the tool against an existing set of configuration files, use the latest [Documentation generator v2 release](https://github.com/DMTF/Redfish-Tools/releases/tag/doc_gen_v2.0.0 "https://github.com/DMTF/Redfish-Tools/releases/tag/doc_gen_v2.0.0").

This document describes the changes and how to update your configuration files.

* [Configuration file changes](#configuration-file-changes)
* [Supplemental material changes](#supplementatl-material-changes)
* [Fields removed from the base configuration](#fields-removed-from-the-base-configuration)
* [Fields renamed in the base configuration](#fields-renamed-in-the-base-configuration)
* [Content supplement JSON file](#content-supplement-json-file)

## Configuration file changes

The current version of the Documentation generator takes configuration input on the command line and from a configuration file, an optional boilerplate document, and an optional schema supplement file. In profile and subset modes, there is an additional mode-specific configuration file.

| File             | Format     | Purpose                                                       |
| :--------------- | :--------- | :------------------------------------------------------------ |
| config           | JSON       | Top-level configuration, including all command-line options. This file also specifies the locations of other configuration  files. |
| boilerplate intro | markdown or html | Content to be inserted in the output verbatim, prior to the generated documentation. May include an `[add_toc]` placeholder to specify where to include a table of contents. |
| boilerplate postscript | markdown or html | Content to be inserted in the output verbatim, after the generated documentation. May include an `[add_toc]` placeholder to specify where to include a table of contents. |
| content supplement | JSON     | Text replacements and additions. Includes: text overrides for property descriptions, units translation (replacements for unit abbreviations), schema-specific intros, postscripts, and property description substitutions. |
| subset doc       | JSON       | Subset profile, unchanged for v3. _Link to spec for this?_         |

## Supplemental material changes

Features that previously were specified within the "Supplemental Material" markdown document are all available elsewhere:

 - "Introduction": replace with separate boilerplate intro file, file location specified in config.json as `boilerplate_intro`. Format is unchanged.
 - "Postscript": replace with separate boilerplate intro file, file location specified in config.json as `boilerplate_postscript`. Format is unchanged.
 - "Keyword Configuration": specify individual fields in config.json: `omit_version_in_headers`, `add_toc`, `actions_in_property_table`, `suppress_version_history`
 - "Description Overrides": `property_description_overrides` in content supplement (in JSON syntax)
 - "FullDescription Overrides": `property_fulldescription_overrides` in content supplement (in JSON syntax)
 - "Schema Supplement": `schema_supplement` in content supplement (in JSON syntax). No longer supports JSON payloads (use a `payload_dir` instead)
 - "Schema Documentation": `schema_link_replacements` in content supplement (in JSON syntax)

(Here, "config.json" means your base config file, specified with the `--config` command-line flag.)

The following have had analogs in the base config.json for some time, and now can only be specified in that file:

 - "Excluded Properties": `excluded_properties`
 - "Excluded Annotations": `excluded_annotations`
 - "Excluded Schemas": `excluded_schemas`
 - "Excluded patternProperties": `excluded_pattern_properties`
 - "Schema URI Mapping": `uri_mapping`
 - "Profile URI Mapping": `profile_uri_to_local`
 - "Registry URI Mapping": `registry_uri_to_local`

The "Units Translation" table is replaced by the `units_translation` field, which has been moved from config.json to the content supplement JSON file.

 - "Units Translation": `units_translation` in content supplement

## Fields removed from the base configuration

Move these fields out of the base config.json and into the content supplement:

 - `property_description_overrides`
 - `property_fulldescription_overrides`
 - `units_translation`

## Fields renamed in the base configuration

Two field names, recognized only in "Property Index" mode and specified in config.json, have been renamed:

 - `ExcludedProperties` is now `excluded_properties` (as in other modes)
 - `DescriptionOverrides` is now `description_overrides`. Note that this is distinct from the `property_description_overrides` used in the content supplement for other modes, and is provided in the base config rather than the content supplement.

## Content supplement JSON file

The content supplement contains text replacements and insertions:

 - `units_translation`: replacements for the units abbreviations used in the schema files.
 - `schema_supplement`: schema-specific intros, postscripts, and property description overrides
 - `schema_link_replacements`: mapping of URIs found in schemas to URIs to substitute. Used to replace links to external refs in documentation.
 - `property_description_overrides`: replacements for individual property descriptions, by property name
 - `property_fulldescription_overrides`: replacements for individual property descriptions, by property name. These overrides also eliminate any auto-generated explanations, like references to the definition of a property in another schema.
