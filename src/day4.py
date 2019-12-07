from functools import reduce

input = range(357253, 892942 + 1)
required_length = 6


def input_check(number):
    number_string = str(number)
    if len(number_string) != required_length:
        return False

    digit_set = set(list(number_string))
    if len(digit_set) == len(number_string):
        return False

    last = -1
    counts = {}

    for x in number_string:
        if x not in counts:
            counts[x] = 1
        else:
            counts[x] = counts[x] + 1

        if last < 0:
            last = int(x)
            continue

        x = int(x)
        if x < last:
            return False
        last = x

    if 2 not in counts.values():
        return False

    return True

assert input_check(112233) is True
assert input_check(111122) is True
assert input_check(122345) is True
assert input_check(111111) is False
assert input_check(124444) is False
assert input_check(123444) is False
assert input_check(123456) is False
assert input_check(123789) is False
assert input_check(223450) is False
assert input_check(987654) is False

result = reduce(lambda x, y: x + y, map(input_check, input))
print('Result part 2: ' + str(result))
