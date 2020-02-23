import os

number = int(input())

for i in range(number + 1):
    result = ['-' * (number - i)]
    if i < number / 2:
        result.append('*' * (number + i * 2))
        result.append('-' * (number - i * 2))
        result.append('*' * (number + i * 2))
    else:
        result.append('*' * (number))
        result.append('-' * (i * 2 - number))
        result.append('*' * (3 * number - i * 2))
        result.append('-' * (i * 2 - number))
        result.append('*' * (number))

    result.append('-' * (number - i))
    print(''.join(result * 2))

os.system("pause")
