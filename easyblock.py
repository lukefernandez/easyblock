#!/usr/bin/python3
# easyblock.py
#
# Tested on Ubuntu 20.04

__version__ = "0.1.0"

import os
import re
import argparse

block_start_string = "### easyblock_start ### \n"
block_end_string = "### easyblock_end ### \n"


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "target_state",
        type=str,
        choices=["on", "off"],
        help="Select your target state.",
    )
    return parser.parse_args()


def get_domains():
    home_path = os.path.expanduser(f"~{os.environ.get('SUDO_USER')}")
    config_file_name = ".easyblock"
    with open(f"{home_path}/{config_file_name}", "r") as config_file:
        domains = []
        for domain in config_file:
            domains.append(domain)
    return domains


def turn_on():
    domains = get_domains()
    with open("/etc/hosts", "a") as hosts_file:
        hosts_file.write(block_start_string)
        for domain in domains:
            hosts_file.write(f"127.0.0.1 {domain}")
        hosts_file.write(block_end_string)


def turn_off():
    """
    TODO: This can almost certainly be cleaned up. Let's make that happen.
    """
    with open("/etc/hosts", "r") as hosts_file:
        with open("/etc/hosts-future", "w") as future_hosts_file:
            delete = False
            for line in hosts_file:
                if re.match(line, block_start_string):
                    delete = True
                    continue
                elif re.match(line, block_end_string):
                    delete = False
                    continue

                if delete:
                    continue
                else:
                    future_hosts_file.write(line)
    os.replace("/etc/hosts-future", "/etc/hosts")


def main():
    args = get_args()
    if args.target_state == "on":
        turn_on()
    elif args.target_state == "off":
        turn_off()
    else:
        raise Exception("Invalid choice for target state. Choose either 'on' or 'off'.")


if __name__ == "__main__":
    main()
