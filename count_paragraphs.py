import sys


def count_paragraphs(stream):
    paragraph_count = 0
    in_paragraph = False

    for line in stream:
        clean_line = line.strip()

        if clean_line:
            if not in_paragraph:
                paragraph_count += 1
                in_paragraph = True
        else:
            in_paragraph = False

    return paragraph_count


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stdin.reconfigure(encoding='utf-8')
    result = count_paragraphs(sys.stdin)
    print(result)


if __name__ == "__main__":
    main()
