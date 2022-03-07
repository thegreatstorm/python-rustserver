import argparse


def argument_controller():
    # Plugins may have to been done manual has mods are different per game server.
    parser = argparse.ArgumentParser('Automate your Rust Server!')
    parser.add_argument('--install', help='Install Rust Server', required=False, action='store_true')
    parser.add_argument('--start', help='Run Rust Server', required=False, action='store_true')
    parser.add_argument('--stop', help='Stop Rust Server', required=False, action='store_true')
    parser.add_argument('--check', help='Check Running', required=False, action='store_true')
    parser.add_argument('--restart', help='Restart Rust Server', required=False, action='store_true')
    parser.add_argument('--update', help='Update Rust Server', required=False, action='store_true')
    parser.add_argument('--change_map', help='Change Map Rust Server', required=False, action='store_true')
    parser.add_argument('--seed', help='Change Seed', required=False)
    parser.add_argument('--size', help='Change Size', required=False)
    parser.add_argument('--install_mod', help='Install Oxide', required=False, action='store_true')
    parser.add_argument('--partial_wipe', help='Clean up Maps', required=False, action='store_true')
    parser.add_argument('--full_wipe', help='Clean up everything!', required=False, action='store_true')
    parser.add_argument('--clean', help='Destroys server folder', required=False, action='store_true')
    parser.add_argument('--download_plugin', help='Download Plugin', required=False)
    parser.add_argument('--command', help='Run Rcon Command', required=False)
    args = parser.parse_args()
    return args