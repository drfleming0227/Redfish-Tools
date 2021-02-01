[![Build Status](https://travis-ci.com/DMTF/Redfish-Tools.svg?branch=master)](https://travis-ci.com/github/DMTF/Redfish-Tools)
<p align="center">
  <img src="http://redfish.dmtf.org/sites/all/themes/dmtf2015/images/dmtf-redfish-logo.png" alt="DMTF Redfish" width=180>

# Redfish doc generator

Copyright 2016-2021 Distributed Management Task Force, Inc. All rights reserved.

The **Redfish doc generator** &mdash; [`doc_generator.py`](doc_generator.py "doc_generator.py") &mdash; is a Python tool that generates documentation in a specified or default [*output mode and format*](#output-modes-and-formats) from JSON Schema files and supplemental files.

To configure the generated documentation, specify command-line arguments and configuration keys in the base configuration file. If you specify a configuration option in more than one way, command&#8209;line arguments take precedence over the configuration keys.

> **Important notice about the Redfish doc generator: v3:**
>
> The doc generator v3 contains _**breaking configuration changes**_ and updates to the `README` files. For information about these changes, see [Redfish doc generator: v3 changes](README-doc-generator-v3-changes.md "README-doc-generator-v3-changes.md").
> 
> To use the previous version of the doc generator, see [Doc Generator v2](https://github.com/DMTF/Redfish-Tools/releases/tag/doc_gen_v2.0.0 "https://github.com/DMTF/Redfish-Tools/releases/tag/doc_gen_v2.0.0").

## Contents

* [Installation](#installation)
* [Usage](#usage)
* [Configuration](#configuration)
* [Output modes and formats](#output-modes-and-formats)
* [Examples](#examples)
* [Processing](#processing)

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

## Configuration

To configure the generated documentation, specify command-line arguments and configuration keys in the base configuration file. If you specify a configuration option in more than one way, command-line arguments take precedence over configuration keys.

Use the `--config` command-line argument to specify the [base configuration file](README-configuration-files.md#base-configuration-file "README-configuration-files.md/#base-configuration-file").

> **Note:** You can specify some configuration information, such as URI mappings, through the base configuration file only and not on the command line.

Several flavors of the base configuration file are available. Additionally, the base configuration file can embed the content supplement configuration file and supplemental files. See [Redfish doc generator: Configuration and supplemental files](README-configuration-and-supplemental-files.md "README-configuration-and-supplemental-files.md").

## Output modes and formats

To generate documentation for a specific audience, such as a developer, in a specific format, such as Markdown, specify an output mode and output format through command-line arguments and configuration keys. Command-line arguments take precedence over configuration keys.

So, for example, you could produce a normative HTML document for developers.

* [Output modes](#output-modes)
* [Output formats](#output-formats)
* [Command-line arguments that define the output mode and format](#command-line-arguments-that-define-the-output-mode-and-format)
* [Base configuration files that define the output mode and format](#base-configuration-files-that-define-the-output-mode-and-format)

### Output modes

The *output mode* defines the type and audience of the generated document:

| Output&nbsp;mode   | Description                          |
| :----------------- | :----------------------------------- |
| <a id="standard-mode"></a>Standard | Guide for novice&nbsp;and&nbsp;experienced&nbsp;developers. |
| <a id="standard-normative-mode"></a>Standard&nbsp;normative | Guide with normative descriptions for developers. Normative output prefers long descriptions to descriptions. |
| <a id="profile-mode"></a>Profile | Document with a subset of properties with profile requirements for service developers. A profile mode document can be terse or verbose. Default is verbose. |
| <a id="subset-mode"></a>Subset | Subset of schema to include in white papers or other documents. |
| <a id="property-index-mode"></a>Property index | <a href="README-property-index-mode.md" title="README-property-index-mode.md">Property index output</a> for schema authors to enable them to locate existing property definitions within the Redfish Schema. End users and other consumers of Redfish data can also use a property index to look up property definitions without regard to their location in the Schema. |

### Output formats

The *output format* defines the format of the generated document:

| Output&nbsp;format    | Description                      |
| :-------------------- | :------------------------------- |
| <code>markdown</code> | Markdown file targeted for the DMTF document publication process. |
| <code>slate</code>    | (default) GitHub-flavored Markdown file targeted for the <a href="https://github.com/slatedocs/slate" title="https://github.com/slatedocs/slate">Slate API doc generator</a>. For Slate, place the <code>index.html.md</code> output in your Slate repository's source directory. |
| <code>html</code>     | HyperText Markup Language (HTML) file. |
| <code>csv</code>      | Comma-separated values (CSV) file. |

### Command-line arguments that define the output mode and format

Use the following command-line options to define the output mode and format:

<table>
   <thead>
      <tr>
         <th align="left" valign="top">Command&#8209;line&nbsp;option</th>
         <th align="left" valign="top">Description</th>
      </tr>
    </thead>
    <tbody>
      <tr>
         <td align="left" valign="top"><code>-n</code>,&nbsp;<code>--normative</code></td>
         <td align="left" valign="top">Produces <a href="#standard-normative-mode">standard normative mode</a>, or developer-focused, output.</td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>--format</code></td>
         <td align="left" valign="top">
            <p>Defines the <a href="#output-formats">output format</a>. Value is:</p>
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
         <td align="left" valign="top">Defines path to a JSON profile document, for <a href="#terse-profile-mode">profile mode</a> output.</td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>-t</code>,&nbsp;<code>--terse</code></td>
         <td align="left" valign="top">Generates <a href="#terse-profile-mode">terse profile mode</a> output, which includes a subset of properties with profile requirements. Meaningful only with <code>--profile</code>.</td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>--subset SUBSET_DOC</code></td>
         <td align="left" valign="top">Defines path to a JSON profile document. Generates <a href="#subset-mode"><i>Schema subset mode</i></a> output, with the subset defined in the JSON profile document.</td>
      </tr>
      <tr>
         <td align="left" valign="top"><code>--property_index</code></td>
         <td align="left" valign="top">Produces <a href="#property-index-mode"><i>property index mode</i></a> output.</td>
      </tr>
   </tbody>
</table>

### Base configuration files that define the output mode and format

Depending on the output mode and format, the configuration keys in the base configuration file can change. Some output modes, such as the property index mode, support additional configuration keys.

The doc generator supports several output modes through various command-line or configuration options. The following table:

* Lists the supported output modes.
* Provides links to sample versions of the base configuration file.
* Provides links to examples of `doc_generator.py` command usage.

| Output mode        | Sample base configuration file | Example command usage |
| :----------------- | :----------------------------- | :-------------------- |
| CSV                | [`sample_inputs/csv/config.json`](sample_inputs/csv/config.json) | [CSV format](README-configuration-files.md#csv-format) |
| Profile            | [`sample_inputs/profile_mode/config.json`](sample_inputs/profile_mode/config.json) | [Terse profile mode in Markdown format](README-configuration-files.md#terse-profile-mode-in-markdown-format) |
| Property index     | [`sample_inputs/property_index/config.json`](sample_inputs/property_index/config.json) | [Property index mode in HTML format](README-configuration-files.md#property-index-mode-in-html-format) |
| Standard           | [`sample_inputs/standard_html/config.json`](sample_inputs/standard_html/config.json) | [Standard mode in HTML format](README-configuration-files.md#standard-mode-in-html-format) |
| Standard normative | [`sample_inputs/standard_html/config_normative.json`](sample_inputs/standard_html/config_normative.json) | [Standard normative mode in HTML format](README-configuration-files.md#standard-normative-mode-in-html-format) |
| Subset             | [`sample_inputs/subset/config.json`](sample_inputs/subset/config.json) | [Subset mode in HTML format](README-configuration-files.md#subset-mode-in-html-format) |

Depending on the output mode, the configuration keys in the base configuration file can change. Some output modes, such as the property index mode, support additional configuration keys.

## Examples

For `doc_generator.py` command examples, see [Redfish doc generator: examples](README-examples.md "README-examples.md").

## Processing

The doc generator reads the [base configuration file](README-configuration-and-supplemental-files#base=configuration-file) to locate the `json-schema` directory, the optional content supplement configuration file, and any supplemental files.

Typically, the tool processes an entire set of JSON Schema files for a version.
