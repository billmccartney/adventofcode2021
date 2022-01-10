import copy


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
    for i in range(0, number_of_bits):
        if bits_high[i] > total/2:  # unsure what should happen when they match...
            gamma |= 1 << i
        else:
            epsilon |= 1 << i
    # print("g=%s e=%s" % (bin(gamma), bin(epsilon)))
    return gamma * epsilon

def bit_mask(bit, number_of_bits):
    return 1 << (number_of_bits - (bit + 1))

def bit_counts_in_list(data, number_of_bits):
    bits_high = [0] * number_of_bits
    bits_low = [0] * number_of_bits
    for row in data:
        for i in range(0, number_of_bits):
            if row & bit_mask(i, number_of_bits):
                bits_high[i] += 1
            else:
                bits_low[i] += 1
    return bits_high, bits_low


def process_file_part2(filename, number_of_bits=5):
    total = 0
    data = []
    with open(filename) as f:
        row = f.readline()
        while row:
            temp = int(row, 2)
            data.append(temp)
            row = f.readline()

    backup_data = copy.deepcopy(data)

    oxygen_generator_rating = 0
    for bit in range(0, number_of_bits):
        bits_high, bits_low = bit_counts_in_list(data, number_of_bits)
        oxygen = 0
        if bits_high[bit] == bits_low[bit]:
            oxygen = bit_mask(bit, number_of_bits)
        elif bits_high[bit] > bits_low[bit]:
            oxygen = bit_mask(bit, number_of_bits)
        if len(data) > 1:
            data = [x for x in data if x & bit_mask(bit, number_of_bits) == oxygen]
        # print(oxygen, bit, [bin(x) for x in data])
    oxygen_generator_rating = data[0]

    data = backup_data
    for bit in range(0, number_of_bits):
        bits_high, bits_low = bit_counts_in_list(data, number_of_bits)
        co2 = 0
        if bits_high[bit] == bits_low[bit]:
            co2 = 0
        elif bits_high[bit] < bits_low[bit]:
            co2 = bit_mask(bit, number_of_bits)

        if len(data) > 1:
            data = [x for x in data if x & bit_mask(bit, number_of_bits) == co2]
        # print(co2, bit, [bin(x) for x in data])
    co2_scrubber_rating = data[0]
    print("oxygen_generator_rating", oxygen_generator_rating)
    print("co2_scrubber_rating", co2_scrubber_rating)
    return oxygen_generator_rating * co2_scrubber_rating


if __name__ == "__main__":
    assert process_file_part1("day3/example.dat") == 198
    output = process_file_part1("day3/raw.dat", number_of_bits=12)
    print("part 1 = ", output)

    assert process_file_part2("day3/example.dat") == 230
    output = process_file_part2("day3/raw.dat", number_of_bits=12)
    print("part 2 = ", output)