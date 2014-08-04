# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 11:57:03 2014

@author: 113010545
"""

import sys
import json

def main():
    hashtags_dict = {}
    with open (sys.argv[1], mode = "r") as tweet_file:     
        for i in tweet_file:  # i is one tweet
            i = json.loads(i)  #parse the nested tweets in workable format'              
            if 'entities' in i:
                x = i['entities']  # x is the entity in tweet i
                hashtags_ent = x['hashtags'] # hashtags_ent is the list of hashtags
                for a in hashtags_ent:  # a is the dict in the hashtags_ent list
                    hashtags_txt = a['text'] # hashtags_txt is the hashtag text in a
                    hashtags_txt = hashtags_txt.encode('utf-8')
                    if hashtags_txt in hashtags_dict.iteritems():  
                        hashtags_dict[hashtags_txt] = hashtags_dict[hashtags_txt] + 1
                    else:                    
                        hashtags_dict[hashtags_txt] = 1                                                 
                        
    stdout = []
    for key in sorted(hashtags_dict, key = hashtags_dict.get, reverse = True):
        temp = key + "LIMITER" + str(hashtags_dict[key])
        stdout.append(temp)
    
    for y in stdout[0:10]:
        k, c = y.split("LIMITER")
        c = float(c)    
        print "%s %s" % (k, c)
    
if __name__ == '__main__':
    main()
