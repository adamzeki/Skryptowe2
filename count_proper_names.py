import sys

def count_sentences_with_proper_names(stream):
    total_sentences = 0
    sentences_with_proper_names = 0

    in_sentence = False
    in_word = False
    first_word = True
    found_proper_name = False

    for char in iter(lambda: stream.read(1), ""):
        if char.isalpha():
            if not in_word:
                in_word = True
                if not first_word and char.isupper():
                    found_proper_name = True
                first_word = False
        else:
            in_word = False

        if char in ".!?":
            if in_sentence:
                total_sentences += 1
                if found_proper_name:
                    sentences_with_proper_names += 1
            in_sentence = False
            first_word = True
            found_proper_name = False

        elif not char.isspace():
            in_sentence = True


    if total_sentences == 0:
        return 0.0

    return (sentences_with_proper_names / total_sentences) * 100

def main():
    result = count_sentences_with_proper_names(sys.stdin)
    print(f"{result:.2f}%")

if __name__ == "__main__":
    main()
