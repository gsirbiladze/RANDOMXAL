
from awscli import clidriver



class GAWSCliGui(object):

    def __init__(self):
        self.main_cmd_provider = clidriver.create_clidriver().create_help_command()

    def get_main_cmd(self, cmd=None):
        """ """
        return self.main_cmd_provider.command_table if cmd is None else self.main_cmd_provider.command_table.get(cmd, None)

    def get_sub_cmd(self, cmd, sub_cmd=None):
        """ """
        curr_cmd = self.get_main_cmd(cmd)
        if curr_cmd is None: return None

        sub_cmd_list = curr_cmd.create_help_command().command_table
        return sub_cmd_list if sub_cmd is None else sub_cmd_list.get(sub_cmd, None)

    def get_sub_cmd_args(self, cmd, sub_cmd):
        """ """
        get_cmd = self.get_sub_cmd(cmd, sub_cmd)
        return get_cmd.create_help_command() if get_cmd is not None else None







