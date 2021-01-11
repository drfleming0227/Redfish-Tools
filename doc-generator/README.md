# Redfish docs generator

Copyright 2016-2021 Distributed Management Task Force, Inc. All rights reserved.

## Contents

* [Version 3 changes](#version-3-changes)
* [About](#about)
* [Installation](#installation)
* [Usage](#usage)
* [Configuration](#configuration)
* [Notes](#notes)

## Version 3 changes

The [Redfish docs generator v3](CHANGES_v2_to_v3.md) introduces breaking changes in how you configure the `doc_generator.py` tool and updates the `README` file. See [Doc Generator v2](https://github.com/DMTF/Redfish-Tools/releases/tag/doc_gen_v2.0.0 "https://github.com/DMTF/Redfish-Tools/releases/tag/doc_gen_v2.0.0") for a snapshot of the *version 2* code.

## About

The Redfish docs generator &mdash; [`doc_generator.py`](#doc_generator.py) &mdash; is a Python tool that processes JSON Schema files to generate Markdown, Slate, HTML, CSV, or property index documentation. Typically, the tool processes an entire set of JSON Schema files for a version.

By default, `doc_generator.py` looks for a `json-schema` directory and supplemental files in the [configuration](#configuration) file that you specify when you run it. Several flavors of configuration files are available.

Output formats include:

* (Default) GitHub-flavored Markdown targeted for the [Slate API docs generator](https://github.com/slatedocs/slate "https://github.com/slatedocs/slate")
* Markdown targeted for the DMTF document publication process
* HTML
* [*Property index* documentation](README_Property_Index.md)
* CSV

## Installation

1. [Clone this repository and install Python](https://github.com/DMTF/Redfish-Tools#installation "https://github.com/DMTF/Redfish-Tools#installation").
1. On the machine from which you will run `doc_generator.py`, install the following software, which is required for HTML output:
    * [Install Python&#8209;Markdown](https://python-markdown.github.io/install/ "https://python-markdown.github.io/install/").
    * [Install Pygments](http://pygments.org/ "http://pygments.org/").
    * Use `pip` to install requirements:

      ```bash
      $ cd doc-generator
      $ pip install -r requirements.txt
      ```
1. (Optional) If you make changes to the `doc_generator.py` code:
    * Install [pytest](https://docs.pytest.org/en/latest/getting-started.html "https://docs.pytest.org/en/latest/getting-started.html").
    * Run the tests:

      ```bash
      $ cd doc-generator
      $ pip install -r dev_requirements.txt
      ```

      To run the tests:

      ```bash
      $ cd doc-generator
      $ pytest
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
```

For examples, see [Redfish docs generator: Configuration](README_config_files.md).

## Configuration

Use the `--config` option to specify the configuration file, which defines:

* Many command-line options
* Some required parameters, such as URI mappings, that you cannot specify on the command line
* Many optional parameters

See [Redfish docs generator: Configuration](README_config_files.md).

## Notes

Normative output prefers long descriptions to descriptions.

For Slate, place the `index.html.md` output in your Slate repository's source directory.

See also:

* [Redfish docs generator: V3 changes](CHANGES_v2_to_v3.md) &mdash; How to restructure your existing configuration files.
* [Redfish docs generator: Configuration](README_config_files.md) &mdash; Configuration files for the Redfish docs generator.
* [Redfish docs generator: Property index mode](README_Property_Index.md) &mdash; Property index mode.

