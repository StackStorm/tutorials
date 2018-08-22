---
title: Rules
files:
  - name: webhook-echo.yaml
    type: yaml
youtube_id: LWA17q5LA3Q
---

# {{ page.title }} #

{% include youtube.html id=page.youtube_id %}

{:.previous-link}
Previous: [StackStorm Exchange](../exchange.md)

{:.after-playlist-links}
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

# Transcript #

Hi everybody and welcome to StackStorm tutorials!

In this tutorial, we'll be learning about rules.

StackStorm rules map triggers to actions or workflows by applying criteria to match trigger payloads to action inputs.

Let's take at one rule, now.

This is the `webhook-echo` rule.

It belongs to the `tutorials` pack, it has a simple description, and it is enabled.

The trigger it uses is the `core.st2.webhook` trigger and the URL is the `tutorials` URL.
The endpoint that StackStorm will use for the webhook is `/api/v1/webhooks/tutorials`.

The criteria is where incoming webhooks are filtered.

In this rule, the `name` attribute of the trigger body is filtered by an `equals` operator, with the pattern `Rules`.
That means if the body `name` equals `Rules`, the action will be run.
If the body `name` does not equal `Rules`, the action will not be run.

The action that is run from this rule is the `core.echo` action, and it is passed all of the data from the trigger.
This includes the trigger headers, as well as the trigger body.

Let's see a rule in action now.

Here, I can list all of the rules with the `st2 rule list` command.

I can also view the `webhook-echo` rule by running `st2 rule get tutorials.webhook-echo`.

Before I fire off a webhook to StackStorm, I need to get an API key.
I do this with the `st2 apikey create` command, and I pass it the `--only-key` flag so that it only prints the API key itself.
Now that we have an API key, I can use the `http` command from the `httpie` package, to fire off an HTTP POST to the `/api/v1/webhooks/tutorials` endpoint.
I use the value of that API key as the `St2-Api-Key` HTTP header and I pass in the value `Something` for the `name` key.
This gets POSTed as JSON.

Here, the HTTP response code is 202, which means that StackStorm has accepted the webhook.

If we check to see if there are any executions, there are no executions.
This is because the rule criteria does not match the data I passed in.

If I do pass in data that matches the rule criteria, in other words, if I pass in `Rules` as the value for the `name` key, the POST is again accepted and we can see that an execution has happened.
Let's view the execution in the web UI.

Here we see that `core.echo` was only executed once, and it was triggered by the `webhook-echo` rule that we configured before.
The trigger data that we echoed contains both the trigger `body` and all of the HTTP headers that were passed to StackStorm.

To see the rule in the web UI, I would go to the `Rules` tab, go to the `Tutorials` pack, and click on the `webhook-echo` rule.
The web UI contains all of the information about the rule from the YAML file we defined earlier.
We can also edit the rule itself, by clicking the `Edit` button.

Here, instead of passing all of the trigger data into the `core.echo` action, we will pass in the `trigger.body`.
That will pass the trigger body directly, and will not pass in any of the trigger headers.

I click `Save` and then I go to the terminal to fire it off again.

Now we can see that there are two executions of `core.echo`.
Let's go to the web UI to view them.

This second execution of `core.echo` was again triggered by the `webhook-echo` rule, but the data that was passed to the `echo` action only contains the trigger body.

To troubleshoot rules, it can be helpful to view all of the trigger instances for a particular rule, whether or not they have matched the rule criteria.
To view this, go to the `Triggers` tab in the web UI, scroll down to the `st2.webhook` trigger in the left column, then go to the `Instances` tab in the right pane.

Here is a list of all of the trigger instances that StackStorm has processed, whether or not they have matched the rule criteria.

Trigger instances can also be created by sensors, which we will cover in another tutorial.
