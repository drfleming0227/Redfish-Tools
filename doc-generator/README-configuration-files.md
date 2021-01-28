[![Build Status](https://travis-ci.com/DMTF/Redfish-Tools.svg?branch=master)](https://travis-ci.com/github/DMTF/Redfish-Tools)
<p align="center">
  <img src="http://redfish.dmtf.org/sites/all/themes/dmtf2015/images/dmtf-redfish-logo.png" alt="DMTF Redfish" width=180>

# Redfish doc generator: Configuration files

## Contents

* [About](#about)
* [Subset configuration file](#subset-configuration-file)
* [Property index configuration file](#property-index-configuration-file)

## About

To configure the generated documentation, the **Redfish doc generator** accepts input from the command line and from configuration files.

This topic describes configuration input that the doc generator reads from the following JSON configuration files:

* <a href="#base-configuration-file">Base configuration file</a> is a JSON file that configures the generated documentation and can include pointers to the <a href="#content-supplement-configuration-file-overview">content supplement configuration file</a> and the [boilerplate intro](README-supplementary-files.md#boilerplate-intro-supplementary-file "README-supplementary-files.md#boilerplate-intro-supplementary-file") and [boilerplate postscript](README-supplementary-files.md#boilerplate-postscript-file "README-supplementary-files.md#boilerplate-postscript-file") supplementary content files.

    Depending on the <a href="#output-modes">output mode</a>, the configuration keys in the base configuration file can change. Some output modes, such as the property index mode, support additional configuration keys.

    The names of some configuration keys differ from their command&#8209;line argument equivalents. Unless otherwise noted, the configuration key has the same meaning as its command&#8209;line argument equivalent.

    For information about the base configuration file, see [README-base-configuration-file.md "README-base-configuration-file.md"]

* <a href="#content-supplement-configuration-file">Content&nbsp;supplement&nbsp;configuration&nbsp;file</a> is a JSON file that defines text overrides for property descriptions, replacements for unit abbreviations, and schema-specific content including introductions, postscripts, and property description substitutions. The base configuration file contains a pointer to this file.

If you specify an option in more than one way, command&#8209;line arguments override the configuration file keys.

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

