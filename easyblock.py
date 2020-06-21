#!/usr/bin/python3
# easyblock.py

__version__ = "0.1.0"

import os
import argparse


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
        hosts_file.write("### easyblock_start ### \n")
        for domain in domains:
            hosts_file.write(f"127.0.0.1 {domain}")
        hosts_file.write("### easyblock_end ### \n")


def turn_off():
    print("Turning off")


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
