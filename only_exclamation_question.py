import sys
from sentence_extractor import read_sentences

def find_only_excl_ques(stream):
    for sentence in read_sentences(stream):
        if '!' in sentence or '?' in sentence:
            yield sentence

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stdin.reconfigure(encoding='utf-8')
    for sentence in find_only_excl_ques(sys.stdin):
        print(sentence)

if __name__ == "__main__":
    main()