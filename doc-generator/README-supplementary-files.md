[![Build Status](https://travis-ci.com/DMTF/Redfish-Tools.svg?branch=master)](https://travis-ci.com/github/DMTF/Redfish-Tools)
<p align="center">
  <img src="http://redfish.dmtf.org/sites/all/themes/dmtf2015/images/dmtf-redfish-logo.png" alt="DMTF Redfish" width=180>

# Redfish doc generator: Supplementary files

## Contents

* [About](#about)
* [Boilerplate intro supplementary file](#boilerplate-intro-supplementary-file)
* [Boilerplate postscript supplementary file](#boilerplate-postscript-supplementary-file)

## About

The **Redfish doc generator** accepts input from supplementary content files.

This topic describes supplementary content from HTML or Markdown files:

* The <a href="#boilerplate-intro-supplementary-file">boilerplate&nbsp;intro supplementary file</a> defines content to include in the output before the generated documentation.
* The <a href="#boilerplate-postscript-supplementary-file">boilerplate&nbsp;postscript&nbsp;supplementary&nbsp;file</a> defines content to include in the output after the generated documentation.

## Boilerplate intro supplementary file

The boilerplate intro file is a Markdown or HTML that contains supplementary content to include in the output before the generated documentation. Can include an <code>[add_toc]</code> directive that specifies location for the table of contents.

For an example boilerplate intro file, see <a href="sample_inputs/standard_html/intro.md"><code>intro.md</code></a>.

## Boilerplate postscript supplementary file

The boilerplate postscript file is a Markdown or HTML that contains supplementary content to include in the output after the generated documentation. 

For an example boilerplate postscript file, see <a href="sample_inputs/standard_html/postscript.md"><code>postscript.md</code></a>.
