import os
import configparser


def config_controller(script_dir, default, local):

    config = configparser.RawConfigParser()
    prefix_dir = os.path.abspath(os.path.join(script_dir))
    default_config_path = os.path.abspath(os.path.join(prefix_dir, default))
    local_config_path = os.path.abspath(os.path.join(prefix_dir, local))

    config.read(default_config_path)
    if os.path.isfile(local_config_path):
        config.read(local_config_path)

    return config


def get_game_config(prefix_dir, game_config, game_name):
    # Game Configuration
    game_config_settings = config_controller(prefix_dir, "server/conf/{}.conf".format(game_name), "local.conf")
    for each_section in game_config_settings.sections():
        for (key, value) in game_config_settings.items(each_section):
            game_config[key] = value

    return game_config


def set_game_config(script_dir, config_settings, game_name):
    print("Setting Game Configurations...")
    prefix_dir = os.path.abspath(os.path.join(script_dir))

    # Game Configuration
    game_config = config_controller(script_dir, "var/lib/{}.conf".format(game_name), "local.conf")
    server_dir = os.path.abspath(os.path.join(prefix_dir, "server/"))
    # Writing our configuration file to 'example.ini'
    with open('{}/conf/{}.conf'.format(server_dir, game_name), 'w') as configfile:
        game_config.write(configfile)

    # App Configurations
    config_settings.set('game_settings', 'installed', game_name)
    config_settings.remove_section('general')
    config_dir = os.path.abspath(os.path.join(prefix_dir, "var/conf/"))
    # Writing our configuration file to 'example.ini'
    with open('{}/local.conf'.format(config_dir), 'w') as configfile:
        config_settings.write(configfile)