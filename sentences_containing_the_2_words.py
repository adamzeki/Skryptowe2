import sys
from sentence_extractor import read_sentences

def find_sentences_with_the_words(stream):
    word_count=0 #czy to oszczedzi tworzenia n razy zmiennej? czy jest sens tak robic w python
    # Myślę, że to nie ma większego znaczenia
    for sentence in read_sentences(stream):
        has_i = False
        has_oraz = False
        has_ale = False
        has_ze = False
        has_lub = False
        for word in sentence.split():
            if word == 'i':
                has_i = True
            if word == 'oraz':
                has_oraz = True
            if word == 'ale':
                has_ale = True
            if word == 'że':
                has_ze = True
            if word == 'lub':
                has_lub = True

        if has_i + has_oraz + has_ale + has_ze + has_lub > 1:
            yield sentence

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stdin.reconfigure(encoding='utf-8')
    for sentence in find_sentences_with_the_words(sys.stdin):
        print(sentence)

if __name__ == "__main__":
    main()