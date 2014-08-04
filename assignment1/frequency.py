# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 22:42:25 2014

@author: 113010545
"""

import sys
import json

def main():
    stdout = {}
    #count = 0.0
    with open (sys.argv[1], mode = "r") as tweet_file:
       for i in tweet_file:
           i = json.loads(i)  #parse the nested tweets in workable format
           if 'text' in i:        
               phrase = i['text'].encode('utf-8')
           else:
               phrase = ""
           for word in phrase.split():
               if word.isalpha():
                   if word in stdout:
                       stdout[word] = stdout[word] + 1.0
                   else:
                       stdout[word] = 1.0
    total = len(stdout.keys()) + 0.0
    for x in stdout:
        stdout[x] = stdout[x]/total
    for key, value in stdout.iteritems():
        print key, value    
    
if __name__ == '__main__':
    main()
