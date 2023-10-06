c# NetBot

#### Video Demo: https://youtu.be/ApMbifm5UH0

## Description
NetBot is my final project for CS50 Python. It uses [Slack Bolt](https://slack.dev/bolt-python/tutorial/getting-started) to create a socket that listens for Slack messages. The application will read the Slack message and respond accordingly.to execute commands on network devices. The link above goes through all steps necessary on the Slack website and Python.

### Files and functions

#### hosts.yml
* Dictionary of routers the netbot can log into. Includes device FQDN and platform so Netmiko can interact with the devices properly.

#### project.py
* imports:
    - Imports `os` for reading environment variables used for API tokens and network device credentials.
    - Imports `logging` for getting helpful log messages on errors once the bolt application is running.
    - Imports `slack_bolt` classes to run the web client that establishes a socket with Slack to receive messages and respond based on the message text.
    - Imports `safe_load` from `yaml` to create dicts based on contents of `hosts.yml`.
    - Imports `NetBot` class to instantiate it for getting responses to send back to slack.
* Functions/class instances:
    - Create instance of slack_bolt App for establishing connection to Slack.
    - `@app.message` decorator is used throughout the file to execute the function underneath when the slack message text contains the string passed as a parameter.
    - `message_debug` executes in response to a Slack message containing the string "netbot debug". It converts the message dict received by the application and converts it into plain text for posting into the Slack chat.
    - `message_help` executes in response to a Slack message containing the string "netbot help". It instantiates NetBot without passing any instance attributes. NetBot returns the message text that the application will post to Slack.
    - `send_device_output` executes in response to a Slack message containing the string "netbot get". It calls the function `get_command_and_device` to get a command string and device dict based on the contents of the Slack message text. It then instantiates NetBot, passing the command and the device as instance variables, so NetBot can send a command to the device indicated and return the output.
    - `get_command_and_device` takes the Slack message text and separates it into vars `command` and `device_key` using ` device=` as a delimiter. If the delimeter is not present, it returns `None` as the values for `command` and `device`. If the delimeter is present, it keeps the `command` variable and calls `get_device_dict` with `device_key` as a parameter to receive the device dict if the string corresponds to a device in the inventory or `None` if it doesn't. The function will then return the `command` string and `device` dict for use in instantiating `NetBot`.
    - `get_device_dict` Reads `hosts.yml` as a list of dicts, adding environment variables `NTWK_USERNAME` and `NTWK_PASSWORD` to the dicts within the list for use as login credentials. It then assigns the device dicts in the list as values in another dict with keys corresponding to the values expected to be passed as the `device` parameter. If a key in `devices` corresponds to the `device` parameter, the function returns the device dict corresponding to that key. If an invalid device key was passed (including an empty string or a None type), the function returns `None`.
    - `mock_message_debug`, `mock_message_help`, and `mock_send_device_output` are functions corresponding to `message_debug`, `message_help`, and `send_device_output`, respectively, for use in unit testing in lieu of testing the decorated functions.

#### netbot.py
* Imports `ConnectHandler` from `netmiko` for logging into network devices, sending commands, and returning the results.
* `HELP_TEXT` property provides the help text containing the valid syntax for commands and devices, as well as the current devices that can be indicated.
* `__init__` instantiates the class with optional `command` and `device` parameters for use as instance attributes. Those parameters are not required when NetBot is instantiated to provide the help text.
* `send_help_info` returns a string containing the class attribute `HELP_TEXT` so users know what commands NetBot will respond to.
* `get_output` expects `self.command` and `self.device` to be set to valid values. If an invalid device was passed (an empty string or `None` type), the method returns an error message with helpful text. If a valid device is set, the method evaluates the command passed in the Slack message to choose a command to send to the network device. If no valid command was passed, the method will return an error message with helpful text. If a valid command and device were passed, the method will use `ConnectHandler` to attempt to connect to the device and get command output. The method will then return the command output, or an error message if an exception is thrown by `ConnectHandler`.

#### test_project.py
* Contains functions for use with `pytest`. __It currently tests only the functions without decorators, as the decorator functions require the web server to be running.__ In lieu of testing the decorator functions, mock functions were created for testing omitting `say` and instead returning a string.

### Requirements
* Slack application (bot) with appropriate permissions as per [Slack Bolt](https://slack.dev/bolt-python/tutorial/getting-started).
* Setting the following environment variables:
    * `NTWK_USERNAME="..."`
    * `NTWK_PASSWORD="..."`
    * `SLACK_APP_TOKEN="xapp..."`
    * `SLACK_BOT_TOKEN="xoxb..."`
* I am using [eve-ng](https://www.eve-ng.net/) to run virtual routers that receive the commands. You can adapt the program to instead run commands on Linux VMs in your own network or a cloud provider.