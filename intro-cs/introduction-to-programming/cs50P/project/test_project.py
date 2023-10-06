import os
from project import (
    mock_message_debug,
    mock_message_help,
    mock_send_device_output,
    get_command_and_device,
    get_device_dict,
)
from netbot import NetBot


# set environment variables for logging into devices
os.environ["NTWK_USERNAME"] = "tester"
os.environ["NTWK_PASSWORD"] = "testerpw"


def test_mock_message_debug():
    message = {
        "client_msg_id": "02e747f5-6770-4fe4-80fe-c549dde1ca20",
        "type": "message",
        "text": "netbot debug",
        "user": "U046H2Q5JAK",
        "ts": "1666716633.386989",
        "blocks": [
            {
                "type": "rich_text",
                "block_id": "L7Li",
                "elements": [
                    {
                        "type": "rich_text_section",
                        "elements": [{"type": "text", "text": "netbot debug"}],
                    }
                ],
            }
        ],
        "team": "T046R0Z54TG",
        "channel": "C047A88DJC9",
        "event_ts": "1666716633.386989",
        "channel_type": "channel",
    }

    assert mock_message_debug(message) == (
        "```\n"
        "client_msg_id: 02e747f5-6770-4fe4-80fe-c549dde1ca20\n"
        "type: message\n"
        "text: netbot debug\n"
        "user: U046H2Q5JAK\n"
        "ts: 1666716633.386989\n"
        "blocks: [{'type': 'rich_text', 'block_id': 'L7Li', 'elements': [{'type': 'rich_text_section', 'elements': [{'type': 'text', 'text': 'netbot debug'}]}]}]\n"
        "team: T046R0Z54TG\n"
        "channel: C047A88DJC9\n"
        "event_ts: 1666716633.386989\n"
        "channel_type: channel\n\n"
        "```"
    )


def test_mock_message_help():
    # the msg text contents doesn't matter here
    # because it's parsed by the decorator
    assert mock_message_help("foo") == (
        "Here are the things you can ask me to do:\n\n"
        "```\n"
        "# get interface information\n"
        "netbot get interface info device=<device name>\n\n"
        "# get routes\n"
        "netbot get routes device=<device name>\n\n"
        "# get HSRP brief output\n"
        "netbot get hsrp device=<device name>\n"
        "```\n\n"
        "where devices are `rt1` and `rt2`"
    )


def test_mock_send_device_output_valid_device():
    message = {"text": "netbot get interface info device=rt1"}

    assert mock_send_device_output(message) == (
        "```\n"
        "Interface                  IP-Address      OK? Method Status                Protocol\n"
        "GigabitEthernet0/0         192.168.128.119 YES DHCP   up                    up      \n"
        "GigabitEthernet0/1         unassigned      YES NVRAM  up                    up      \n"
        "GigabitEthernet0/2         unassigned      YES NVRAM  up                    up      \n"
        "GigabitEthernet0/2.101     10.10.10.2      YES NVRAM  up                    up      \n"
        "GigabitEthernet0/2.102     10.20.10.2      YES NVRAM  up                    up      \n"
        "GigabitEthernet0/2.201     10.70.20.2      YES NVRAM  up                    up      \n"
        "GigabitEthernet0/2.202     10.80.20.2      YES NVRAM  up                    up      \n"
        "GigabitEthernet0/3         unassigned      YES NVRAM  administratively down down    \n"
        "```"
    )

def test_mock_send_device_output_invalid_device():
    message = {"text": "netbot get interface info device=rt3"}

    assert mock_send_device_output(message) == (
        '```\n'
        'Invalid device. Say "netbot help" for list of valid devices.\n'
        '```'
        )

def test_mock_send_device_output_invalid_command():
    message = {"text": "netbot get foo device=rt1"}

    assert mock_send_device_output(message) == (
        "```\n"
        "Command 'netbot get foo' is invalid or currently unsupported."
        "Say `netbot help` for list of valid commands.\n"
        "```"
        )


def test_get_device_dict_rt1():
    # Existing device
    assert get_device_dict("rt1") == {
        "host": "vios-rt1.jm",
        "device_type": "cisco_ios",
        "username": "tester",
        "password": "testerpw",
    }


def test_get_device_dict_rt2():
    # Existing device
    assert get_device_dict("rt2") == {
        "host": "vios-rt2.jm",
        "device_type": "cisco_ios",
        "username": "tester",
        "password": "testerpw",
    }


def test_get_device_dict_rt3():
    # Non-existent device
    assert get_device_dict("rt3") == None


def test_get_command_and_device_invalid():
    # string is missing " device=" delimiter
    assert get_command_and_device("netbot get interface device rt1") == (None, None)


def test_get_command_and_device_invalid():
    # device does not exist
    assert get_command_and_device("netbot get interface device=rt3") == (
        "netbot get interface",
        None,
    )


def test_get_command_and_device_rt1():
    assert get_command_and_device("netbot get interface device=rt1") == (
        "netbot get interface",
        {
            "host": "vios-rt1.jm",
            "device_type": "cisco_ios",
            "username": "tester",
            "password": "testerpw",
        },
    )


def test_get_command_and_device_rt2():
    assert get_command_and_device("netbot get interface device=rt2") == (
        "netbot get interface",
        {
            "host": "vios-rt2.jm",
            "device_type": "cisco_ios",
            "username": "tester",
            "password": "testerpw",
        },
    )


def test_netbot_command_interface():
    netbot = NetBot(
        "netbot get interface info",
        {
            "host": "vios-rt2.jm",
            "device_type": "cisco_ios",
            "username": "tester",
            "password": "testerpw",
        },
    )

    assert (
        netbot.get_output()[:60]
        == "Interface                  IP-Address      OK? Method Status"
    )


def test_netbot_command_route():
    netbot = NetBot(
        "netbot get routes",
        {
            "host": "vios-rt2.jm",
            "device_type": "cisco_ios",
            "username": "tester",
            "password": "testerpw",
        },
    )

    assert netbot.get_output()[:22] == "Gateway of last resort"


def test_netbot_invalid_command():
    netbot = NetBot(
        "netbot foo",
        {
            "host": "vios-rt2.jm",
            "device_type": "cisco_ios",
            "username": "tester",
            "password": "testerpw",
        },
    )

    assert netbot.get_output() == (
        f"Command 'netbot foo' is invalid or currently unsupported."
        "Say `netbot help` for list of valid commands."
    )


def test_netbot_invalid_device():
    netbot = NetBot(
        "netbot get routes",
        {
            "host": "192.168.128.244",
            "device_type": "cisco_ios",
            "username": "tester",
            "password": "testerpw",
        },
    )

    assert netbot.get_output() == (
        f"There was a problem connecting to 192.168.128.244\n\n"
    )