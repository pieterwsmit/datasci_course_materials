import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    scores = {}
    with open (sys.argv[1], mode = "r") as sent_file:   
        for line in sent_file:
            k, v = line.split("\t")
            scores[k] = int(v.strip("\n"))
    
    
    abs_words = {}
    tweet_words = []       
    stdout = []
    with open (sys.argv[2], mode = "r") as tweet_file:
        for i in tweet_file:
            i = json.loads(i)  #parse the nested tweets in workable format
            score_sum = 0 
            if 'text' in i:        
                phrase = i['text'].encode('utf-8')
            else:
                phrase = ""
            for word in phrase.split():
                for x in scores:
                    if x == word:
                        score_sum = score_sum + scores[x]
                    elif word.isalpha():
                        tweet_words.append(word)
            tweet_words = list(set(tweet_words))
            for a in tweet_words:
                if a in abs_words:
                    abs_words[a] = abs_words[a] + score_sum
                else:
                    abs_words[a] = score_sum
            stdout.append(score_sum)
    for key, value in abs_words.iteritems():
        print key, value

if __name__ == '__main__':
    main()
