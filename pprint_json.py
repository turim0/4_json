import json
import sys


def load_data(file_name):
    try:
        with open(file_name) as json_file:
            json_string = json_file.read()
            parsed_dict = json.loads(json_string)
            return parsed_dict
    except FileNotFoundError as err:
        print(err)
    except ValueError:
        print('No JSON object could be decoded')


def pretty_print_json(parsed_dict):
    print(json.dumps(parsed_dict, indent=4))


if __name__ == '__main__':
    if len(sys.argv) == 1 or sys.argv[1] in {'-h', '--help'}:
        print('Usage: {0} + your_file.json'.format(sys.argv[0]))
        sys.exit()
    parsed_dict = load_data(sys.argv[1])
    pretty_print_json(parsed_dict)



