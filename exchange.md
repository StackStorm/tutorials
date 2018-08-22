---
title: StackStorm Exchange
files:
  # - name: rule.yaml
  #   type: yaml
youtube_id: fRVgHAgzoUI
---

# {{ page.title }} #

{% include youtube.html id=page.youtube_id %}

{:.previous-link}
Previous: [Advanced Actions](actions/advanced.md)

{:.next-link}
Next: [Rules](rules/index.md)

{:.after-playlist-links}
# Commands #

* `st2 pack search zabbix`
* `st2 pack search aws`
* `st2 pack search azure`
* `st2 pack install azure`
* `st2 pack list`
* `st2 action list --pack=azure`

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

# Transcript #

Hi everybody and welcome to StackStorm tutorials!

This tutorial in about StackStorm Exchange.

StackStorm Exchange is a GitHub organization of curated StackStorm packs, each in their own repository.
The StackStorm client makes it easy to search for and install packs from StackStorm Exchange.
All you have to do is use the `pack` subcommand of the `st2` command.

Here I'm searching for the zabbix pack.
I can also search for AWS, and Azure, and I can easily install packs with `st2 pack install azure`.

Now, when I list all of the packs, you can see that the Azure pack has been installed.

Pack installation runs as a StackStorm action.
To view its status, check the Execution History tab in the web UI.

Let's take a look at all of the actions in the Azure pack.

All of these actions are now available to any workflows I create.

You can also use the Exchange web interface at [exchange.stackstorm.org](https://exchange.stackstorm.org).

Here I'm going to search for the Azure pack.
This is the link to the pack's GitHub repository.
On GitHub you can find the documentation for the Azure pack by looking at the README.

These are the available actions in the Azure pack.
You can also list all of the available actions by looking into the code itself.

Another way to install StackStorm packs is through the Extreme Workflow Composer.
Go to the Packs tab, then go to the filter, type in part or all of what you are looking for.

Here I'm looking for the GitHub pack, so I select it on the left and click install.
I can then go view the execution in the History tab.
