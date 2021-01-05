[![Build Status](https://travis-ci.com/DMTF/Redfish-Tools.svg?branch=master)](https://travis-ci.com/github/DMTF/Redfish-Tools)
<p align="center">
  <img src="http://redfish.dmtf.org/sites/all/themes/dmtf2015/images/dmtf-redfish-logo.png" alt="DMTF Redfish" width=180>
</p>

# Redfish-Tools

**Redfish-Tools** is the public repository of tools released by the Scalable Platforms Management Forum (SPMF) of the DMTF. For Redfish developer information, see [DMTF](https://redfish.dmtf.org/ "https://redfish.dmtf.org/").

## Installation

To use any of the tools in this repository:

1. Clone the `Redfish-Tools` repository:

    ```
    git clone git@github.com:DMTF/Redfish-Tools.git
    git remote add upstream git@github.com:DMTF/Redfish-Tools.git
    ```

1. Install Python on the machine from which you will run the tools:

    | Software | Download                             |
    | :------- | :----------------------------------- |
    | Python 3 | [https://www.python.org/downloads/](https://www.python.org/downloads/) |

## Tools

 * **CSDL-to-JSON converter**: [`csdl-to-json.py`](https://github.com/DMTF/Redfish-Tools/blob/master/csdl-to-json-convertor/README.md "https://github.com/DMTF/Redfish-Tools/blob/master/csdl-to-json-convertor/README.md")
 * **Redfish documentation generator**: [`doc_generator.py`](https://github.com/DMTF/Redfish-Tools/blob/master/doc-generator/README.md "https://github.com/DMTF/Redfish-Tools/blob/master/doc-generator/README.md")
 * **JSON Schema-to-OpenAPI converter**: [`json-to-yaml.py`](https://github.com/DMTF/Redfish-Tools/blob/master/json-to-openapi-converter/README.md "https://github.com/DMTF/Redfish-Tools/blob/master/doc-generator/README.md")
 * **OData CSDL validator**: [`odata_validator.py`](https://github.com/DMTF/Redfish-Tools/blob/master/odata-csdl-validator/README.md "https://github.com/DMTF/Redfish-Tools/blob/master/doc-generator/README.md")
