import os
import json
from subprocess import check_output
import re
from bin.utils.configuration_controller import config_controller


def run_playbook(playbook, game_server_config):
    result = json.dumps(game_server_config)
    command = "ansible-playbook {} --extra-vars '{}'".format(playbook, result)
    # print(command)
    # Run the playbook
    os.system(command)


def find_process(process_name):
  output = check_output('ps aux | grep -ie "Rust Server" | grep -v grep | awk \'{print $2}\'', shell=True)
  print(output.split())
  if len(output.split()) > 0:
      return True

  return False
