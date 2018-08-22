---
title: Workflows
files:
  - name: gather-bash-versions.yaml
    type: yaml
  - name: gather-python-versions.yaml
    type: yaml
  - name: gather-node-versions.yaml
    type: yaml
  - name: gather-versions.yaml
    type: yaml
youtube_id: QnNGdlidatY
---

# {{ page.title }} #

{% include youtube.html id=page.youtube_id %}

{:.previous-link}
Previous: [Actions](../index.md)

{:.next-link}
Next: [Advanced Actions](../advanced.md)

{:.after-playlist-links}
# Commands #

In a terminal, run the following:

* `st2 action get tutorials.gather-bash-versions`
* `st2 action execute tutorials.gather-bash-versions component=bash`
* `st2 execution get <id>`
* `st2 action execute tutorials.gather-bash-versions component=bash mockable_demo=thisshouldnotexist`
* `st2 execution get <id>`
* `st2 action execute tutorials.gather-versions`
* `st2 execution get <id>`

# Notes/Errata #

* Orchestra is the old name for the Orquesta workflow engine
* Tasks in Orquesta workflows can be run in parallel - see the [Orquesta documentation]() for more information

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

# Transcript #

Hi everybody and welcome to StackStorm tutorials!

Today's tutorial is on workflows.

Workflows are actions that are chained together in a sequential order.
That means that they run one after another.

Running actions in parallel, or at the same time, will be covered in another tutorial.

There are three different workflow engines that StackStorm supports.

The first one is ActionChain.
ActionChain is very simple, but does not support advanced features like the other two engines do.

The second workflow engine is Mistral.
This workflow engine is from OpenStack, and is more flexible and complex than ActionChain.
It supports the use of YAQL and Jinja.

The last workflow engine that StackStorm supports is called Orquesta.
Note that, currently, Orquesta is in a technology preview or release candidate state, and is not yet stable.
A stable release of Orquesta will be released with StackStorm 3.0.

The first workflow is run by the Orquesta workflow engine.
The `entry_point` is simply another YAML file in the `workflows` directory, under the `actions` directory.
It takes two parameters: the `mockable_demo` parameter, which has a default value, and a `component` parameter.

The `gather-python-versions` workflow also uses the Orquesta workflow engine.
It also uses a different `entry_point`, but it accepts the same parameters.

The `gather-node-versions` workflow uses the Mistral workflow engine.
It has, again, a different `entry_point`, but accepts the same parameters.

Finally, the `gather-versions` workflow uses the ActionChain engine and has its own `entry_point` and only one parameter.
We'll see why in just a bit.
Let's take a look at one of those workflows.

This is the definition of the `gather-bash-versions` workflow.
Please refer to the Orquesta documentation for a full description of the workflow syntax.

The two interesting keys in this workflow are the `input` key and the `tasks` key.
The two input parameters to this workflow are `mockable_demo` and `component`, as we saw in the action metadata file from before.

These parameters are published into workflow context dictionaries, which will be referenced later on.

The value of the tasks key is an ordered dictionary of the tasks to run.

The first task is `check_bash_major_version`.
It runs the `check-bash-version` action from the `tutorials` pack, and passes in two parameters to the action: `major` and `minor`.
When the action is successful, it publishes the standard out from the action into the `major` key of its workflow context.
The next task it runs is `check_bash_minor_version`.
The `check_bash_minor_version` task runs the same `check-bash-version` action from the `tutorials` pack, but it passes in different values for the `major` and `minor` input parameters.
When the action is successful, it publishes the standard out of the script into the `minor` key of its workflow context.
Then the workflow runs the `report-bash-version` task, which sends out an HTTP POST request to a specified URL.
This URL is constructed using YAQL, Y-A-Q-L, which stands for Yet Another Query Language.
The YAQL part of this string is denoted by the angle bracket and percentage sign, and is closed by a matching percentage sign and angle bracket.
The subdomain that is used in the HTTP request is pulled from the `mockable_demo` key of its workflow context, which comes from the workflow input parameters.
This action adds a `content_type` HTTP header, and submits a JSON dictionary containing the `component`, `major`, and `minor` keys, again using YAQL to interpolate them into the JSON string itself.
After that, the workflow is done.

Let's take a look at the ActionChain workflow.

This workflow is run by the ActionChain workflow engine.
The first key in this YAML file is the `chain` key.
It specifies a list of tasks to run.
The first task is `gather_bash_versions` (with underscores), it runs the `gather-bash-versions` (with dashes) action from the `tutorials` pack, and passes in two parameters: the `mockable_demo` parameter and the `component` parameter.
The `mockable_demo` parameter uses a Jinja expression, designated by the two curly braces, to pass in the `mockable_demo` variable from the workflow input.
The `component` parameter is simply set to a literal string value.
For this task, the value of the `component` parameter is `bash`.

When the task is finished running, whether the action succeeded or failed, the workflow engine will transition to running the `gather_python_versions` task.

The `gather_python_versions` task is defined very similarly to the `gather_bash_versions` task.
It runs the `gather-python-versions` action from the `tutorials` pack, and uses the same value for the `mockable_demo` parameter.
The `component` parameter, however, is `python`, not `bash`, like it was in the `gather_bash_versions` task.

When this task is finished, again whether the action succeeded or failed, the workflow engine will then run the `gather_node_versions` task.

The `gather_node_versions` task runs the `gather-node-versions` action from the `tutorials` pack, and passes in the same `mockable_demo` parameter, with the same value as before.
This time, the value of the `component` parameter is `node.js`.

When this task is finished, if the action is successfully run, the workflow will run the `report_success` task.
If the action failed, the workflow will run the `generate_uuid` task.

The `report_success` task uses the `local` action from the `core` pack to run the `echo` command on the StackStorm server.
This example is a silly way to report success.
In production, some workflows post success messages to an instant messaging system, or send an email.
Other workflows may use an entirely different mechanism to report success, or may not report success at all.
It is up to the workflow author to decide how to handle reporting success.

If the `gather_node_versions` task fails, the workflow runs the `generate_uuid` task.
This task runs the `uuid` action from the `core` pack and passes in the `uuid_type` parameter with the value `uuid4`.
This generated UUID is not used anywhere.
Like the `report_success` task, this is a silly example.
In most workflows, the author will somehow report a test failure, either using an instant message system, by sending an email or an alert to a monitoring system, or some other mechanism to report failure.
Again, it is up to the workflow author to decide how to handle reporting a workflow failure.

The last important key in an ActionChain workflow definition is the `default` key.
The value of this key specifies which task to run first.
For this workflow, execution will start with the `gather_bash_versions` task.
