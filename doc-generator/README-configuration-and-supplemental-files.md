[![Build Status](https://travis-ci.com/DMTF/Redfish-Tools.svg?branch=master)](https://travis-ci.com/github/DMTF/Redfish-Tools)
<p align="center">
  <img src="http://redfish.dmtf.org/sites/all/themes/dmtf2015/images/dmtf-redfish-logo.png" alt="DMTF Redfish" width=180>

# Redfish doc generator: Configuration and supplemental files

Copyright 2016-2021 Distributed Management Task Force, Inc. All rights reserved.

To configure the generated documentation, you specify command-line arguments and configuration keys in the base configuration file. If you specify a configuration option in more than one way, command-line arguments take precedence over configuration keys.

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

The names of some configuration keys differ from their command&#8209;line argument equivalents. Unless otherwise noted, the configuration key has the same meaning as its command&#8209;line argument equivalent.

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

For descriptions of the configuration keys, see [Base configuration file](README-base-configuration-file.md "README-base-configuration-file.md").

## Content supplement configuration file

The content supplement configuration file is a JSON file that that defines text overrides for property descriptions, replacements for unit abbreviations, and schema-specific content to apply to the generated schema documentation. The base configuration file contains a pointer to this file.

For descriptions of the configuration keys, see [Content supplement configuration file](README-content-supplement-configuration-file.md "README-content-supplement-configuration-file.md").

## Boilerplate intro file

**Sample boilerplate intro file:** <a href="sample_inputs/standard_html/intro.md"><code>intro.md</code></a>

The boilerplate intro file is a Markdown or HTML file that contains supplementary content to include in the output before the generated documentation.

This file can include an <code>[add_toc]</code> directive that specifies location for the table of contents.

## Boilerplate postscript file

**Sample boilerplate postscript file:** <a href="sample_inputs/standard_html/postscript.md"><code>postscript.md</code></a>

The boilerplate postscript file is a Markdown or HTML file that contains supplementary content to include in the output after the generated documentation.

This file can include an <code>[add_toc]</code> directive that specifies location for the table of contents.
