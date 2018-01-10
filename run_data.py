from sys import argv
from json import loads, dumps

def print_message(msg):
	return {"inbound_message": msg}

if __name__ == '__main__':
	# print('Number of arguments:', len(argv), 'arguments.')
	# print('Argument List:', str(argv))
	# print(dumps(print_message(argv[2]), indent=4, sort_keys=True))
    data = loads(argv[1])
    #print(dumps(print_message(data), indent=4, sort_keys=True))
    print(data)




