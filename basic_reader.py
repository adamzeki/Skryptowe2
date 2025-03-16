import chardet
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

f = open(file_path, encoding=encoding_info['encoding'], mode = 'rt')
print(f.read())