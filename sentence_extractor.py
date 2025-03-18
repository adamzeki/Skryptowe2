import sys

def read_sentences(stream):
    sentence = ""
    in_sentence = False

    for char in iter(lambda: stream.read(1), ""):

        sentence += char
        if not char.isspace() and char not in ".!?":
            in_sentence = True
        if char in ".!?":
            if in_sentence:
                yield ' '.join(sentence.split())
                sentence = ""
                in_sentence = False

    if ' '.join(sentence.split()):  # Ostatnie zdanie (gdy brak kropki na końcu)
        yield ' '.join(sentence.split())


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stdin.reconfigure(encoding='utf-8')
    for i in read_sentences(sys.stdin):
        print(i)

if __name__ == "__main__":
    main()