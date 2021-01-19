[![Build Status](https://travis-ci.com/DMTF/Redfish-Tools.svg?branch=master)](https://travis-ci.com/github/DMTF/Redfish-Tools)
<p align="center">
  <img src="http://redfish.dmtf.org/sites/all/themes/dmtf2015/images/dmtf-redfish-logo.png" alt="DMTF Redfish" width=180>
</p>

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

<table>
   <thead>
      <tr>
         <th align="left" valign="top">Tools</th>
         <th align="left" valign="top" colspan="2">Step</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td align="left" valign="top" rowspan="2">&checkmark;&nbsp;CSDL-to-JSON converter<br/>&checkmark;&nbsp;Redfish doc generator<br/>&checkmark;&nbsp;JSON&nbsp;Schema&#8209;to&#8209;OpenAPI&nbsp;converter<br/>&checkmark;&nbsp;OData CSDL validator</td>
         <td align="left" valign="top">1.</td>
         <td align="left" valign="top">
            Clone the <code>Redfish-Tools</code> repository:
            <pre lang="bash">% git clone git@github.com:DMTF/Redfish-Tools.git
% git remote add upstream git@github.com:DMTF/Redfish-Tools.git</pre>
         </td>
      </tr>
      <tr>
         <td align="left" valign="top">2.</td>
         <td align="left" valign="top">
            <a href="https://www.python.org/downloads/" title="https://www.python.org/downloads/">Download and install Python</a> on the machine from which you will run the tools.
         </td>
      </tr>
      <tr>
         <td align="left" valign="top" rowspan="2">&checkmark;&nbsp;Redfish doc generator</td>
         <td align="left" valign="top">3.</td>
         <td align="left" valign="top">
            Install the following software, which is required for HTML output:
            <ul>
               <li><a href="https://python-markdown.github.io/install/" title="https://python-markdown.github.io/install/">Install Python&#8209;Markdown</a>.</li>
               <li><a href="http://pygments.org/" title="http://pygments.org/">Install Pygments</a>.</li>
               <li>
                  Install requirements:
                  <pre lang="bash">% cd doc-generator
% pip install -r requirements.txt</pre></li>
         </td>
      </tr>
      <tr>
         <td align="left" valign="top">4.</td>
         <td align="left" valign="top">
            (Optional) If you plan to make changes to the <code>doc_generator.py</code> code:
            <ul>
               <li>Install <code>pytest</code>:
                  <pre lang="bash">% cd doc-generator
% pip install -r dev_requirements.txt</pre>
               </li>
               <li>
                  Run the tests:
                  <pre lang="bash">% cd doc-generator
% pytest</pre>
               </li>
            </ul>
            For information about <code>pytest</code>, see <a href="https://docs.pytest.org/en/latest/getting-started.html" title="https://docs.pytest.org/en/latest/getting-started.html">pytest</a>.
         </td>
      </tr>
   </tbody>
</table>
