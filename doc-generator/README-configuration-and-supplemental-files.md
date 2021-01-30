[![Build Status](https://travis-ci.com/DMTF/Redfish-Tools.svg?branch=master)](https://travis-ci.com/github/DMTF/Redfish-Tools)
<p align="center">
  <img src="http://redfish.dmtf.org/sites/all/themes/dmtf2015/images/dmtf-redfish-logo.png" alt="DMTF Redfish" width=180>

# Redfish doc generator: Configuration and supplemental files

## Contents

* [About](#about)
* [Base configuration file](#base-configuration-file)
* [Content supplement configuration file](#content-supplement-configuration-file)
* [Boilerplate intro file](#boilerplate-intro-file)
* [Boilerplate postscript file](#boilerplate-postscript-file)

## About

To configure the generated documentation, the **Redfish doc generator** reads command-line arguments and configuration file keys. If you specify an option in more than one way, command&#8209;line arguments take precendence over the configuration file keys.

The doc generator reads configuration keys from the [base configuration file](#base-configuration-file) and, if included, the [content supplement configuration file](#content-supplement-configuration-file). Additionally, the doc generator includes content from the <a href="#boilerplate-intro-file">boilerplate&nbsp;intro</a> and <a href="#boilerplate-postscript-file">boilerplate&nbsp;postscript</a> supplemental files.

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

The content supplement configuration file is a JSON file that defines text overrides for property descriptions, replacements for unit abbreviations, and schema-specific content including introductions, postscripts, and property description substitutions. The base configuration file contains a pointer to this file.

For descriptions of the configuration keys, see [Content supplement configuration file](README-content-supplement-configuration-file.md "README-content-supplement-configuration-file.md").

## Boilerplate intro file

**Sample boilerplate intro file:** <a href="sample_inputs/standard_html/intro.md"><code>intro.md</code></a>

The boilerplate intro file is a Markdown or HTML file that contains supplementary content to include in the output before the generated documentation.

Can include an <code>[add_toc]</code> directive that specifies location for the table of contents.

## Boilerplate postscript file

**Sample boilerplate postscript file:** <a href="sample_inputs/standard_html/postscript.md"><code>postscript.md</code></a>

The boilerplate postscript file is a Markdown or HTML file that contains supplementary content to include in the output after the generated documentation.

Can include an <code>[add_toc]</code> directive that specifies location for the table of contents.


