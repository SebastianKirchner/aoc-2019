original_program = [1, 12, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 6, 1, 19, 1, 19, 9, 23, 1, 23, 9, 27, 1, 10, 27,
                    31, 1, 13, 31, 35, 1, 35, 10, 39, 2, 39, 9, 43, 1, 43, 13, 47, 1, 5, 47, 51, 1, 6, 51, 55, 1, 13,
                    55, 59, 1, 59, 6, 63, 1, 63, 10, 67, 2, 67, 6, 71, 1, 71, 5, 75, 2, 75, 10, 79, 1, 79, 6, 83, 1, 83,
                    5, 87, 1, 87, 6, 91, 1, 91, 13, 95, 1, 95, 6, 99, 2, 99, 10, 103, 1, 103, 6, 107, 2, 6, 107, 111, 1,
                    13, 111, 115, 2, 115, 10, 119, 1, 119, 5, 123, 2, 10, 123, 127, 2, 127, 9, 131, 1, 5, 131, 135, 2,
                    10, 135, 139, 2, 139, 9, 143, 1, 143, 2, 147, 1, 5, 147, 0, 99, 2, 0, 14, 0]

step_size = 4


def run_program(program):
    program = program.copy()
    instruction_pointer = 0
    while instruction_pointer < len(program):
        instruction = program[instruction_pointer]
        if instruction < 1 or instruction > 2:
            break

        address_output = program[instruction_pointer + 3]
        address_operater_l = program[instruction_pointer + 1]
        address_operater_r = program[instruction_pointer + 2]
        if instruction == 1:
            program[address_output] = program[address_operater_l] + program[address_operater_r]
        elif instruction == 2:
            program[address_output] = program[address_operater_l] * program[address_operater_r]
        else:
            break
        instruction_pointer += step_size
    return program


assert run_program([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
assert run_program([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
assert run_program([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
assert run_program([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]

# PART 1

original_program[1] = 12
original_program[2] = 2
result = run_program(original_program)
print('Result part 1: ' + str(result[0]))

# PART 2
expexted_output = 19690720

for noun in range(100):
    for verb in range(100):
        original_program[1] = noun
        original_program[2] = verb
        result = run_program(original_program)
        if result[0] == expexted_output:
            print('Result part 2: ' + str(100 * noun + verb))
            break
