import random
import subprocess

count = 0
result_line = 1
queued_str = set()
memo = set()
while True:
    n = random.choice([0, 1])
    if n == 0:
        oji_str = subprocess.check_output(['ojichat', '花子'])
        # remove white space
        oji_str = oji_str.replace(b' ', b'')
        if oji_str in memo:
            continue
        memo.add(oji_str)
        queued_str.add(oji_str)
        print(f'{result_line}日目 太郎->花子 {oji_str.decode("utf-8")}', end='')
        result_line += 1
        count += 1
    else:
        if count > 0:
            re = random.choice(list(queued_str))
            queued_str.remove(re)
            print(f'{result_line}日目 花子->太郎 Re:{re.decode("utf-8")}', end='')
            result_line += 1
            count -= 1
    if result_line == 1001:
        break
