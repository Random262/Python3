import json
import subprocess
from collections import defaultdict


def read_logs(file):
    with open(file, 'r') as f:
        logs = [json.loads(line) for line in f]
    return logs


def first_by_level(logs):
    counter = defaultdict(int)
    for log in logs:
        level = log['level']
        counter[level] += 1
    return counter


def second_by_hour(logs):
    counter = defaultdict(int)
    for log in logs:
        time = log['time']
        hour = time.split()[1].split(':')[0]
        counter[hour] += 1
    return counter


def third_critical_by_time():
    try:
        cmd = '''grep '"level": "CRITICAL"' skillbox_json_messages.log | grep '05:0\|05:1\|05:20' '''
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        result = result.stdout.count('\n')
        return result
    except Exception as e:
        return None


def forth_by_dog():
    try:
        cmd = '''grep -c "dog" skillbox_json_messages.log '''
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return None


def fifth_by_warning(logs):
    counter = defaultdict(int)
    for log in logs:
        if log['level'] == 'WARNING':
            message = log['message']
            words = message.split()
            for word in words:
                counter[word] += 1
    return max(counter, key=counter.get)


if __name__ == "__main__":
    file = 'skillbox_json_messages.log'
    logs = read_logs(file)
    print(json.dumps(first_by_level(logs)))
    print(json.dumps(second_by_hour(logs)))
    print(third_critical_by_time(), 'логов уровня CRITICAL было с 5:00 до 5:20')
    print(forth_by_dog(), 'сообщений содержат слово dog')
    print(fifth_by_warning(logs), 'самое частое слово на уровне WARNING')