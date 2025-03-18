import sys
from sentence_extractor import read_sentences

def get_first_20(stream):
    counter=0
    for sentence in read_sentences(stream):
        if counter < 20:
            yield sentence
            counter+=1


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stdin.reconfigure(encoding='utf-8')
    for sentence in get_first_20(sys.stdin):
        print(sentence)

if __name__ == "__main__":
    main()