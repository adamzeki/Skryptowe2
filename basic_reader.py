import chardet
import sys
from collections import deque
from chardet import UniversalDetector

def detect_encoding(file_path):
    detector = UniversalDetector()

    with open(file_path, 'rb') as f:
        for line in f:
            detector.feed(line)
            if detector.done:
                break

    detector.close()
    return detector.result

file_path = "brzydkie-kaczatko.txt"
encoding_info = detect_encoding(file_path)

with open(file_path, encoding=encoding_info['encoding'], mode = 'rt') as f:
    sys.stdin = f
    q=deque()
    empty_ctr = 0
    pre_finished = False
    for line in sys.stdin:
        clean_line = ' '.join(line.split())

        if len(q) < 10 and not pre_finished:
            if not clean_line:
                empty_ctr+=1
            else:
                empty_ctr=0
            if empty_ctr >= 2:
                q.clear()
                empty_ctr=0
                pre_finished=True

        if "-----" in clean_line:
            while len(q) > 0:
                print(q.popleft())
            break

        q.append(clean_line)
        if len(q) >= 10:
            print(q.popleft())