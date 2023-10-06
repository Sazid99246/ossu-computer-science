import os
import logging
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from yaml import safe_load
from netbot import NetBot


# Initialize slack app with bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# listen for debug request
@app.message("netbot debug")
def message_debug(message, say):
    """
    Converts the Slack message payload into a string
    and returns it as a string with code formatting.

    :param message: Slack message payload
    :param say: function included by slack_bolt library
    :return: Text containing debug message
    :rtype: str
    """

    debug_msg = ""
    for key, value in message.items():
        debug_msg = debug_msg + f"{key}: {value}\n"
    say(f"```\n{debug_msg}\n```")


# Listen to incoming messages that contain "netbot help"
@app.message("netbot help")
def message_help(message, say):
    """
    Instantiate NetBot and send help text to the channel
    when "netbot help" appears in a Slack message

    :param message: Slack message payload
    :param say: function included by slack_bolt library
    :return: No value; the function posts a message in Slack
    """

    # Create a new NetBot
    netbot = NetBot()

    # Return the help message text
    help_text = netbot.send_help_info()
    say(help_text)


# listen for message requesting device output
@app.message("netbot get")
def send_device_output(message, say):
    """
    Instantiate NetBot, get command output when
    "netbot get" appears in a Slack message,
    and send response to Slack.

    :param message: Slack message payload
    :param say: function included by slack_bolt library
    :return: No value; the function posts a message in Slack
    """

    # get command device dict from input
    command, device = get_command_and_device(message["text"])

    netbot = NetBot(command, device)

    # Get command output from device
    device_output = netbot.get_output()

    # Post output in Slack
    say(f"```\n{device_output}\n```")


def get_command_and_device(message):
    """
    Parses Slack message into the command and device.
    Calls get_device_dict() to get the device dict if
    the device exists.

    :param message: Slack message text
    :type message: str
    :return: command and device tuple or None, None tuple
    :rtype: (str,dict)
    """

    try:
        # split input into command and device
        command, device_key = message.strip().split(" device=")
    except ValueError:
        # No device found
        return None, None
    else:
        device = get_device_dict(device_key)
        return command, device


def get_device_dict(device=""):
    """
    Accepts a hostname and returns its dict of attr if the
    host exists in hosts.yml device dict. This dict is
    used for logging into the network device.

    :param device: Slack message text
    :type device: str
    :return: A dictionary of device attributes
    :rtype: dict
    """
    # Read hosts file into structured data
    with open("hosts.yml", encoding="utf-8") as file:
        hosts = safe_load(file)

    # Add credentials from env vars
    for host in hosts["host_list"]:
        host["username"] = os.environ.get("NTWK_USERNAME")
        host["password"] = os.environ.get("NTWK_PASSWORD")
    rt1, rt2 = hosts["host_list"]

    devices = {"rt1": rt1, "rt2": rt2}

    try:
        return devices[device]
    except KeyError:
        return None


def mock_message_debug(message):
    """
    mock function for testing functionality of message_debug
    which normally executes when the Slack message contains
    the string "netbot debug"

    :param message: mock Slack message payload dict
    :return: Text containing debug message
    :rtype: str
    """

    debug_msg = ""
    for key, value in message.items():
        debug_msg = debug_msg + f"{key}: {value}\n"
    return f"```\n{debug_msg}\n```"


def mock_message_help(message):
    """
    mock function for testing functionality of message_help
    which normally executes when the Slack message contains
    the string "netbot help"

    :param message: mock Slack message text
    :return: No value; the function posts a message in Slack
    """

    # Create a new NetBot
    netbot = NetBot()

    # Return the help message text
    help_text = netbot.send_help_info()
    return help_text


def mock_send_device_output(message):
    """
    mock function for testing functionality of send_device_output
    which normally executes when the Slack message contains
    the string "netbot get"

    :param message: mock Slack message text
    :return: No value; the function posts a message in Slack
    """

    # get command device dict from input
    command, device = get_command_and_device(message["text"])

    netbot = NetBot(command, device)

    # Get command output from device
    device_output = netbot.get_output()

    # Post output in Slack
    return f"```\n{device_output}\n```"


if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()