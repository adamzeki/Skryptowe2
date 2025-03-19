import sys
import locale
from sentence_extractor import read_sentences

locale.setlocale(locale.LC_ALL, "pl_PL.UTF-8")

def find_sentences_in_lexicographical_order(stream):
    for sentence in read_sentences(stream):
        is_ordered = True
        prev_word = "@"
        for word in sentence.split():
            if word[0].isalpha():
                if locale.strcoll(prev_word, word) > 0:
                    is_ordered = False
                    break
                prev_word = word

        if is_ordered:
            yield sentence


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stdin.reconfigure(encoding='utf-8')
    for sentence in find_sentences_in_lexicographical_order(sys.stdin):
        print(sentence)

if __name__ == "__main__":
    main()