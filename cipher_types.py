import subprocess
import json

def get_cipher_types():
	# terminal 'open ssl help'
	p = subprocess.Popen(['openssl', 'help'], stderr=subprocess.PIPE)
	out, openssl_output = p.communicate()

	cipher_types = []

	# cipher types are after 'details\n', delimited by ' ' and not ''
	for line in openssl_output.split('details)\n')[-1].split("\n"):
		cipher_types = cipher_types + [part for part in line.split(' ') if part != '']

	return cipher_types

print json.dumps(get_cipher_types())
