---
title: Workflows With Mistral
files:
  - name: gather-versions.yaml
    type: yaml
  - name: gather-node-versions.yaml
    type: yaml
---

# Workflows With Orquesta #

[![StackStorm Workflows](https://img.youtube.com/vi/g4D_iFUXlEA/0.jpg)](https://www.youtube.com/watch?v=g4D_iFUXlEA)

[Previous tutorial](../index.md) [Next tutorial](https://docs.stackstorm.com)

# Steps #

In a terminal, run the following:

* `st2 action list`

<!--
# Notes/Errata #

* The 
-->
<!--
# Known Bugs #

* The `--json` flag to the `st2` command is supposed to print the results in JSON format, however the command prints the results in JSON format and then prints the results in the normal table format.

# Troubleshooting Tips and Workarounds #

* If you get stuck on part A, refresh the page. The pack list occasionally gets out of date.
-->

# Files #

{% for file in page.files %}
`{{ file.name }}`

```{{ file.type }}
{% include_relative {{ file.name }} %}
```
{% endfor %}

# Questions, Comments, and Corrections #

Open an [issue](https://github.com/stackstorm/tutorials/issues) or submit a pull request.
