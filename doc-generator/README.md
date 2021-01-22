[![Build Status](https://travis-ci.com/DMTF/Redfish-Tools.svg?branch=master)](https://travis-ci.com/github/DMTF/Redfish-Tools)
<p align="center">
  <img src="http://redfish.dmtf.org/sites/all/themes/dmtf2015/images/dmtf-redfish-logo.png" alt="DMTF Redfish" width=180>

# Redfish doc generator

Copyright 2016-2021 Distributed Management Task Force, Inc. All rights reserved.

The **Redfish doc generator** &mdash; [`doc_generator.py`](doc_generator.py "doc_generator.py") &mdash; is a Python tool that generates output in a specified [format](#output-formats) from JSON Schema files and supplementary content files.

## Contents

* [Version 3 changes](#version-3-changes)
* [Installation](#installation)
* [Usage](#usage)
* [Output formats](#output-formats)
* [Configuration](#configuration)
* [Processing](#processing)
* [Notes](#notes)

## Version 3 changes

The Redfish doc generator v3:

* Introduces [breaking changes](CHANGES_v2_to_v3.md) in how you configure the `doc_generator.py` tool.
* Updates the `README` files.

For a snapshot of the *version 2* code, see [Doc Generator v2](https://github.com/DMTF/Redfish-Tools/releases/tag/doc_gen_v2.0.0 "https://github.com/DMTF/Redfish-Tools/releases/tag/doc_gen_v2.0.0").

## Installation

To install the Redfish doc generator, see [Installation](../README.md#installation "../README.md#installation").

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

For more information about the output formats, see [Output formats](#output-formats).

For `doc_generator.py` examples, see [Redfish doc generator examples](README_config_files.md#redfish-docs-generator-examples).

## Output formats

The type of output that the doc generator produces depends on the following command-line options:

| Command-line&nbsp;option | Description                                                                   |
| :----------------------- | :---------------------------------------------------------------------------- |
| `-n`,&nbsp;`--normative` | Produces normative, or developer-focused, output. |
| `--format`               | The output format. Value is: <ul><li><code>markdown</code> &mdash; Markdown targeted for the DMTF document publication process</li><li><code>slate</code> (default) &mdash; GitHub-flavored Markdown targeted for the [Slate API doc generator](https://github.com/slatedocs/slate "https://github.com/slatedocs/slate")</li><li><code>html</code> &mdash; HTML</li><li><code>csv</code></li></ul>, which is the default output
| `--profile PROFILE_DOC`  | Path to a JSON profile document, for profile output. |
| `-t`,&nbsp;`--terse`     | Terse output (meaningful only with --profile). By default, profile output is verbose and includes all properties regardless of profile requirements. "Terse"output is intended for use by Service developers, including only the subset of properties with profile requirements. |
| `--subset SUBSET_DOC`    | Path to a JSON profile document. Generates *Schema subset* output, with the subset defined in the JSON profile document. |
| `--property_index`       | Produces [*property index* output](README_Property_Index.md "README_Property_Index.md"). |

## Configuration

Use the `--config` option to specify the [base configuration file](README_config_files.md "README_config_files.md"). The base configuration file defines:

* Required and optional parameters that you can also specify on the command line. 
* Some required parameters, such as URI mappings, that you cannot specify on the command line.

Several flavors of configuration files are available. See [Redfish doc generator: Configuration](README_config_files.md).

## Processing

By default, `doc_generator.py` looks for a `json-schema` directory and supplemental files in the [configuration](#configuration) file that you specify when you run it.

Typically, the tool processes an entire set of JSON Schema files for a version.

## Notes

Normative output prefers long descriptions to descriptions.

For Slate, place the `index.html.md` output in your Slate repository's source directory.

See also:

* [Redfish doc generator v3 changes](CHANGES_v2_to_v3.md "CHANGES_v2_to_v3.md") &mdash; How to restructure your configuration files.
* [Redfish doc generator: Configuration and supplementary files](README_config_files.md "README_config_files.md") &mdash; Configuration and supplementary files for the Redfish doc generator.
* [Redfish doc generator: Property index configuration](README_Property_Index.md "README_Property_Index.md") &mdash; Property index mode.
