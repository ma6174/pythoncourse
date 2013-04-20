#!/usr/bin/env python
# derived from Python Cookbook, 2nd edition, pg 67

import os, sys

def main():
    nargs = len(sys.argv)
    if not 3 <= nargs <= 5:
        print 'Usage: %s search_text replace_text [infile [outfile]]'% sys.argv[0]
    else:
        stext = sys.argv[1]
        rtext = sys.argv[2]
        input_file = sys.stdin
        output_file = sys.stdout
        if nargs > 3:
            input_file = open(sys.argv[3])
        if nargs > 4:
            output_file = open(sys.argv[4],'w')
        for s in input_file:
            output_file.write(s.replace(stext,rtext))
        output_file.close()
        input_file.close()


if __name__ == '__main__':
    print 'before we call, the args are:'
    for a in sys.argv:
        print a
    main()


