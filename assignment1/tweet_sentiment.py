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
            scores[k] = int(v.strip("\n"))  # initialize an empty dictionary
    #print scores.items()
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
            stdout.append(score_sum)
        #lines(tweet_file)
        #tweet_file.close()
    #print "Scores: %s" % stdout
    for number in stdout:
        print number

if __name__ == '__main__':
    main()

