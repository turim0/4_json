#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import sys


def load_data():
    with open(sys.argv[1]) as json_file:
        json_string = json_file.read()
        parsed_string = json.loads(json_string)
        return parsed_string


def pretty_print_json(parsed_string):
    print(json.dumps(parsed_string, indent = 4))


if __name__ == '__main__':
    try:
        if len(sys.argv) == 1 or sys.argv[1] in {'-h', '--help'}:
            print('Usage: {0} + your_file.json'.format(sys.argv[0]))
            sys.exit()
        parsed_string = load_data()
        pretty_print_json(parsed_string)
    except FileNotFoundError as err:
        print(err)


