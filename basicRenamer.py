#!/usr/bin/env python

import os
import argparse

if __name__ == '__main__':
    # Check the arguments passed
    args = argparse.ArgumentParser()
    args.add_argument("-i", "--inputDir", required=True, help="The directory to list files from.")
    args.add_argument("-t", "--test", required=False, action="store_true", help="If passed, the program will only simulate the move")
    args.add_argument("-v", "--verbose", required=False, action="store_true", help="If passed, the program will output verbosely")
    args.add_argument("-f", "--formatString", required=True, help="The string to format the files to. Use ^ as the incrementing number")
    args = args.parse_args()

    files = [f for f in os.listdir(args.inputDir) if os.path.isfile(os.path.join(args.inputDir, f))]
    files.sort();

    counter = 1
    for file in files:
        filename, fileExt = os.path.splitext(file)
        newFilename = "%s%s" % (args.formatString.replace('^', '{:02d}'.format(counter)), fileExt)

        if args.verbose or args.test:
    	   print("%s becomes %s..." % (file, newFilename))
        if not args.test:
            os.rename(args.inputDir + file, args.inputDir + newFilename)
    	counter += 1