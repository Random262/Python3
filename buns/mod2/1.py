import os


def sum_rss(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()[1:]
    result = 0
    for line in lines:
        columns = line.split()
        rss = int(columns[5])
        result += rss
    units = ['B', 'KiB', 'MiB', 'GiB']
    index = 0
    while result >= 1024:
        result /= 1024
        index += 1
    formatted_result = "{:.2f} {}".format(result, units[index])
    return formatted_result


if __name__ == "__main__":
    path_dir = os.path.dirname(os.path.abspath(__file__))
    f_path = os.path.join(path_dir, "output_file.txt")
    rss = sum_rss(f_path)
    print(rss)
