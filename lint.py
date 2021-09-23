#!/usr/bin/env python

import sys 

from pylint import lint  

THRESHOLD = 0 

run = lint.Run(["calculadora.py"], do_exit=False) 
score = run.linter.stats["global_note"]  

if score < THRESHOLD: 

    print("Linter failed: Score < threshold value") 

    sys.exit(1) 


sys.exit(0) 