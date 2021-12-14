

def process_file_part1(filename):
    count = 0
    with open(filename) as f:
        last = f.readline().strip() # Prime the pump by reading the first row
        row = f.readline().strip() # setup the first comparison
        while row: # if there are still more lines, keep going...
            if int(last) < int(row):
                count += 1
            last = row
            row = f.readline().strip()

    return count


class process_file_part2:
    window = []
    count = 0
    def add_element(self, item):
        self.window = self.window[1:3] + [item]
        return int(sum(self.window))
    def process(self, filename):
        with open(filename) as f:
            count = 0
            # First build the window...
            self.window = [int(f.readline().strip()), int(f.readline().strip()), int(f.readline().strip())]
            last = int(sum(self.window))  # initial window values
            row = f.readline().strip()
            while row:  # if there are still more lines, keep going...
                value = self.add_element(int(row))
                if last < value:
                    count += 1
                last = value
                row = f.readline().strip()
        return count



if __name__ == '__main__':
    # Ensure the test data passes
    assert(process_file_part1("day1/example.dat") == 7)
    assert(process_file_part2().process("day1/example.dat") == 5)
    # process the new data
    output = process_file_part1("day1/raw.dat")
    print("Part 1: raw.dat contains %d increases" % output)
    output = process_file_part2().process("day1/raw.dat")
    print("Part 2: raw.dat contains %d increases" % output)
