import re

def parse(lines):
    register_re = re.compile('Register (\w): (\d+)\n')
    program_re = re.compile('Program: (.*)\n')
    registers = {}
    program = []
    for line in lines:
        if line:
            if register_re.match(line):
                reg, val = register_re.findall(line)[0]
                registers[reg] = int(val)
            elif program_re.match(line):
                prog = program_re.findall(line)[0]
                program = list(map(int, prog.split(',')))
    return registers, program

def combo(operand, registers):
    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return registers['A']
    elif operand == 5:
        return registers['B']
    elif operand == 6:
        return registers['C']

def run_program(i, registers, program, output=[]):
    if i < len(program):
        opcode = program[i]
        operand = program[i + 1]
        if opcode == 0:
            registers['A'] = registers['A'] // (2 ** combo(operand, registers))
        elif opcode == 1:
            registers['B'] = registers['B'] ^ operand
        elif opcode == 2:
            registers['B'] = combo(operand, registers) % 8
        elif opcode == 3:
            if registers['A'] != 0:
                i = operand - 2
        elif opcode == 4:
            registers['B'] = registers['B'] ^ registers['C']
        elif opcode == 5:
            output.append(combo(operand, registers) % 8)
        elif opcode == 6:
            registers['B'] = registers['A'] // (2 ** combo(operand, registers))
        elif opcode == 7:
            registers['C'] = registers['A'] // (2 ** combo(operand, registers))
        run_program(i + 2, registers, program, output)
        return output 

def one(registers, program):
    print(registers, program)
    output = run_program(0, registers, program)
    return ','.join(str(c) for c in output)

def two(registers, program):
    for i in range(110000000000000, 110000001000000):
        registers['A'] = i
        output = run_program(0, registers, program, [])
        # print(i, output, program)
        if output == program:
            return i

fin = open('d17_in.txt', 'r')
fout = open('d17_out.txt', 'w')

lines = fin.readlines()
registers, program = parse(lines)

fout.write(str(two(registers, program)))

fin.close()
fout.close()
