from netmiko import ConnectHandler


class NetBot:
    """
    Define NetBot class to interact with network devices
    based on messages sent by Slack users
    """

    HELP_TEXT = (
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

    def __init__(self, command="", device=""):
        """
        Class constructor

        :param command: Command to pass to get_output()
        :type command: str
        :param device: Device attributes used for login
        :type device: dict
        """
        self.command = command
        self.device = device

    def send_help_info(self):
        """
        Send help info to users know what to do

        :return: Text to post in a Slack message response
        :rtype: str
        """

        return self.HELP_TEXT

    def get_output(self):
        """
        get output specified in self.command from device
        indicated in self.device.

        :return: Command output or error message
        :rtype: str
        """

        # If we didn't get a dict passed as device, the
        # device is invalid
        if not type(self.device) is dict:
            return 'Invalid device. Say "netbot help" for list of valid devices.'

        match self.command:
            case "netbot get interface info":
                command = "show ip interface brief"
            case "netbot get routes":
                command = "show ip route | begin ^Gateway"
            case "netbot get hsrp":
                command = "show standby brief"
            case _:
                return (
                    f"Command '{self.command}' is invalid or currently unsupported."
                    "Say `netbot help` for list of valid commands."
                )

        # Connect to device and get command output
        try:
            connection = ConnectHandler(**self.device)
        except:
            # connection error
            return f"There was a problem connecting to {self.device['host']}\n\n"
        else:
            with ConnectHandler(**self.device) as connection:
                return connection.send_command(command)