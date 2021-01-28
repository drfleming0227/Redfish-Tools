[![Build Status](https://travis-ci.com/DMTF/Redfish-Tools.svg?branch=master)](https://travis-ci.com/github/DMTF/Redfish-Tools)
<p align="center">
  <img src="http://redfish.dmtf.org/sites/all/themes/dmtf2015/images/dmtf-redfish-logo.png" alt="DMTF Redfish" width=180>

# Redfish doc generator: Configuration files

To configure the generated documentation, the **Redfish doc generator** reads command-line arguments and configuration file keys. If you specify an option in more than one way, command&#8209;line arguments override the configuration file keys.

The doc generator reads configuration keys from these JSON configuration files:

* [Base configuration file](#base-configuration-file)
* [Content supplement configuration file](#contentsupplementconfigurationfile)

## Base configuration file

The base configuration file is a JSON file that configures the generated documentation and can include pointers to the <a href="#content-supplement-configuration-file-overview">content supplement configuration file</a> and the [boilerplate intro](README-supplementary-files.md#boilerplate-intro-supplementary-file "README-supplementary-files.md#boilerplate-intro-supplementary-file") and [boilerplate postscript](README-supplementary-files.md#boilerplate-postscript-file "README-supplementary-files.md#boilerplate-postscript-file") supplementary content files.

Depending on the <a href="#output-modes">output mode</a>, the configuration keys in the base configuration file can change. Some output modes, such as the property index mode, support additional configuration keys.

The names of some configuration keys differ from their command&#8209;line argument equivalents. Unless otherwise noted, the configuration key has the same meaning as its command&#8209;line argument equivalent.

See [Base configuration file](README-base-configuration-file.md "README-base-configuration-file.md").

## Content&nbsp;supplement&nbsp;configuration&nbsp;file

The content supplement configuration file is a JSON file that defines text overrides for property descriptions, replacements for unit abbreviations, and schema-specific content including introductions, postscripts, and property description substitutions. The base configuration file contains a pointer to this file.

See [Content supplement configuration file](README-content-supplement-configuration-file.md "README-content-supplement-configuration-file.md").
