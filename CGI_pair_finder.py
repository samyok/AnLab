from globals.config import *

print('\n\n' +
      '=========================================\n'
      ' AnLab CGI_pair_finder.py \n' +
      ' Created by Samyok Nepal, 2018. \n' +
      ' Version 1.0.1\n' +
      '\n' +
      ' To find pairs of CGIs for analysis. \n' +
      ' High-high, low-high, high-low and \n'
      ' low-low pairs must be found separately. \n' +
      '\n' +
      ' The output files are in the same form as\n' +
      ' input. \n' +
      '=========================================\n'
      )

# config
# First Island
low = open(folder + config['OUTPUT']['CGIs_LOW'], "r")
# Second Island
high = open(folder + config['OUTPUT']['CGIs_HIGH'], "r")

# outfile
PAIRS = open(folder + config["OUTPUT"]['CGI_PAIRS'], "w")

# We need to run this 4 times -- low-low, high-high, high-low, and low-high


def main(first, second, outfile):
    # input the second cgi island data into a dict bc we are using a mutated struct
    cgi_data = {}

    for line in second:
        chopped = line.split("\t")
        # associate the location and the methylation in a dict.
        cgi_data[chopped[0]] = chopped[1]

    for line in first:
        chopped = line.split("\t")

        # island_start = int(chopped[0])
        island_end = int(chopped[0]) + int(chopped[4])
        pairs = []  # internal, capital is file.
        for key in cgi_data:
            distance = int(key) - int(island_end)
            if 0 < distance < config['INFO']['Single_definition']:
                location_difference = key + "\t" + str(distance)
                pairs.append(location_difference)

        if len(pairs) == 1:
            # needs to be equal to 1 because this means that it only has one CGI that is within 10000 kb of it.
            outfile.write(chopped[0] + "\t" +
                        chopped[4] + "\t" +
                        pairs[0])
            # this prints:
            # location of start first CGI in pair, length first CGI in pair, location of second CGI in pair, distance


files = [low, high]
for i in range(0,2):
    for j in range(0,2):
        main(files[i], files[j], PAIRS)
        print(i,j)

for i in range(0,2):
    files[i].close()

PAIRS.close()
