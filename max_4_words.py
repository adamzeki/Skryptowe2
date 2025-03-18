import sys
from sentence_extractor import read_sentences

def find_max_4(stream):
    for sentence in read_sentences(stream):
        if len(sentence.split()) <= 4: #czy usuwac ze splita znaki (-, : itp), zeby nie zapychaly limitu slow
            yield sentence

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stdin.reconfigure(encoding='utf-8')
    for sentence in find_max_4(sys.stdin):
        print(sentence)

if __name__ == "__main__":
    main()