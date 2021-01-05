# Redfish documentation generator

Copyright 2016-2021 Distributed Management Task Force, Inc. All rights reserved.

Version 3 introduces breaking changes to how you configure the `doc_generator.py` tool. For how to restructure your existing configuration files, see [Changes in Doc Generator V3](CHANGES_v2_to_v3.md). The `README` files have also been updated. A snapshot of the *version 2* code is available as the `Doc Generator v2` release.

## About

The `doc_generator.py` tool is a Python tool that parses and generates documentation in a specified output format from a set of JSON Schema files. Typically, the tool processes an entire set of files for a version. 

GitHub-flavored Markdown targeted for the [Slate API docs generator](https://github.com/slatedocs/slate "https://github.com/slatedocs/slate") is the default output.

Other output formats include:

* Markdown tuned to the DMTF document publication process
* HTML 
* *Property index* documentation
* CSV

## Installation

See [Installation](https://github.com/DMTF/Redfish-Tools/blob/master#installation "https://github.com/DMTF/Redfish-Tools/blob/master#installation").

1. Install the following required software on the machine from which you will run `doc_generator.py`:

    | Software | Description | Download |
    |----------|-------------|----------|
    | Python 3 | If you have not already installed Python, install only the standard library for Markdown output. | [https://www.python.org/downloads/](https://www.python.org/downloads/) |
    | Python&#8209;Markdown | Required for HTML output. | [https://python-markdown.github.io/install/](https://python-markdown.github.io/install/) |
    | Pygments | Required for HTML output. | [http://pygments.org/](http://pygments.org/) |

1. Use `pip` to install requirements:

    ```
    % cd doc-generator
    % pip install -r requirements.txt
    ```

1. If you are making changes to this code, also install pytest and run the tests. To use `pip` to install:

    ```
    % cd doc-generator
    % pip install -r dev_requirements.txt
    ```

    To run the tests:

    ```
    % cd doc-generator
    % pytest
    ```

## Usage

By default, `doc_generator.py` looks for a `json-schema` directory and supplemental files in the configuration file that you specify when you run it. Several flavors of configuration files are available.

The `--config` option specifies the configuration file.

This file defines:

* Many command-line options
* Some required parameters, such as URI mappings, that you cannot specify on the command line
* Many optional parameters

See [Redfish documentation generator config files](README_config_files.md).

```
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
   python3 ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/subset/config.json
```

For more examples, [Redfish documentation generator config files](README_config_files.md)

## Notes

For information about property index mode, see [Property Index Mode](README_Property_Index.md).

Normative output prefers long descriptions to descriptions.

For Slate, place the `index.html.md` output in your Slate repository's source directory.
