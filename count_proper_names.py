import sys
from sentence_extractor import read_sentences

def count_sentences_with_proper_names(stream):
    total_sentences = 0
    sentences_with_proper_names = 0

    for sentence in read_sentences(stream):
        total_sentences+=1
        in_word = False
        first_word = True

        for char in sentence:
            if char.isalpha():
                if not in_word:
                    in_word = True
                    if not first_word and char.isupper():
                        sentences_with_proper_names += 1
                        break
                    first_word = False
            else:
                in_word = False

    if total_sentences == 0:
        return 0.0

    return (sentences_with_proper_names / total_sentences) * 100

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stdin.reconfigure(encoding='utf-8')
    result = count_sentences_with_proper_names(sys.stdin)
    print(f"{result:.2f}%")

if __name__ == "__main__":
    main()
