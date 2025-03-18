import sys
from sentence_extractor import read_sentences

def longest_no_neigh(stream):
    max_len = -1
    max_sen = ""
    for sentence in read_sentences(stream):
        no_neigh = True
        prev_let = ""
        for word in sentence.split():
            if word[0].isalpha():
                if prev_let == word[0]:
                    no_neigh = False
                    break
                else:
                    prev_let = word[0]

        if no_neigh and len(''.join(sentence.split())) > max_len:
            max_len = len(''.join(sentence.split()))
            max_sen = sentence

    return max_sen

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stdin.reconfigure(encoding='utf-8')
    print(longest_no_neigh(sys.stdin))

if __name__ == "__main__":
    main()