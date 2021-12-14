
def process_file_part1(filename, number_of_bits=5):
    total = 0
    bits_high = [0] * number_of_bits
    with open(filename) as f:
        row = f.readline()
        while row:
            temp = int(row, 2)
            total += 1
            for i in range(0, number_of_bits):
                if temp & (1 << i):
                    bits_high[i] += 1
            row = f.readline()
    # Now figure out if we have more than half of the bits for each entry
    gamma = 0
    epsilon = 0
    # print(bits_high, total/2)
    for i in range(0,number_of_bits):
        if bits_high[i] > total/2:  # unsure what should happen when they match...
            gamma |= 1 << i
        else:
            epsilon |= 1 << i
    # print("g=%s e=%s" % (bin(gamma), bin(epsilon)))
    return gamma * epsilon


if __name__ == "__main__":
    assert process_file_part1("day3/example.dat") == 198
    output = process_file_part1("day3/raw.dat", number_of_bits=12)
    print("part 1 = ", output)