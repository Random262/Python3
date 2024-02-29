import sys


def get_mean_size():
    lines = sys.stdin.readlines()[1:]
    if not lines:
        print("No files found")
        return
    result = 0
    counter = 0
    for line in lines:
        size = int(line.split()[4])
        result += size
        counter += 1
    if counter == 0:
        print("No files found")
        return
    res = result / counter
    return res


if __name__ == "__main__":
    res_size = get_mean_size()
    if res_size is not None:
        print(res_size)