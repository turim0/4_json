import json
import sys


def load_data(file_name):
    try:
        with open(file_name, encoding='utf-8') as json_file:
            json_string = json_file.read()
            decoded_json = json.loads(json_string)
            return decoded_json
    except (FileNotFoundError, ValueError):
        return None



def pretty_print_json(decoded_json):
    print(json.dumps(decoded_json, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    if len(sys.argv) == 1 or sys.argv[1] in {'-h', '--help'}:
        print('Usage: {0} + your_file.json'.format(sys.argv[0]))
        sys.exit()
    decoded_json = load_data(sys.argv[1])
    if decoded_json is None:
        sys.exit('Error: file not found or no json object could be decoded')
    pretty_print_json(decoded_json)



