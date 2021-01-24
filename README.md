[![Build Status](https://travis-ci.com/DMTF/Redfish-Tools.svg?branch=master)](https://travis-ci.com/github/DMTF/Redfish-Tools)
<p align="center">
  <img src="http://redfish.dmtf.org/sites/all/themes/dmtf2015/images/dmtf-redfish-logo.png" alt="DMTF Redfish" width=180>

# Redfish-Tools

The Redfish-Tools public repository contains the DMTF Scalable Platforms Management Forum (SPMF) tools.

For Redfish developer information, see DMTF at [https://redfish.dmtf.org/](https://redfish.dmtf.org/ "https://redfish.dmtf.org/").

* [Installation](#installation)
* [Tools](#tools)

## Installation

1. (All tools) Clone the `Redfish-Tools` repository:
   ```bash
   % git clone git@github.com:DMTF/Redfish-Tools.git
   % git remote add upstream git@github.com:DMTF/Redfish-Tools.git
   ```
1. (All tools) [Download and install Python](https://www.python.org/downloads/ "https://www.python.org/downloads/") on the machine from which you will run the tools.
1. (JSON Schema-to-OpenAPI converter only) Install YAML for Python:
    ```bash
    % pip install pyyaml
    ```
1. (Redfish doc generator only) Install the following software, which is required for HTML output:
   * [Install Python‑Markdown](https://python-markdown.github.io/install/ "https://python-markdown.github.io/install/").
   * [Install Pygments](http://pygments.org/ "http://pygments.org/").
   * Install requirements:
      ```bash
      % cd doc-generator
      % pip install -r requirements.txt
      ```
1. (Optional) To make changes to the `doc_generator.py` code, install [`pytest`](https://docs.pytest.org/en/latest/getting-started.html "https://docs.pytest.org/en/latest/getting-started.html"):

    ```bash
    % cd doc-generator
    % pip install -r dev_requirements.txt
    ```

## Tools

* [CSDL-to-JSON converter](csdl-to-json-convertor/README.md "csdl-to-json-convertor/README.md")
* [Redfish doc generator](doc-generator/README.md "doc-generator/README.md")
* [JSON Schema-to-OpenAPI converter](json-to-openapi-converter/README.md "json-to-openapi-converter/README.md")
* [OData CSDL validator](odata-csdl-validator/README.md "odata-csdl-validator/README.md")
