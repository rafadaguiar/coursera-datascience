import sys


def sentiment_ref(afinnfile):
    scores = {}  # initialize an empty dictionary
    for line in afinnfile.readlines():
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores


def tweet_score(sent_scores, tweet):
    score = 0.0
    newWords = []
    words = tweet.split()
    for word in words:
        if word in sent_scores.keys():
            score += sent_scores[word]
        else:
            newWords.append(word)
    return [tweet, score, newWords]


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_scores = sentiment_ref(sent_file)

    response = []
    for line in tweet_file.readlines():
        response.append(tweet_score(sent_scores, line))
    score = 0.0
    for resp in response:
        for newword in resp[2]:
            for r in response:
                if newword in r[0]:
                    score += r[1]/len(r[0])
            print "%s %f" % (newword, score)

if __name__ == '__main__':
    main()
