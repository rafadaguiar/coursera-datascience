from collections import defaultdict
import sys


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
    words = tweet_file.read().split()
    relative(get_counts(words))


if __name__ == '__main__':
    main()
