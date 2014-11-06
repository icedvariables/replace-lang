#!/usr/bin/env python

import re, sys

RE_LINE = re.compile("(.*)/(.*)")

def interpret(code, debug=False):
    program = original = code

    if(debug):print "INPUT:", program

    for i, line in enumerate(program.split("\n")):
        match = re.match(RE_LINE, line)
        
        if(match):
            find = match.group(1)
            replace = match.group(2)
        
            if(debug):print "FIND:", find, "REPLACE:", replace
        
            if(find):
                program = re.sub(find, replace, program)
        
        if(debug):
            print "LOOP "+str(i)+":"
            print program+"\n"

    return program

if __name__=="__main__":
    if(len(sys.argv) < 2):
        print __FILE__+" filename [debug]"
        sys.exit()
    
    filename = sys.argv[1]
    try:
        debug = int(sys.argv[2])
    except:
        debug = 0
    
    try:
        f = open(filename, "r")
    except IOError:
        print "Could not read file '"+filename+"'"
        sys.exit()
    
    out = interpret(f.read(), debug)
    
    f.close()
    
    print "OUTPUT:"
    print out