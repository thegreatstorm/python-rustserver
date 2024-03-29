#!/usr/bin/python3

# Base Imports
import argparse
import os
import shutil
import json

# Custom Code
from bin.utils.argument_controller import argument_controller
from bin.utils.configuration_controller import config_controller, set_game_config, get_game_config
from bin.server_manager import run_playbook
from bin.utils.rust_rcon_connector import connect_rust_rcon
from bin.server_manager import find_process

# Grabs path where this script was ran.
script_dir = os.path.dirname(os.path.abspath(__file__))
prefix_dir = os.path.abspath(os.path.join(script_dir))


# =============== Arguments =============================
args = argument_controller()
# =============== Arguments =============================

# ================ Configuration Piece ===================
config_settings = config_controller(script_dir, "var/conf/default.conf", "var/conf/local.conf")
app_name = config_settings.get('general', 'app_name')
version = config_settings.get('general', 'version')
description = config_settings.get('general', 'description')
game_installed = config_settings.get('game_settings', 'installed')
current_game = "rustserver"
app_directory = os.path.abspath(os.path.join(prefix_dir, "server/"))
# ================ Configuration Piece ===================

app_settings = {}
app_settings["app_name"] = app_name
app_settings["version"] = version
app_settings["description"] = description
app_settings["app_directory"] = script_dir

game_config = {}
game_config["app_dir"] = app_directory
print("Welcome to {}".format(app_name))
print(description)
print("<{}>".format(version))
print("========================================================")
print("")


if args.start:
    print("Starting Rust Server")
    print("--------------------------------------------------------")
    if game_installed != 'unset':
        playbook_name = "start.yml"
        game_config = get_game_config(prefix_dir, game_config, current_game)
        playbook = os.path.abspath(os.path.join(prefix_dir, "playbooks/{}/{}".format(current_game, playbook_name)))
        try:
            run_playbook(playbook, game_config)
        except Exception as e:
            print("Started Rust Server: {}".format(str(e)))
            exit(1)
    else:
        print("Rust Server not installed.")
        exit(0)

if args.install:
    print("Installing Rust Server: {}".format(current_game))
    print("--------------------------------------------------------")
    if game_installed == 'unset':
        playbook_name = "install.yml"
        playbook = os.path.abspath(os.path.join(prefix_dir, "playbooks/{}/{}".format(current_game, playbook_name)))
        try:
            # Copies over the config
            set_game_config(script_dir, config_settings, current_game)
            run_playbook(playbook, game_config)
        except Exception as e:
            print("Failed To Install: {}".format(str(e)))
            exit(1)
    else:
        print("Rust Server not installed.")
        exit(0)

if args.update:
    print("Updating Rust Server")
    print("--------------------------------------------------------")
    if game_installed != 'unset':
        playbook_name = "update.yml"
        playbook = os.path.abspath(os.path.join(prefix_dir, "playbooks/{}/{}".format(current_game, playbook_name)))
        run_playbook(playbook, game_config)
    else:
        print("Rust Server not installed.")
        exit(1)

if args.stop:
    print("Stopping Rust Server")
    print("--------------------------------------------------------")
    if game_installed != 'unset':
        game_config = get_game_config(prefix_dir, game_config, current_game)
        playbook_name = "stop.yml"
        playbook = os.path.abspath(os.path.join(prefix_dir, "playbooks/{}/{}".format(current_game, playbook_name)))
        run_playbook(playbook, game_config)
    else:
        print("Rust Server not installed.")
        exit(1)

if args.restart:
    print("Restarting Rust Server")
    print("--------------------------------------------------------")
    if game_installed != 'unset':
        game_config = get_game_config(prefix_dir, game_config, current_game)
        server_identity = game_config['identity']
        playbook_name = "restart.yml"
        game_config = get_game_config(prefix_dir, game_config, current_game)
        playbook = os.path.abspath(os.path.join(prefix_dir, "playbooks/{}/{}".format(current_game, playbook_name)))
        try:
            run_playbook(playbook, game_config)
            print("Restarted Rust Server")
            exit(0)
        except Exception as e:
            print("Failed To Install: {}".format(str(e)))
            exit(1)
    else:
        print("Rust Server not installed.")
        exit(1)

if args.install_mod:
    print("Installing Oxide")
    print("--------------------------------------------------------")
    if game_installed != 'unset':
        playbook_name = "mod_install.yml"
        playbook = os.path.abspath(os.path.join(prefix_dir, "playbooks/{}/{}".format(current_game, playbook_name)))
        run_playbook(playbook, game_config)
    else:
        print("Rust Server not installed.")
        exit(1)

if args.partial_wipe:
    print("Partial Wipe Wipe Rust Server")
    print("--------------------------------------------------------")
    if game_installed != 'unset':
        game_config = get_game_config(prefix_dir, game_config, current_game)
        print("{}/rustserver/server/{}/*.map".format(game_config["app_dir"], game_config["identity"]))
        playbook_name = "partial_wipe.yml"
        playbook = os.path.abspath(os.path.join(prefix_dir, "playbooks/{}/{}".format(current_game, playbook_name)))
        run_playbook(playbook, game_config)
    else:
        print("Rust Server not installed")
        exit(1)

if args.full_wipe:
    print("Full Wipe Rust Server")
    print("--------------------------------------------------------")
    if game_installed != 'unset':
        game_config = get_game_config(prefix_dir, game_config, current_game)
        playbook_name = "full_wipe.yml"
        playbook = os.path.abspath(os.path.join(prefix_dir, "playbooks/{}/{}".format(current_game, playbook_name)))
        run_playbook(playbook, game_config)
    else:
        print("Rust Server not installed")
        exit(1)

if args.clean:
    print("Cleaning Server Directory")
    print("--------------------------------------------------------")
    # Removing Server Folder
    server_dir = os.path.abspath(os.path.join(prefix_dir, "server/"))
    conf = os.path.abspath(os.path.join(prefix_dir, "var/conf/"))
    # Creating server folder.
    try:
        if os.path.isdir(server_dir):
            shutil.rmtree(server_dir)
            os.makedirs(server_dir + "/conf")
            if os.path.isfile("{}/local.conf".format(conf)):
                os.remove("{}/local.conf".format(conf))
            print("Cleaned Settings")
        else:
            os.makedirs(server_dir + "/conf")
            os.makedirs(server_dir + "/downloads")
            print("Cleaned Settings")
    except OSError as error:
        print("Failed to Clean OSError: ".format(str(error)))

if args.command:
    if args.command is not None:
        print("Running Rust Command")
        print("--------------------------------------------------------")
        if game_installed != 'unset':
            game_config = get_game_config(prefix_dir, game_config, current_game)
            server_info = {}
            server_info["hostname"] = "0.0.0.0"
            server_info["rcon_port"] = game_config['rcon_port']
            server_info["rcon_password"] = game_config['rcon_password']
            server_info["enable_trace"] = False
            # print(server_info)
            connect_rust_rcon(server_info, args.command)
        else:
            print(args.command)
            print("Rust Server not installed")
            exit(1)

if args.download_plugin:
    if args.download_plugin is not None:
        print("Download Plugin from Umod!")
        print("--------------------------------------------------------")
        if game_installed != 'unset':
            plugin_name = args.download_plugin
            game_config = get_game_config(prefix_dir, game_config, current_game)

            playbook_name = "plugin_install.yml"
            playbook = os.path.abspath(os.path.join(prefix_dir, "playbooks/{}/{}".format(current_game, playbook_name)))

            game_config["plugin_name"] = plugin_name
            run_playbook(playbook, game_config)
        else:
            print(args.command)
            print("Rust Server not installed")
            exit(1)

if args.change_map:
    if args.change_map is not None:
        print("Change Map Settings -- This won't reflect unless an restart")
        print("--------------------------------------------------------")
        if game_installed != 'unset':
            if args.seed is None or args.size is None:
                print("You must put --seed=\"\" --size=\"\" to change map settings")
                exit(1)
            seed = args.seed
            size = args.size
            game_config = get_game_config(prefix_dir, game_config, current_game)

            playbook_name = "change_map.yml"
            playbook = os.path.abspath(os.path.join(prefix_dir, "playbooks/{}/{}".format(current_game, playbook_name)))

            game_config["seed"] = args.seed
            game_config["size"] = args.size
            run_playbook(playbook, game_config)
        else:
            print(args.command)
            print("Rust Server not installed")
            exit(1)
        exit(1)

if args.check:
    print("Checking Rust Server Is Running")
    print("--------------------------------------------------------")
    if game_installed != 'unset':
        game_config = get_game_config(prefix_dir, game_config, current_game)
        server_identity = game_config['identity']
        if find_process(server_identity):
            print("{} is running!".format(game_config['hostname']))
        else:
            print("{} is down!".format(game_config['hostname']))
    else:
        print("Rust Server not installed.")
        exit(1)

print("Make sure you type in --help to get more info!")