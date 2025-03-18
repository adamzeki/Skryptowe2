import sys
from sentence_extractor import read_sentences

def find_longest_sentence(stream):
    max_sent = ""
    max_len = -1
    for sentence in read_sentences(stream):
        if len(''.join(sentence.split())) > max_len:
            max_len = len(''.join(sentence.split()))
            max_sent = sentence

    return max_sent

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stdin.reconfigure(encoding='utf-8')
    print(find_longest_sentence(sys.stdin))

if __name__ == "__main__":
    main()