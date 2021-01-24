import os
import json
from bin.utils.configuration_controller import config_controller


def run_playbook(playbook, game_server_config):
    result = json.dumps(game_server_config)
    command = "ansible-playbook {} --extra-vars '{}'".format(playbook, result)
    # print(command)
    # Run the playbook
    os.system(command)
