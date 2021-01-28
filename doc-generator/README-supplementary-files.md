[![Build Status](https://travis-ci.com/DMTF/Redfish-Tools.svg?branch=master)](https://travis-ci.com/github/DMTF/Redfish-Tools)
<p align="center">
  <img src="http://redfish.dmtf.org/sites/all/themes/dmtf2015/images/dmtf-redfish-logo.png" alt="DMTF Redfish" width=180>

# Redfish doc generator: Supplementary files

The **Redfish doc generator** takes content from the following supplementary files:

* <a href="#boilerplate-intro-file">Boilerplate&nbsp;intro file</a>
* <a href="#boilerplate-postscript-file">Boilerplate&nbsp;postscript&nbsp;file</a>

## Boilerplate intro file

**Sample boilerplate intro file:** <a href="sample_inputs/standard_html/intro.md"><code>intro.md</code></a>

The boilerplate intro file is a Markdown or HTML file that contains supplementary content to include in the output before the generated documentation.

Can include an <code>[add_toc]</code> directive that specifies location for the table of contents.

## Boilerplate postscript file

**Sample boilerplate postscript file:** <a href="sample_inputs/standard_html/postscript.md"><code>postscript.md</code></a>

The boilerplate postscript file is a Markdown or HTML file that contains supplementary content to include in the output after the generated documentation.

Can include an <code>[add_toc]</code> directive that specifies location for the table of contents.

## Include the supplementary files

To include the supplementary files, add a pointer to one or both files at the bottom of the base configuration file:

```json
{
   ...
  "boilerplate_intro": "./intro.md",
  "boilerplate_postscript": "./postscript.md", 
  "content_supplement": "./content_supplement.json"
}
```
