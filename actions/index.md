---
title: Actions
files:
  - name: echo.yaml
    type: yaml
  - name: check-bash-version.yaml
    type: yaml
  - name: check-bash-version.sh
    type: bash
  - name: check-python-version.yaml
    type: yaml
  - name: check-python-version.py
    type: python
  - name: check-node-version.yaml
    type: yaml
  - name: check-node-version.js
    type: js
youtube_id: 6ZlErpWUCv4
---

# {{ page.title }} #

{% include youtube.html id=page.youtube_id %}

{:.next-link}
Next: [Workflows](workflows/index.md)

{:.after-playlist-links}
# Commands #

* `st2 action list --pack=tutorials`
* `st2 action get tutorials.echo`
* `st2 run tutorials.echo message="Hello world"`
* `st2 action get tutorials.check-bash-version`
* `st2 run tutorials.check-bash-version major=true minor=true`
* `st2 run tutorials.check-bash-version`
* `st2 action get tutorials.check-python-version`
* `st2 run tutorials.check-python-version`
* `st2 run tutorials.check-python-version major=true minor=true`
* `st2 run tutorials.check-python-version major=true`
* `st2 action get tutorials.check-node-version`
* `st2 run tutorials.check-node-version`
* `st2 run tutorials.check-node-version major=true`
* `st2 run tutorials.check-node-version major=true minor=true`
* `nano actions/check-bash-version.yaml actions/check-python-version.yaml actions/check-node-version.yaml`

# Notes/Errata #

* We do not delve into action runners in this tutorial. That will be covered in a future tutorial. However, see the [Advanced Actions](actions/advanced.md) tutorial for actions run with more advanced runners, especially Python scripts!
* Running Python scripts with the `local-shell-script` runner is regarded as an anti-pattern. Please use the `python-script` runner from the [Advanced Actions tutorial](actions/advanced.md) to run Python scripts.
* In the video, you may not be able to see the "Logout" button in the user menu of the Workflow Composer. This is because the menu has the same background color as the toolbar, so it blends in. You should be able to see it on your screen.

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

Today's tutorial is on Actions.

To start off, I'm going to list all of the actions in the tutorials pack.

I'm going to run the ST2 command to list all of the actions, and limit it to the tutorials pack.

Now the first action we're going to look at today is the `echo` action.

To take a look at that I execute `st2 action get tutorials.echo`.

This tells me some interesting information about the `echo` action: it belongs to the tutorials pack, there's a short description of it, it uses the `local-shell-cmd` runner, and it takes a message parameter.

The message parameter is the most important part of this; this `required` option indicates to me that I have to pass it into the action itself, and it has to be a string.

The description of it is simply the message that the echo command will actually echo.

The `local-shell-cmd` runner will simply run the echo command on the StackStorm server itself.

If you don't know what an action runner is yet, don't worry - we'll cover that in a future tutorial. For now, just know that it tells StackStorm what type of action it is.

In order to run this, all I have to do is use the `st2` command to run it.

Here, StackStorm ran the command on the StackStorm server itself, the parameters that I passed in were "Hello world", and the result is that it succeeded, and the standard out of that command was "Hello world".

The next action I want to talk about is the `check-bash-version` action, so we'll take a look at that.

This action is slightly more complex than the last `echo` action. It uses a different runner - it uses the `local-shell-script` runner, that runner accepts an `entry_point` parameter and for this runner it's just the name of the shell script that we want to run. The shell script takes two boolean flags: `major` and `minor`, we can pass those in and we'll run it with the `major` and the `minor` flags.

As you can see, from the standard out, it printed "4.3", that means the StackStorm server is running Bash 4.3. But we don't necessarily have to pass in either parameter.

Let's see what happens when we don't.

In this case, when you don't pass in any flags, the script prints out the entire version string.

There are two other similar actions that we can take a look at: the first one is the `check-python-version` action.

This action is very similar to the `check-bash-version` action, except with this one the `entry_point` is different - instead of being a Bash script, it calls a Python script. But notice the parameters are very similar: it takes a `minor` and a `major` parameter, and both are booleans.

To call this action, it would be very similar to the last one.

And again, when I don't pass in the `major` or `minor` parameters, it gives me the full version string of the installed version of Python.

Similar to the `check-bash-version` action, I can pass in the `major` and `minor` flags to the action.

I can also just pass in _one_ of the flags.

The other action we can take a look at is the `check-node-version` action.
This, again, is very similar, but instead it runs a Node script. And this Node script accepts the same parameters: `major` and `minor`.

That gives us the full Node version.
And with that we can also pass one or both of the `major` and `minor` flags.

Now at this point, you're probably asking "how are actions defined"?
Let's take a look.

I'm currently in the tutorials pack and all of the actions we just ran are right here.
Let's dig into them.

This action, the `check-bash-version` action, is defined in this YAML file.
It specifies the runner, and it specifies the `entry_point` to use. It also specifies all of the parameters, and the `check-python-version` action is going to be very similar.

Here we see it's using the same runner, but it's `entry_point` is different - exactly like what we saw before - and the `check-node-version` action is going to be the exact same as well.

Another way to run actions is to use the web interface.
Once it's loaded in your web browser, you can go to the "Actions" tab, and go to the tutorials pack.
There we see all of the actions available to us, and one of them is the `check-python-version` action.

This is a list of all of the options that can be passed to the action - you'll notice the boolean `major` and `minor` flags that we saw in the action metadata file.
If we wanted to get the major and minor versions of Python installed on the StackStorm host, we would select both of those and click "Run".

StackStorm schedules the actions to run, so once we go into "Execution History", we can see here that the `check-python` task has run and it has output "2.7".
