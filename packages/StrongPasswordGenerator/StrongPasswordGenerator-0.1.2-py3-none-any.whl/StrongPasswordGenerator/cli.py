import argparse
from StrongPasswordGenerator import generate

patternPreset = [('[a-zA-Z0-9]', 'abcDEF789'), ('[a-f0-9]', 'Hexadecimal'), ('[\.\-]', 'Morse')]


def about():
  patternDump = ''

  for i, v in enumerate(patternPreset):
    patternDump += "\t%d. %s - %s\n" % (i + 1, v[0], v[1])

  return '''%(prog)s [options]

Preset patterns to be used with -x flag:
''' + patternDump


def main():
  parser = argparse.ArgumentParser(usage=about())

  parser.add_argument('-x', dest='pattern', default=None, type=int, required=False, help='Specifies pattern preset, overrides whitelist')
  parser.add_argument('-w', dest='whitelist', default=None, required=False, help='Regex pattern for allowed characters')
  parser.add_argument('-b', dest='blacklist', default=None, required=False, help='Regex pattern for disallowed characters')
  parser.add_argument('-v', dest='verbose', default=None, action='store_true', required=False, help='Verbose mode')
  parser.add_argument('-q', dest='avoidSimilar', action='store_true', default=None, required=False, help='Avoid similar characters (1iIl0oO\'´`\|.,), overrides blacklist')
  parser.add_argument('-c', dest='length', default=None, type=int, help="Password length")

  arguments = vars(parser.parse_args())

  for key, value in list(arguments.items()):
    if value is None:
      del arguments[key]

  if 'avoidSimilar' in arguments:
    arguments['blacklist'] = '[1|i|I|l|\||0|o|0|`|´|"|\'|\.|,]'

  if 'pattern' in arguments and arguments['pattern'] > 0 and arguments['pattern'] <= len(patternPreset):
    arguments['whitelist'] = patternPreset[arguments['pattern'] - 1][0]

  print(generate(arguments))
