import argparse


def argument_controller():
    # Plugins may have to been done manual has mods are different per game server.
    parser = argparse.ArgumentParser('Automate your Rust Server!')
    parser.add_argument('-r', '--run', help='Run Rust Server', required=False, action='store_true')
    parser.add_argument('-s', '--stop', help='Stop Rust Server', required=False, action='store_true')
    parser.add_argument('-t', '--restart', help='Restart Rust Server', required=False, action='store_true')
    parser.add_argument('-i', '--install', help='Install Rust Server', required=False, action='store_true')
    parser.add_argument('-u', '--update', help='Update Rust Server', required=False, action='store_true')
    parser.add_argument('-m', '--install_mod', help='Install Oxide', required=False, action='store_true')
    parser.add_argument('-d', '--command', help='Run Rcon Command <command>', required=False)
    parser.add_argument('-p', '--partial_wipe', help='Clean up Maps', required=False, action='store_true')
    parser.add_argument('-w', '--full_wipe', help='Clean up everything!', required=False, action='store_true')
    parser.add_argument('-c', '--clean', help='Clean Rust Server (Y/N)', required=False, action='store_true')
    args = parser.parse_args()
    return args