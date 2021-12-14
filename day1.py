
def processFilePart1(filename):
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


if __name__ == '__main__':
    # Ensure the test data passes
    assert(processFilePart1("day1/example.dat") == 7)
    # process the new data
    output = processFilePart1("day1/raw.dat")
    print("Part 1: raw.dat contains %d increases" % output)

