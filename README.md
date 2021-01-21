[![Build Status](https://travis-ci.com/DMTF/Redfish-Tools.svg?branch=master)](https://travis-ci.com/github/DMTF/Redfish-Tools)
<p align="center">
  <img src="http://redfish.dmtf.org/sites/all/themes/dmtf2015/images/dmtf-redfish-logo.png" alt="DMTF Redfish" width=180>

# Redfish-Tools

The Redfish-Tools public repository contains the DMTF Scalable Platforms Management Forum (SPMF) tools.

For Redfish developer information, see [DMTF](https://redfish.dmtf.org/ "https://redfish.dmtf.org/").

## Tools

* [CSDL-to-JSON converter](csdl-to-json-convertor/README.md "csdl-to-json-convertor/README.md")
* [Redfish doc generator](doc-generator/README.md "doc-generator/README.md")
* [JSON Schema-to-OpenAPI converter](json-to-openapi-converter/README.md "json-to-openapi-converter/README.md")
* [OData CSDL validator](odata-csdl-validator/README.md "odata-csdl-validator/README.md")

## Installation

To install the tools in the Redfish-Tools respository:

<ol>
   <li>
      <p>Clone the <code>Redfish-Tools</code> repository:</p>
      <pre lang="bash">% git clone git@github.com:DMTF/Redfish-Tools.git
% git remote add upstream git@github.com:DMTF/Redfish-Tools.git</pre>
   </li>
   <li>
      <p><a href="https://www.python.org/downloads/" title="https://www.python.org/downloads/">Download and install Python</a> on the machine from which you will run the tools.</p>
   </li>
</ol>

For the Redfish doc generator only, complete these additional steps:

<ol>
   <li>
      <p>Install the following software, which is required for HTML output:</p>
      <ul>
         <li><a href="https://python-markdown.github.io/install/" title="https://python-markdown.github.io/install/">Install Python&#8209;Markdown</a>.</li>
         <li><a href="http://pygments.org/" title="http://pygments.org/">Install Pygments</a>.</li>
         <li>Install requirements:
            <pre lang="bash">% cd doc-generator
% pip install -r requirements.txt</pre>
         </li>
      </ul>
   </li>
   <li>
      <p>(Optional) If you plan to make changes to the <code>doc_generator.py</code> code:</p>
      <ul>
         <li>To install <a href="https://docs.pytest.org/en/latest/getting-started.html" title="https://docs.pytest.org/en/latest/getting-started.html"><code>pytest</code></a>, run these commands:
            <pre lang="bash">% cd doc-generator
% pip install -r dev_requirements.txt</pre>
         </li>
         <li>Run the tests:
            <pre lang="bash">% cd doc-generator
% pytest</pre>
         </li>
      </ul>
   </li>
</ol>
