
def day2_part1_process(filename):
    horizontal = 0
    depth = 0
    with open(filename) as f:
        line = f.readline()
        while(line):
            direction, count = line.strip().split(" ")
            count = int(count)
            if(direction == "forward"):
                horizontal += count
            elif(direction == "up"):
                depth -= count
            elif(direction == "down"):
                depth += count

            line = f.readline()
    return horizontal * depth


def day2_part2_process(filename):
    horizontal = 0
    depth = 0
    aim = 0
    with open(filename) as f:
        line = f.readline()
        while(line):
            direction, count = line.strip().split(" ")
            count = int(count)
            if(direction == "forward"):
                horizontal += count
                depth += aim * count
            elif(direction == "up"):
                aim -= count
            elif(direction == "down"):
                aim += count

            line = f.readline()
    return horizontal * depth


if __name__ == "__main__":
    assert(day2_part1_process("day2/example.dat") == 150)
    print("part1 %d" % day2_part1_process("day2/raw.dat"))
    assert (day2_part2_process("day2/example.dat") == 900)
    print("part2 %d" % day2_part2_process("day2/raw.dat"))