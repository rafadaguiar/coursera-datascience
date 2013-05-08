import sys
import json


def parser_text_state(response):
    txst = []

    for line in response:
        result = json.loads(line.strip())
        if 'place' in result.keys() and (result['place'] is not None):
            if 'country_code' in result['place'].keys() and result['place']['country_code'] == 'US':
                state = result['place']['full_name'].split(", ")[1]
                txst.append([result['text'], state])
    return txst


def sentiment_ref(afinnfile):
    scores = {}  # initialize an empty dictionary
    for line in afinnfile.readlines():
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores


def tweet_score(sent_scores, txst):
    score = 0.0
    stscore = {}
    for tweet, state in txst:
        for word in tweet.split():
            if word in unicode(sent_scores.keys()):
                score += 1
        stscore[state] = score
    first = sorted(stscore, key=stscore.get, reverse=True)
    if first:
        print first[0]


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sent_scores = sentiment_ref(sent_file)
    txst = parser_text_state(tweet_file)
    tweet_score(sent_scores, txst)

if __name__ == '__main__':
    main()
