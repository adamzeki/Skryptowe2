import sys

from sentence_extractor import read_sentences


def find_sentences_in_lexicographical_order(stream):
    for sentence in read_sentences(stream):
        is_ordered = True
        prev_word = "@" #earlier than 'A' in ascii table
        for word in sentence.split():
            if word[0].isalpha():
                if prev_word > word.upper():
                    is_ordered = False
                    break

                prev_word = word.upper()


        if is_ordered:
            yield sentence


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stdin.reconfigure(encoding='utf-8')
    for sentence in find_sentences_in_lexicographical_order(sys.stdin):
        print(sentence)

if __name__ == "__main__":
    main()