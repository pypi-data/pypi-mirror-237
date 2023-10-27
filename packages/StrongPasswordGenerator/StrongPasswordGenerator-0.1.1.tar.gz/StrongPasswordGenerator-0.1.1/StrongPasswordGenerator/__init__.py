import argparse, os, re

def generate(options = {}):

	generatedPattern = ''
	password = ''

	if not 'whitelist' in options:
		options['whitelist'] = '[a-zA-Z0-9\\x21-\\x40\\x5B-\\x60\\x7B-\\x7D]'

	if 'verbose' in options:
		print("Whitelist : %s" % options['whitelist'])

	if not 'length' in options:
		options['length'] = 15

	for x in range(0, 0xff):
		char = chr(x)

		if re.match(options['whitelist'], char):
			generatedPattern += char

	if 'blacklist' in options:
		generatedPattern = re.sub(options['blacklist'], '', generatedPattern)

		if 'verbose' in options:
			print("Using blacklist : %s" % options['blacklist'])

	if 'verbose' in options:
		print("Generated pattern : %s" % generatedPattern)

	generatedPatternLength = len(generatedPattern)

	for x in os.urandom(options['length']):
#		python3 x = integer
#		python2 x = string
		password += generatedPattern[x % generatedPatternLength]

	return password
