# python-rustserver
Rust Server Automation Only!

## Prerequisites
* Centos 8
    * `sudo yum install epel-release -y`
    * `sudo yum install git ansible python38.x86_64 glibc.i686 libstdc++.i686 wget -y`
* Ubuntu 64-bit
    * `sudo dpkg --add-architecture i386; sudo apt update; sudo apt install ansible wget tar netcat lib32gcc1 lib32stdc++6 steamcmd lib32z1 unzip`
    
## Install Requirements
* Ansible
* Python3
* Git
* Unzip

## Python modules
`pip install -r requirements.txt`

## Commands
* `-h, --help`
    * show this help message and exit
* `--install`
    * Install Rust Server
* `--start`
    * Run Rust Server
* `--stop`             
    * Stop Rust Server
* `--restart`
    * Restart Rust Server
* `--update`
    * Update Rust Server
* `--install_mod`
    * Install Oxide
* `--download_plugin="plugin_name"`
    * Downloads Plugin from umod
* `--command`
    * Run Rcon Command
* `--partial_wipe`
    * Clean up Maps
* `--full_wipe`
    * Clean up everything!
* `--clean`
    * Destroys server folder
* `--check`
    * Checks by server_identity if server is running.
    
## FAQ
* Can this run inside a docker container?
    * Yes I have tested this with centos 8 container and was successful.
