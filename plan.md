# Basics for end users (even non-DevOps users) #

### Actions ###

* [x] How to run them individually from the web UI
* [x] How to run them from the `st2` command
* [x] How to create your own
  - [x] YAML description
* [x] Examples:
  - [x] `local-shell-script` with Bash
  - [x] `local-shell-script` with Python
  - [x] `local-shell-script` with Node


### Advanced Actions ###
* [ ] Show different runners
  - [x] `remote-shell-cmd`
  - [x] `remote-shell-script`
  - [x] `python-script`
  - [ ] `http-request` with GitHub API
* [ ] Dig into the check version scripts themselves
  - [ ] Python code


### StackStorm Exchange ###

* Quick overview
* How to install actions from Exchange
  - [x] Digging through all of the actions
  - [x] Show copy/pasting the install command (`st2 pack install ...`)
  - [x] Show list in WebUI
    + Now including the installed GitHub pack
  - [x] Go into installing packs from the WebUI


### Workflows ###

* [x] How to run them individually from the web UI
* [x] How to run with the `st2` command
* [x] How to create your own
  - [x] VERY quick overview
  - [x] ActionChain
  - [x] Mistral v2
  - [x] Orchestra/Orquesta
* What actions to do?
  - [x] Passing data between actions
    + [x] Mock REST API/service to pass data to and pull data from
    + [x] Don't get bogged down in what exactly the service does


### Rules ###

* Be careful about mentioning sensors or triggers (we haven't explained that yet)
* [ ] What exactly they are
  - [ ] Example: polling sensor from GitHub pack
    + Check if GitHub has a streaming/websocket option
    + Mention that you can use webhooks with GitHub or Jira on-prem
    + [ ] Dump each GitHub issue to a file?
  - Example: sensor/webhooks from Jira
    + Why you should use rules to filter sensor/webhook data from (for example) Jira instead of using the built-in Jira webhooks
* How to use common operators


### Packs ###

* Create your own
  - Content
* Pack structure
* "Integration" packs for external/internal services
  - Jira
  - Bitbucket
* "Automation" packs for internal groups or custom services
* Common internal packs
  - Security (every organization has its own risk profile and security posture)
  - Ops (different in every organization)
* Pack configuration
  - config.schema.yaml



# Individual Packs #

* Not every pack needs a video, but can target a select few popular, full featured, well written packs and do walkthroughs
  - Dig through list of available packs in st2web
  - Show how to review packs
    + Quickly scan through actions to get a sense of completeness
    + Any workflows? More are better
    + Any sensors? (possibly N/A)
* Jira
  - How to setup webhooks in ST2 instead of Jira
* Bitbucket or another VCS
  - Setup webhook on VCS server to push to StackStorm webhook
    + Associated rule redeploys StackStorm packs when the master branch of specific repositories are updated
* Slack
  - Perform management via API



# Format #

* Video should pair with a corresponding page
* Maybe use GitHub pages?
  - Seems like it would work well
  - Enables community engagement for individual pages:
    - Can open issues
    - Create pull requests
    - Ask questions
* Page title should match the video exactly
  - Helps discoverability/SEO
* List of page sections (sections can be omitted if blank):
  - Link to the video
  - Sections/steps from video
    + Copied and pasted verbatim (except for maybe passwords and secrets)
    + Helps discoverability/SEO
  - Files used in the video
    + The contents of a FEW (<3) small (<10 lines) files may be copied verbatim
    + Any larger files should be linked to
      * Should be able to use GitHub Gists so we don't have to host them ourselves
  - Notes/Errata
    + In particular, if the video is slightly out of date, we should make note of this and guide users to the up-to-date instructions
  - Known Bugs
    + Each step may have known bugs
  - Troubleshooting and Workarounds (should never be blank - always include it even if it's just blank, so users know )
    + Can document common errors, places where users get lost, confused, or things don't work as expected
    + Anything not covered in the video
      * Example:
        Issue: Slack responds with "invalid_token"
        Troubleshooting step: Ensure you are using the Bot User OAuth Access Token (NOT the OAuth Access Token), which you can access from the Authentication and Permissions section of your Slack workspace: https://<workspace_name>.slack.com/...
  - Link to the page on GitHub
    + Make it as easy as possible for users to engage
* Remember: a picture is with worth a thousand words, a video is worth a billion



# Advanced Topics #

### Using the `search` operator in rules ###


### Sensors and Triggers ###

* What they are
* Where you should use either one
  - Pull/poll based vs Push/event based
  - Example
    + multiple Jira sensors
      * slows down already slow Jira node/s!
    + vs
    + one Jira webhook
      * less load on Jira, multi-node/scalable!
* How to write one


### ChatOps ###

* Action aliases
* Video for setting up with every supported chat service
  - Setup with Slack
    + Which bot token to use?
      * OAuth Access Token
        - For ???
      * Bot User OAuth Access Token
        - For Slack bots (HUBOT_SLACK_TOKEN)
  - Setup with Mattermost
  - Setup with Rocketchat


### RBAC ###

* I don't know enough about this to do a video or anything, but it's definitely something we should cover
* Show off what a paid license will get you


### Authentication Backends ###

* LDAP (paid version)
  - Not community version



# Potential Hangups #

* Talk to Tomaz about the site to create gifs from terminal commands
* The content doesn't have to be kept completly up-to-date for every release
  - Small pieces that are out of date are acceptable
  - Users can stumble their way through small changes
  - We can note small changes in the notes section of video pages
* We don't have to go through an exhaustive or in-depth list of StackStorm features
  - Remember - this documentation is gonna be geared mostly towards people who aren't professional developers
