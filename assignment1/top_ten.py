from collections import defaultdict
import operator
import sys
import json


def get_counts(seq):
    counts = defaultdict(float)
    for x in seq:
        counts[x] += 1
    return sorted(counts.iteritems(), key=operator.itemgetter(1), reverse=True)[:10]


def parser_hashtag(response):
    hashtags = []
    for line in response:
        result = json.loads(line.strip())
        if 'entities' in result.keys():
            if 'hashtags' in result['entities'].keys() and result['entities']['hashtags'] != []:
                # print result['entities']['hashtags'][0]['text']
                hashtags.append(result['entities']['hashtags'][0]['text'])
    return hashtags


def main():
    tweet_file = open(sys.argv[1])
    top10 = get_counts(parser_hashtag(tweet_file))
    for hashtag, count in top10:
        print "%s %s" % (hashtag, count)

if __name__ == '__main__':
    main()
