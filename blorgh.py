#!/usr/bin/python3

import argparse
import sys

from lib import git
from lib import mkd

if __name__ == '__main__':

  '''// BLORGH //'''

  parser = argparse.ArgumentParser()

  parser.add_argument('-o', '--output-dir',
      help='output directory where the static files will be put')

  parser.add_argument('-u', '--url', 
      help='The Git repo URL to checkout and build')

  parser.add_argument('-d', '--directory',
      help='The source directory to build from')

  args = parser.parse_args()

  if args.output_dir:
    output_dir = args.output_dir
  else:
    print("No output directory specified... Aborting.")
    sys.exit(1)

  if args.directory:
    input_dir = args.directory
  else:
    print("No source directory specified... Aborting.")
    sys.exit(1)

  if args.url:
    git.clone(args.url, input_dir)

  print("Generating static resources from '{}' to '{}'").format(
      input_dir, output_dir)

  mkd.generate_static(input_dir, output_dir)

  print("\n\nDone!")
  sys.exit(0)





