[![Build Status](https://travis-ci.com/DMTF/Redfish-Tools.svg?branch=master)](https://travis-ci.com/github/DMTF/Redfish-Tools)
<p align="center">
  <img src="http://redfish.dmtf.org/sites/all/themes/dmtf2015/images/dmtf-redfish-logo.png" alt="DMTF Redfish" width=180>

# Redfish doc generator: Examples

Copyright 2016-2021 Distributed Management Task Force, Inc. All rights reserved.

Several files in the `sample_inputs` directory provide examples of configuration files that you can use to produce different types of documentation. The following examples show some command&#8209;line invocations.

> **Notes:** 
>
> * These examples assume that you have a clone of the `DMTF/Redfish` repo and the `DMTF/Redfish-Tools` repositories in the same parent directory, and that your working directory is the `Redfish` clone, so that the schemas are in `./json-schema` and `doc_generator.py` is at `../Redfish-Tools/doc-generator/doc_generator.py` relative to your current working directory.
> * The configuration files reference other files in this directory.

## Contents

* [CSV format](#csv-format)
* [Standard mode in HTML format](#standard-mode-in-html-format)
* [Standard normative mode in HTML format](#standard-normative-mode-in-html-format)
* [Terse profile mode in Markdown format](#terse-profile-mode-in-markdown-format)
* [Schema subset mode in HTML format](#schema-subset-mode-in-html-format)
* [Property-index mode in HTML format](#property-index-mode-in-html-format)

## CSV format

**Not implemented**

**Base configuration file:** <a href="sample_inputs/csv/config.json"><code>sample_inputs/csv/config.json</code></a>

```zsh
% cd Redfish
% python3 ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/csv/config.json
```

## Standard mode in HTML format

**Base configuration file:** <a href="sample_inputs/standard_html/config.json"><code>sample_inputs/standard_html/config.json</code></a>

```zsh
% cd Redfish
% python3 ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/standard_html/config.json
```

Note that the `object_reference_disposition` in this config file identifies specific behavior for the `Redundancy` resource and for `PCIeInterface`, defined in `PCIeDevice`.

## Standard normative mode in HTML format

**Base configuration file:** <a href="sample_inputs/standard_html/config_normative.json"><code>sample_inputs/standard_html/config_normative.json</code></a>

```zsh
% cd Redfish
% python3 ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/standard_html/config_normative.json
```

## Terse profile mode in Markdown format

**Base configuration file:** <a href="sample_inputs/profile_mode/config.json"><code>sample_inputs/profile_mode/config.json</code></a>

```zsh
% cd Redfish
% python3 ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/profile_mode/config.json
```

Configuration file references the profile `OCPBasicServer.v1_0_0.json`, which in turn references `OCPManagedDevice.v1_0_0.json`.

## Schema subset mode in HTML format

**Base configuration file:** <a href="sample_inputs/subset/config.json"><code>sample_inputs/subset/config.json</code></a>

```zsh
% cd Redfish
% python3 ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/subset/config.json
```

Configuration file references the profile `OCPBasicServer.v1_0_0.json`, which in turn references `OCPManagedDevice.v1_0_0.json`.

## Property-index mode in HTML format

**Base configuration file:** <a href="sample_inputs/property_index/config.json"><code>sample_inputs/property_index/config.json</code></a>

```zsh
% cd Redfish
% python3 ../Redfish-Tools/doc-generator/doc_generator.py --config=../Redfish-Tools/doc-generator/sample_inputs/property_index/config.json
```

> **Note:** The base configuration file for property index output includes the `description_overrides` key, which is specific to that mode.
