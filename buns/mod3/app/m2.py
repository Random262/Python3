import sys


def decrypt(line):
    res = ''
    dot_counter = 0
    rev_string = line[::-1]
    for i in rev_string:
        if i != '.':
            if dot_counter >= 2:
                dot_counter -= 2
            else:
                if dot_counter == 1:
                    dot_counter -= 1
                    res += i
                else:
                    res += i
        else:
            dot_counter += 1
    return res[::-1]


if __name__ == "__main__":
    data = sys.stdin.read().strip()
    print(decrypt(data))