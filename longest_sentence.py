import sys
from sentence_extractor import read_sentences

def find_longest_sentence(stream):
    longest_sent = ""
    max_len = -1
    curr_len = 0
    curr_sen = ""
    for sentence in read_sentences(stream):
        