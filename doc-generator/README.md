[![Build Status](https://travis-ci.com/DMTF/Redfish-Tools.svg?branch=master)](https://travis-ci.com/github/DMTF/Redfish-Tools)
<p align="center">
  <img src="http://redfish.dmtf.org/sites/all/themes/dmtf2015/images/dmtf-redfish-logo.png" alt="DMTF Redfish" width=180>

# Redfish doc generator

Copyright 2016-2021 Distributed Management Task Force, Inc. All rights reserved.

The **Redfish doc generator** &mdash; [`doc_generator.py`](doc_generator.py "doc_generator.py") &mdash; is a Python tool that generates output in a specified [format](#output-modes-and-output-formats) from JSON Schema files and supplementary content files. You use [configuration files](#configuration) to configure this output.

The Redfish doc generator v3 introduces [breaking changes](README-doc-generator-v3-changes.md) in how you configure the `doc_generator.py` tool and updates the `README` files.

For a snapshot of the *version 2* code, see [Doc Generator v2](https://github.com/DMTF/Redfish-Tools/releases/tag/doc_gen_v2.0.0 "https://github.com/DMTF/Redfish-Tools/releases/tag/doc_gen_v2.0.0").

* [Installation](#installation)
* [Usage](#usage)
* [Output modes and output formats](#output-modes-and-output-formats)
* [Configuration](#configuration)
* [Processing](#processing)
* [Notes](#notes)

# Installation

To install the Redfish doc generator, see [Installation](../README.md#installation "../README.md#installation").

# Usage

```text
usage: doc_generator.py [-h] [--config CONFIG_FILE] [-n]
                        [--format {markdown,slate,html,csv}] [--out OUTFILE]
                        [--payload_dir payload_dir] [--profile PROFILE_DOC]
                        [-t] [--subset SUBSET_DOC] [--property_index]
                        [--property_index_config_out CONFIG_FILE_OUT]
                        [--escape ESCAPE_CHARS]
                        [import_from ...]

Generate documentation for Redfish JSON schema files.

positional arguments:
  import_from           Name of a file or directory to process (wild cards are
                        acceptable). Default: json-schema

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG_FILE  Path to a config file, containing configuration in
                        JSON format.
  -n, --normative       Produce normative (developer-focused) output
  --format {markdown,slate,html,csv}
                        Output format
  --out OUTFILE         Output file (default depends on output format:
                        output.md for Markdown, index.html for HTML,
                        output.csv for CSV
  --payload_dir payload_dir
                        Directory location for JSON payload and Action
                        examples. Optional.Within this directory, use the
                        following naming scheme for example files:
                        <schema_name>-v<major_version>-example.json for JSON
                        payloads, <schema_name-v<major_version>-action-<action
                        _name>.json for action examples.
  --profile PROFILE_DOC
                        Path to a JSON profile document, for profile output.
  -t, --terse           Terse output (meaningful only with --profile). By
                        default, profile output is verbose and includes all
                        properties regardless of profile requirements. "Terse"
                        output is intended for use by Service developers,
                        including only the subset of properties with profile
                        requirements.
  --subset SUBSET_DOC   Path to a JSON profile document. Generates "Schema
                        subset" output, with the subset defined in the JSON
                        profile document.
  --property_index      Produce Property Index output.
  --property_index_config_out CONFIG_FILE_OUT
                        Generate updated config file, with specified filename
                        (property_index mode only).
  --escape ESCAPE_CHARS
                        Characters to escape (\) in generated Markdown. For
                        example, --escape=@#. Use --escape=@ if strings with
                        embedded @ are being converted to mailto links.

Example:
   doc_generator.py --format=html
   doc_generator.py --format=html --out=/path/to/output/index.html /path/to/spmf/json-files
```

For more information about Output modes and output formats, see [Output modes and output formats](#output-modes-and-output-formats).

For `doc_generator.py` examples, see [Redfish doc generator examples](README-configuration-files.md#redfish-doc-generator-examples).

# Output modes and output formats

The *output mode* defines the type of generated output, such as:

* Developer-focused, or normative
* Property index
* Subset

The *output format* defines the format of the generated output, such as Markdown, HTML, or CSV.

The doc generator supports several output modes and formats through various command-line or configuration options.

The following table describes the supported output modes and formats and provides links to:

* Sample versions of the base configuration file that produce output in that mode.
* Sample `doc_generator.py` command usage.

Depending on the output mode, the configuration keys in the base configuration file can change. Some output modes, such as the property index mode, support additional configuration keys.

<table>
  <col width="10%">
  <col width="10%">
  <col width="40%">
  <col width="20%">
  <col width="20%">
  <thead>
    <tr>
      <th align="left" valign="top">Output mode</th>
      <th align="left" valign="top">Output format</th>
      <th align="left" valign="top">Command&#8209;line&nbsp;option<br/>or<br/>Configuration&nbsp;keys</th>
      <th align="left" valign="top">Sample base configuration file</th>
      <th align="left" valign="top">Sample command usage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="left" valign="top">CSV</td>
      <td align="left" valign="top">CSV</td>
      <td align="left" valign="top"><code>--format csv</code><br/><code>"format": "csv"</code></td>
      <td align="left" valign="top"><a href="sample_inputs/csv/config.json"><code>sample_inputs/csv/config.json</code></a></td>
      <td align="left" valign="top"><a href="#csv">CSV</a></td>
    </tr>
    <tr>
      <td align="left" valign="top">Terse profile index</td><td align="left" valign="top">Markdown</td>
      <td align="left" valign="top"><code>--format csv</code><br/><code>"format": "csv"</code></td>
      <td align="left" valign="top"><a href="sample_inputs/profile_mode/config.json"><code>sample_inputs/profile_mode/config.json</code></a></td>
      <td align="left" valign="top"><a href="#terse-profile-index-in-markdown">Terse profile index in Markdown</a></td>
    </tr>
    <tr>
      <td align="left" valign="top">Property index</td><td align="left" valign="top">HTML</td>
      <td align="left" valign="top"><code>--format csv</code><br/><code>"format": "csv"</code></td>
      <td align="left" valign="top"><a href="sample_inputs/property_index/config.json"><code>sample_inputs/property_index/config.json</code></a></td>
      <td align="left" valign="top"><a href="#property-index-html">Property index HTML</a></td>
    </tr>
    <tr>
      <td align="left" valign="top">Standard</td><td align="left" valign="top">HTML</td>
      <td align="left" valign="top"><code>--format csv</code><br/><code>"format": "csv"</code></td>
      <td align="left" valign="top"><a href="sample_inputs/standard_html/config.json"><code>sample_inputs/standard_html/config.json</code></a></td>
      <td align="left" valign="top"><a href="#standard-html">Standard HTML</a></td>
    </tr>
    <tr>
      <td align="left" valign="top">Standard with normative descriptions</td><td align="left" valign="top">HTML</td>
      <td align="left" valign="top"><code>--format csv</code><br/><code>"format": "csv"</code></td>
      <td align="left" valign="top"><a href="sample_inputs/standard_html/config_normative.json"><code>sample_inputs/standard_html/config_normative.json</code></a></td>
      <td align="left" valign="top"><a href="#standard-html-with-normative-descriptions">Standard with normative descriptions HTML</a></td>
    </tr>
    <tr>
      <td align="left" valign="top">Subset</td><td align="left" valign="top">HTML</td>
      <td align="left" valign="top"><code>--format csv</code><br/><code>"format": "csv"</code></td>
      <td align="left" valign="top"><a href="sample_inputs/subset/config.json"><code>sample_inputs/subset/config.json</code></a></td>
      <td align="left" valign="top"><a href="#subset-html">Subset HTML</a></td>
  </tbody>
</table>

<!-- <dl>
   | CSV output mode</dt>
   <dd><b>Command-line option:</b> <code>--format csv</code></dd>
   <dd><b>Configuration key:</b> <code>"format": "csv"</code></dd>
   <dd><b>Sample base configuration file:</b> [`sample_inputs/csv/config.json`](sample_inputs/csv/config.json)</dd>
   <dd><b>Sample doc_generator.py command usage:</b> [CSV](#csv)</dd>
   <dt>Profile documentation in Markdown output mode</dt>
   <dd><b>Command-line option:</b> <code>--format csv</code></dd>
   <dd><b>Configuration key:</b> <code>"format": "csv"</code></dd>
   <dd><b>Sample base configuration file:</b> [`sample_inputs/profile_mode/config.json`](sample_inputs/profile_mode/config.json)</dd>
   <dd><b>Sample doc_generator.py command usage:</b> [Profile index Markdown in terse mode](#profile-index-markdown-in-terse-mode)</dd>
   <dt>Property index documentation in HTML output mode</dt>
   <dd><b>Command-line option:</b> <code>--format csv</code></dd>
   <dd><b>Configuration key:</b> <code>"format": "csv"</code></dd>
   <dd><b>Sample base configuration file:</b> [`sample_inputs/property_index/config.json`](sample_inputs/property_index/config.json)</dd>
   <dd><b>Sample doc_generator.py command usage:</b> [Property index HTML](#property-index-html)</dd>
   <dt>Standard documentation in HTML format</dt>
   <dd><b>Command-line option:</b> <code>--format csv</code></dd>
   <dd><b>Configuration key:</b> <code>"format": "csv"</code></dd>
   <dd><b>Sample base configuration file:</b> [`sample_inputs/standard_html/config.json`](sample_inputs/standard_html/config.json)</dd>
   <dd><b>Sample doc_generator.py command usage:</b> [Standard HTML](#standard-html)</dd>
   <dt>Standard with normative descriptions mode documentation in HTML format</dt>
   <dd><b>Command-line option:</b> <code>--format csv</code></dd>
   <dd><b>Configuration key:</b> <code>"format": "csv"</code></dd>
   <dd><b>Sample base configuration file:</b> [`sample_inputs/standard_html/config_normative.json`](sample_inputs/standard_html/config_normative.json)</dd>
   <dd><b>Sample doc_generator.py command usage:</b> [Standard with normative descriptions HTML](#standard-html-with-normative-descriptions)</dd>
   <dt>Subset documentation in HTML format</dt>
   <dd><b>Command-line option:</b> <code>--format csv</code></dd>
   <dd><b>Configuration key:</b> <code>"format": "csv"</code></dd>
   <dd><b>Sample base configuration file:</b> [`sample_inputs/subset/config.json`](sample_inputs/subset/config.json)</dd>
   <dd><b>Sample doc_generator.py command usage:</b> [Subset HTML](#subset-html)</dd>
</dl> -->

The type of output that the doc generator produces depends on the following command-line or configuration options:

<table>
   <col width="40%">
   <col width="60%">
   <thead>
      <tr>
         <th align="left" valign="top">Command&#8209;line&nbsp;option</th>
         <th align="left" valign="top">Description</th>
      </tr>
    </thead>
    <tbody>
      <tr>
         <td align="left" valign="top"><code>-n</code>,&nbsp;<code>--normative</code></td>
         <td align="left" valign="top">Produces normative, or developer-focused, output.</td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>--format</code></td>
         <td align="left" valign="top">
            <p>The output format. Value is:</p>
            <ul>
               <li><code>markdown</code> &mdash; Markdown file targeted for the DMTF document publication process.</li>
               <li><code>slate</code> (default) &mdash; GitHub-flavored Markdown file targeted for the <a href="https://github.com/slatedocs/slate" title="https://github.com/slatedocs/slate">Slate API doc generator</a>.</li>
               <li><code>html</code> &mdash; HyperText Markup Language (HTML) file.</li>
               <li><code>csv</code> &mdash; Comma-separated values (CSV) file.</li>
            </ul>
         </td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>--profile&nbsp;PROFILE_DOC</code></td>
         <td align="left" valign="top">Path to a JSON profile document, for profile output.</td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>-t</code>,&nbsp;<code>--terse</code></td>
         <td align="left" valign="top">Terse output, which is meaningful only with <code>--profile</code>. By default, profile output is verbose and includes all properties regardless of profile requirements. *Terse* output is intended for use by service developers, including only the subset of properties with profile requirements.</td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>--subset SUBSET_DOC</code></td>
         <td align="left" valign="top">Path to a JSON profile document. Generates *Schema subset* output, with the subset defined in the JSON profile document.</td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>--property_index</code></td>
         <td align="left" valign="top">Produces <a href="README-property-index-mode.md" title="README-property-index-mode.md"><i>property index</i> output</a>.</td>
      </tr>
   </tbody>
</table>

# Configuration

Use the `--config` option to specify the [base configuration file](README-configuration-files.md "README-configuration-files.md"). The base configuration file defines:

* Required and optional parameters that you can also specify on the command line. 
* Some required parameters, such as URI mappings, that you cannot specify on the command line.

Several flavors of configuration files are available. See [Redfish doc generator: Configuration and supplementary files](README-configuration-files.md).

# Processing

By default, `doc_generator.py` looks for a `json-schema` directory and supplemental files in the [configuration](#configuration) file that you specify when you run it.

Typically, the tool processes an entire set of JSON Schema files for a version.

# Notes

Normative output prefers long descriptions to descriptions.

For Slate, place the `index.html.md` output in your Slate repository's source directory.

See also:

* [Redfish doc generator v3 changes](README-doc-generator-v3-changes.md "README-doc-generator-v3-changes.md") &mdash; How to restructure your configuration files.
* [Redfish doc generator: Configuration and supplementary files](README-configuration-files.md "README-configuration-files.md") &mdash; Configuration and supplementary files for the Redfish doc generator.
* [Redfish doc generator: Property index configuration](README-property-index-mode.md "README-property-index-mode.md") &mdash; Property index mode.
