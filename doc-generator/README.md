[![Build Status](https://travis-ci.com/DMTF/Redfish-Tools.svg?branch=master)](https://travis-ci.com/github/DMTF/Redfish-Tools)
<p align="center">
  <img src="http://redfish.dmtf.org/sites/all/themes/dmtf2015/images/dmtf-redfish-logo.png" alt="DMTF Redfish" width=180>

# Redfish doc generator

Copyright 2016-2021 Distributed Management Task Force, Inc. All rights reserved.

## Contents

* [About](#about)
* [Installation](#installation)
* [Usage](#usage)
* [Examples](#examples)
* [Output modes and output formats](#output-modes-and-output-formats)
* [Configuration](#configuration)
* [Processing](#processing)

## About

The **Redfish doc generator** &mdash; [`doc_generator.py`](doc_generator.py "doc_generator.py") &mdash; is a Python tool that generates output in a specified or default [output mode and format](#output-modes-and-output-formats) from JSON Schema files and supplementary content files. The doc generator reads configuration keys from [configuration files](#configuration) to configure this output.

> **Important:** The doc generator v3 contains [breaking configuration changes](README-doc-generator-v3-changes.md) and updates to the `README` files. For a snapshot of the *version 2* code, see [Doc Generator v2](https://github.com/DMTF/Redfish-Tools/releases/tag/doc_gen_v2.0.0 "https://github.com/DMTF/Redfish-Tools/releases/tag/doc_gen_v2.0.0").

## Installation

1. Clone the `Redfish-Tools` repository:
   ```zsh
   % git clone git@github.com:DMTF/Redfish-Tools.git
   % git remote add upstream git@github.com:DMTF/Redfish-Tools.git
   ```
1. [Download and install Python](https://www.python.org/downloads/ "https://www.python.org/downloads/") on the machine from which you will run the tools.
1. Install the following software, which is required for HTML output:
   * [Install Python‑Markdown](https://python-markdown.github.io/install/ "https://python-markdown.github.io/install/").
   * [Install Pygments](http://pygments.org/ "http://pygments.org/").
   * Install requirements:
      ```zsh
      % cd doc-generator
      % pip install -r requirements.txt
      ```
1. (Optional) To make changes to the `doc_generator.py` code, install [`pytest`](https://docs.pytest.org/en/latest/getting-started.html "https://docs.pytest.org/en/latest/getting-started.html"):

    ```zsh
    % cd doc-generator
    % pip install -r dev_requirements.txt
    ```

## Usage

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

For information about output modes and output formats, see [Output modes and output formats](#output-modes-and-output-formats).

## Examples

For `doc_generator.py` examples, see [Redfish doc generator examples](README-configuration-files.md#redfish-doc-generator-examples).

## Output modes and output formats

The *output mode* defines the type of generated output:

| Mode               | Audience                         | Description |
| :----------------- | :------------------------------- | :---------- |
| CSV                | ??                               | Comma-separated values (CSV) file. |
| Standard           | Novice&nbsp;and&nbsp;experienced&nbsp;developer | Standard guide. |
| Standard&nbsp;normative | Developer                        | Standard guide with normative descriptions. Normative output prefers long descriptions to descriptions. |
| Terse profile      | Service developer                | Includes only the subset of properties with profile requirements. Terse output is meaningful only for profile mode. |
| Verbose profile    | ??                               | By default, profile mode is verbose and includes all properties regardless of profile requirements. |
| Subset             | ??                               | ?? |
| Property index     | ??                               | ?? |

The *output format* defines the format of the generated output:

| Output&nbsp;format    | Description                      |
| :-------------------- | :------------------------------- |
| <code>markdown</code> | Markdown file targeted for the DMTF document publication process. |
| <code>slate</code>    | (default) GitHub-flavored Markdown file targeted for the <a href="https://github.com/slatedocs/slate" title="https://github.com/slatedocs/slate">Slate API doc generator</a>. For Slate, place the <code>index.html.md</code> output in your Slate repository's source directory. |
| <code>html</code>     | HyperText Markup Language (HTML) file. |
| <code>csv</code>      | Comma-separated values (CSV) file. |

Use the following command-line options to define the output mode and format:

<table>
   <col width="20%">
   <col width="40%">
   <col width="20%">
   <col width="20%">
   <thead>
      <tr>
         <th align="left" valign="top">Command&#8209;line&nbsp;option</th>
         <th align="left" valign="top">Description</th>
         <th align="left" valign="top">Output modes</th>
         <th align="left" valign="top">Output format</th>
      </tr>
    </thead>
    <tbody>
      <tr>
         <td align="left" valign="top"><code>-n</code>,&nbsp;<code>--normative</code></td>
         <td align="left" valign="top">Produces normative, or developer-focused, output.</td>
         <td align="left" valign="top">Standard normative</td>
         <td/>
      </tr>
      <tr>
         <td align="left" valign="top"><code>--format</code></td>
         <td align="left" valign="top">
            <p>Defines the output format. Value is:</p>
            <ul>
               <li><code>markdown</code> &mdash; Markdown file targeted for the DMTF document publication process.</li>
               <li><code>slate</code> (default) &mdash; GitHub-flavored Markdown file targeted for the <a href="https://github.com/slatedocs/slate" title="https://github.com/slatedocs/slate">Slate API doc generator</a>.</li>
               <li><code>html</code> &mdash; HyperText Markup Language (HTML) file.</li>
               <li><code>csv</code> &mdash; Comma-separated values (CSV) file.</li>
            </ul>
         </td>
         <td/>
         <td align="left" valign="top">Use to specify the output format.</td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>--profile&nbsp;PROFILE_DOC</code></td>
         <td align="left" valign="top">Defines path to a JSON profile document, for profile output.</td>
         <td align="left" valign="top">Terse profile<br/>Verbose profile</td>
         <td/>
      </tr>
      <tr>
         <td align="left" valign="top"><code>-t</code>,&nbsp;<code>--terse</code></td>
         <td align="left" valign="top">Generates terse output, which includes a subset of properties with profile requirements. Meaningful only with <code>--profile</code>.</td>
         <td align="left" valign="top">Terse profile</td>
         <td/>
      </tr>
      <tr>
         <td align="left" valign="top"><code>--subset SUBSET_DOC</code></td>
         <td align="left" valign="top">Defines path to a JSON profile document. Generates *Schema subset* output, with the subset defined in the JSON profile document.</td>
         <td align="left" valign="top">Subset</td>
         <td/>
      </tr>
      <tr>
         <td align="left" valign="top"><code>--property_index</code></td>
         <td align="left" valign="top">Produces <a href="README-property-index-mode.md" title="README-property-index-mode.md"><i>property index</i> output</a>.</td>
         <td align="left" valign="top">Property index</td>
         <td/>
      </tr>
   </tbody>
</table>

## Configuration

Use the `--config` option to specify the [base configuration file](README-configuration-files.md#base-configuration-file "README-configuration-files.md/#base-configuration-file"). The base configuration file defines configuration keys that define the generated output. Some configuration information, such as URI mappings, cannot be specified on the command line.

Several flavors of configuration files are available. See [Redfish doc generator: Configuration and supplementary files](README-configuration-files.md).

The following table describes the supported output modes and formats and provides links to samples of `doc_generator.py` command usage.

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
         <th align="left" valign="top">Format</th>
         <th align="left" valign="top">Sample command usage</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td align="left" valign="top">CSV</td>
         <td align="left" valign="top">CSV</td>
         <td align="left" valign="top"><a href="README-configuration-files.md#csv">CSV</a></td>
      </tr>
      <tr>
         <td align="left" valign="top">Terse profile</td>
         <td align="left" valign="top">Markdown</td>
         <td align="left" valign="top"><a href="README-configuration-files.md#terse-profile-index-in-markdown">Terse profile index in Markdown</a></td>
      </tr>
      <tr>
         <td align="left" valign="top">Property index</td>
         <td align="left" valign="top">HTML</td>
         <td align="left" valign="top"><a href="README-configuration-files.md#property-index-html">Property index HTML</a></td>
      </tr>
      <tr>
         <td align="left" valign="top">Standard</td>
         <td align="left" valign="top">HTML</td>
         <td align="left" valign="top"><a href="README-configuration-files.md#standard-html">Standard HTML</a></td>
      </tr>
      <tr>
         <td align="left" valign="top">Standard normative</td>
         <td align="left" valign="top">HTML</td>
         <td align="left" valign="top"><a href="README-configuration-files.md#standard-html-with-normative-descriptions">Standard with normative descriptions HTML</a></td>
      </tr>
      <tr>
         <td align="left" valign="top">Subset</td>
         <td align="left" valign="top">HTML</td>
         <td align="left" valign="top"><a href="README-configuration-files.md#subset-html">Subset HTML</a></td>
      </tr>
   </tbody>
</table>

## Processing

By default, `doc_generator.py` looks for a `json-schema` directory and supplemental files in the [configuration](#configuration) file that you specify when you run it.

Typically, the tool processes an entire set of JSON Schema files for a version.
