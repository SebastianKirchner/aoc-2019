input = range(357253, 892942 + 1)


def greater_than_check(number):
    last = -1
    equal = False
    for digit in str(number):
        if last < 0:
            last = int(digit)
            continue

        if int(digit) < last:
            return False
        if int(digit) == last:
            equal = True
        last = int(digit)
    return equal


assert greater_than_check(111111) is True
assert greater_than_check(122345) is True
assert greater_than_check(123456) is False
assert greater_than_check(123789) is False
assert greater_than_check(223450) is False

count = 0
for x in input:
    count += greater_than_check(x)

print('Result part 1: ' + str(count))

