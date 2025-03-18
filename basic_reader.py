import sys
from collections import deque

sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')

def print_cleaned_lines(cleaned_text):
    for line in cleaned_text.splitlines():
        print(line)

def text_cleaner(stream):
    res_string = ""
    line_cntr = 0
    prev_preamb = False
    preamb_finished = False
    for line in stream:
        clean_line = ' '.join(line.split())
        if "-----" in clean_line:
            break
        res_string += clean_line + '\n'

        if line_cntr < 10 and not preamb_finished:
            line_cntr+=1
            if not clean_line:
                if prev_preamb:
                    res_string = ""
                    preamb_finished = True
                else:
                    prev_preamb = True
            else:
                prev_preamb = False

    return res_string

def main():
    print_cleaned_lines(text_cleaner(sys.stdin))

if __name__ == "__main__":
    main()