from sys import argv


def print_message(msg):
	return {"inbound_message": msg}

if __name__ == '__main__':
	print('Number of arguments:', len(argv), 'arguments.')
	print('Argument List:', str(argv))