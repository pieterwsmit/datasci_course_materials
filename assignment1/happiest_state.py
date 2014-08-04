# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 23:07:12 2014

@author: 113010545
"""
import sys
import json

def main():    
    states = {
            'AK': 'Alaska',
            'AL': 'Alabama',
            'AR': 'Arkansas',
            'AS': 'American Samoa',
            'AZ': 'Arizona',
            'CA': 'California',
            'CO': 'Colorado',
            'CT': 'Connecticut',
            'DC': 'District of Columbia',
            'DE': 'Delaware',
            'FL': 'Florida',
            'GA': 'Georgia',
            'GU': 'Guam',
            'HI': 'Hawaii',
            'IA': 'Iowa',
            'ID': 'Idaho',
            'IL': 'Illinois',
            'IN': 'Indiana',
            'KS': 'Kansas',
            'KY': 'Kentucky',
            'LA': 'Louisiana',
            'MA': 'Massachusetts',
            'MD': 'Maryland',
            'ME': 'Maine',
            'MI': 'Michigan',
            'MN': 'Minnesota',
            'MO': 'Missouri',
            'MP': 'Northern Mariana Islands',
            'MS': 'Mississippi',
            'MT': 'Montana',
            'NA': 'National',
            'NC': 'North Carolina',
            'ND': 'North Dakota',
            'NE': 'Nebraska',
            'NH': 'New Hampshire',
            'NJ': 'New Jersey',
            'NM': 'New Mexico',
            'NV': 'Nevada',
            'NY': 'New York',
            'OH': 'Ohio',
            'OK': 'Oklahoma',
            'OR': 'Oregon',
            'PA': 'Pennsylvania',
            'PR': 'Puerto Rico',
            'RI': 'Rhode Island',
            'SC': 'South Carolina',
            'SD': 'South Dakota',
            'TN': 'Tennessee',
            'TX': 'Texas',
            'UT': 'Utah',
            'VA': 'Virginia',
            'VI': 'Virgin Islands',
            'VT': 'Vermont',
            'WA': 'Washington',
            'WI': 'Wisconsin',
            'WV': 'West Virginia',
            'WY': 'Wyoming'
    }
    
    
    scores = {}
    with open (sys.argv[1], mode = "r") as sent_file:   
        for line in sent_file:
            k, v = line.split("\t")
            scores[k] = int(v.strip("\n"))  # initialize an empty dictionary
            
    state_scores = {}
    with open (sys.argv[2], mode = "r") as tweet_file:     
        for i in tweet_file:
            i = json.loads(i)  #parse the nested tweets in workable format'
            state = ""                
            if 'user' in i:
                x = i['user']
                state_str = str(x['location'].encode('utf-8'))
                for st, name in states.iteritems():
                    if (len(state_str) > 4 and ((state_str[-3] == ",") or (state_str[-4] == ","))):
                        temp = state_str[-2:].upper()
                        if temp == st:                    
                            state = temp
                    elif (state_str == name):
                        state = st
            score_sum = 0
            if len(state) > 0:
                if 'text' in i:        
                    phrase = i['text'].encode('utf-8')
                else:
                    phrase = ""        
                for word in phrase.split():
                    for x in scores:
                        if x == word:
                            score_sum = score_sum + scores[x]
            if state in state_scores:
                state_scores[state] = state_scores[state] + score_sum
            else:
                state_scores[state] = score_sum                
    
    stdout = max(state_scores, key=state_scores.get)
    print stdout
 
if __name__ == '__main__':
    main()   


 
 