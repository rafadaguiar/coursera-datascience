import sys


def sentiment_ref(afinnfile):
    scores = {}  # initialize an empty dictionary
    for line in afinnfile.readlines():
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores


def tweet_score(sent_scores, tweet):
    score = 0.0
    for word in tweet.split():
        if word in sent_scores.keys():
            score += sent_scores[word]
    print score


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_scores = sentiment_ref(sent_file)

    for line in tweet_file.readlines():
        tweet_score(sent_scores, line)

if __name__ == '__main__':
    main()
