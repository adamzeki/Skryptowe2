import sys

from sentence_extractor import read_sentences


def find_25_longest_sentences(stream):
    """Zwraca listę zdań należących do czwartego kwartylu długości."""
    sentences = list(read_sentences(stream))
    if not sentences:
        return []

    lengths = sorted(len(s) for s in sentences)
    threshold = lengths[int(0.75 * len(lengths))]

    return [s for s in sentences if len(s) >= threshold]

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stdin.reconfigure(encoding='utf-8')
    for sentence in find_25_longest_sentences(sys.stdin):
        print(sentence)

if __name__ == '__main__':
    main()