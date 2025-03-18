import sys
from sentence_extractor import read_sentences

def more_than_1_subordinate(stream):
    ret_sen = ""
    ret_found = False
    for sentence in read_sentences(stream): #moze da sie returnowac od razu po znalezieniu bez broken pipeline; ja znalazlem tylko metode gdzie przechwytujemy ten blad w basic_reader i go obslugujemy, ale chyba tak sie nie powinno robic
        if sentence.count(',') > 1 and not ret_found:
            ret_sen = sentence
            ret_found = True

    return ret_sen

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stdin.reconfigure(encoding='utf-8')
    print(more_than_1_subordinate(sys.stdin))

if __name__ == "__main__":
    main()