---
title: Advanced Rules
files:
  # - name: advanced.yaml
  #   type: yaml
---

# Actions #

[![StackStorm Advanced Rules](https://img.youtube.com/vi/g4D_iFUXlEA/0.jpg)](https://www.youtube.com/watch?v=g4D_iFUXlEA)

[Previous tutorial](https://docs.stackstorm.com) [Next tutorial](advanced.md)

# TODO #

* Lorem ipsum

# Commands #

* `st2 rule list`

<!--
# Notes/Errata #

* In the video, you may not be able to see the "Logout" button in the user menu of the Workflow Composer. This is because the menu has the same background color as the toolbar, so it blends in. You should be able to see it on your screen.
-->
<!--
# Known Bugs #

* The `--json` flag to the `st2` command is supposed to print the results in JSON format, however the command prints the results in JSON format and then prints the results in the normal table format.

# Troubleshooting Tips and Workarounds #

* If you get stuck on part A, refresh the page. The pack list occasionally gets out of date.
-->

# Files #

{% for file in page.files %}
{: id="{{ file.name }}" }
`{{ file.name }}`

```{{ file.type }}
{% include_relative {{ file.name }} %}
```
{% endfor %}

# Questions, Comments, and Corrections #

Open an [issue](https://github.com/stackstorm/tutorials/issues) or submit a [pull request](https://github.com/stackstorm/tutorials/pulls).
