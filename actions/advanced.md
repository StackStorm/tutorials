---
title: Advanced Actions
files:
  - name: remote-echo.yaml
    type: yaml
  - name: check-remote-bash-version.yaml
    type: yaml
  - name: check-python-version-script.yaml
    type: yaml
  - name: check-python-version-script.py
    type: python
  - name: get-todo-json.yaml
    type: yaml
examples:
  - name: forloop_chain.yaml
    available_on: GitHub
    repository_url: https://github.com/stackstorm/st2
    url: https://github.com/stackstorm/st2/tree/master/contrib/examples/actions/chains/forloop_chain.yaml
youtube_id: o-LkF5eTYyg
---

# {{ page.title }} #

{% include youtube.html id=page.youtube_id %}

{:.previous-link}
Previous: [Workflows](workflows/index.md)

{:.next-link}
Next: [StackStorm Exchange](../exchange.md)

{:.after-playlist-links}
# Commands #

* `nano actions/check-bash-version.yaml actions/check-python-version.yaml actions/check-node-version.yaml`
* `nano actions/remote-echo.yaml`
* `st2 action get tutorials.remote-echo`
* `st2 run tutorials.remote-echo message='Hello World!' hosts=st2tutorials`
* `st2 run tutorials.remote-echo message='Hello World!' hosts=st2tutorials,localhost`
* `nano actions/check-remote-bash-version.yaml`
* `st2 run tutorials.check-remote-bash-version hosts=st2tutorials,localhost`
* `nano actions/check-python-version-script.yaml`
* `nano actions/check-python-version-script.py`
* `st2 run tutorials.check-python-version-script`
* `st2 run tutorials.check-python-version`
* `nano actions/get-todo-json.yaml`
* `curl https://jsonplaceholder.typicode.com/todos/1`
* `st2 run tutorials.get-todo-json`


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

{% if page.examples %}
# Examples #

{% for example in page.examples %}
{: id="{{ example.name }}" }
<a href="{{ example.url }}">`{{ example.name }}`</a>{% if example.available_on %} - Available on <a href="{{ example.repository_url }}">{{ example.available_on }}</a>{% endif %}
{% endfor %}
{% endif page.examples %}

{% if page.files %}
# Files #

{% for file in page.files %}
{: id="{{ file.name }}" }
`{{ file.name }}`

```{{ file.type }}
{% include_relative {{ file.name }} %}
```
{% endfor %}
{% endif page.files %}

# Questions, Comments, and Corrections #

Open an [issue](https://github.com/stackstorm/tutorials/issues) or submit a [pull request](https://github.com/stackstorm/tutorials/pulls).

# Transcript #

Hi everybody and welcome to StackStorm tutorials!

This tutorial is on Advanced Actions.

In the last tutorial, we went over a few different actions.
Each action called a different type of script, we called a Bash script, a Python script, and a Node.js script.

All of those scripts ran on the StackStorm server itself.

In this tutorial, we'll learn how to call scripts on remote machines.
We'll also learn how to call Python scripts directly, and we'll learn how to send out an HTTP request.

To get started, let's take a look at the actions we defined last time.

For the `echo` action, we used the `local-shell-cmd` runner. For the other three actions, we used the `local-shell-script` runner, but the `entry_point` for each was a different script.

For the `check-bash-version` action we called the `check-bash-version.sh` script; the Python and Node actions also used the `local-shell-script` runner, with slightly different entry points.

All of the scripts ran on the StackStorm server itself.

However, StackStorm can also run scripts on remote systems. Let's take a look at one.

This action uses a slightly different runner - it uses the `remote-shell-cmd` runner.
Let's take a look at it.
The `remote-echo` action takes the same parameters as the `echo` action, but the `remote-shell-cmd` runner itself takes an extra `hosts` parameter.
Let's see that in action.

Here, the remote echo action takes the same message parameter as before, but the command was run on the `st2tutorials` host.
We can also run the same command on two different hosts.
Here I'm running the action on both the `st2tutorials` host and `localhost`.
I'm specifying their hostnames as a comma-separated list.

The command is run twice - first, it's run on localhost, and second, it's run on st2tutorials.
In both cases, the standard out was "Hello World!" as expected, the action succeeded, and standard error was empty.

Next let's take a look at running a script on a remote system.

This action, the `check-remote-bash-version` action, checks the version of Bash on a remote host.
It uses the `remote-shell-script` runner, and has the same `entry_point` as the `check-bash-version-script`.
This runner also takes a `hosts` parameter.
Let's see it in action.

This action has run the same Bash script on two different hosts: the `st2tutorials` host and `localhost`.
In both cases, it succeeded, and the standard out was the same.

StackStorm can also run Python scripts directly with the `python-script` runner.
Let's take a look at an action that uses the `python-script` runner.

This action is the exact same as the `check-python-version` action from the previous tutorial, with two differences: this action uses the `python-script` runner instead of the `local-shell-script` runner. The `entry_point` is also a slightly different Python script.
Let's take a look at that.

This Python script is specific to StackStorm, because it imports directly from `st2common`.
It defines a `get_version_string` function that accepts `major`, `minor`, and `micro` parameters.
Similar to the action from the previous tutorial, it creates a version string, but instead of printing it to standard out, this function simply returns it.
The script then defines a subclass of `Action`.
That class's `run` function accepts `major` and `minor` parameters, and passes them to the `get_version_string` function that we defined before.
The `run` function simply returns a dictionary of the `version`, `major`, `minor`, and `micro` keys.
Let's see how that's different than the `local-shell-script` runner.

As you can see, the result that was returned from the `run` function contains `version`, `major`, `minor`, and `micro` keys.
Let's compare that to the result of the action from the previous tutorial.

The previous action printed the version string to its standard out.
StackStorm can capture the standard out from any shell script, but for Python scripts, it can capture the entire Python return value.
