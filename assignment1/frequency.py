from collections import defaultdict
import sys
import json


def parser_words(response):
    words = []
    for line in response:
        result = json.loads(line.strip())
        if 'text' in result.keys():
            words += result['text'].encode("utf8").split()
    return words


def get_counts(seq):
    counts = defaultdict(int)
    for x in seq:
        counts[x] += 1
    return counts


def relative(freqdict):
    for k in freqdict.keys():
        freqdict[k] = float(freqdict[k])/len(freqdict)
        print "%s %f" % (k, freqdict[k])


def main():
    tweet_file = open(sys.argv[1])
    words = parser_words(tweet_file)
    relative(get_counts(words))


if __name__ == '__main__':
    main()
