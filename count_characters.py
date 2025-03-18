import sys

def count_characters(stream):
    characters_count = 0

    for line in stream:
        non_whitespace_count = sum(1 for char in line if not char.isspace())
        characters_count += non_whitespace_count

    return characters_count

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stdin.reconfigure(encoding='utf-8')
    result = count_characters(sys.stdin)
    print(result)

if __name__ == "__main__":
    main()
