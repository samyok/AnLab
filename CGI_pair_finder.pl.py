from globals.config import *

print('\n\n' +
      '=========================================\n'
      ' AnLab CGI_pair_finder.py \n' +
      ' Created by Samyok Nepal, 2018. \n' +
      ' Version 0.1.5beta\n' +
      ' \n' +
      ' Not too sure if this works :D.\n' +
      ' \n' +
      ' To find pairs of CGIs for analysis. \n' +
      ' High-high, low-high, high-low and \n'
      ' low-low pairs must be found separately. \n' +
      ' \n' +
      ' The output files are in the same form as\n' +
      ' input. \n' +
      '=========================================\n'
      )
# config
# First Island
low = folder + config['OUTPUT']['CGIs_LOW']
# Second Island
high = folder + config['OUTPUT']['CGIs_HIGH']

# outfile
PAIRS = open(folder + config["OUTPUT"]['CGI_PAIRS'], "w")


# We need to run this 4 times -- low-low, high-high, high-low, and low-high


def main(first, second):
    # input the second cgi island data into a dict bc we are using a mutated struct
    counter = 0
    cgi_data = {}
    second_ = open(second, "r")
    for line in second_:
        chopped = line.split("\t")
        # associate the location and the methylation in a dict.
        cgi_data[chopped[0]] = chopped[1]
    second_.close()

    first_ = open(first, "r")
    for line in first_:
        chopped = line.split("\t")

        island_start = int(chopped[0])
        island_end = int(chopped[0]) + int(chopped[4])
        pairs = []  # internal, capital is file.
        for key in cgi_data:
            distance = int(key) - int(island_end)
            if 0 < distance < config['INFO']['Single_definition']:
                location_difference = key + "\t" + str(distance)
                pairs.append(location_difference)

        if len(pairs) == 1:
            counter += 1
            print("> Writing line", counter)
            # needs to be equal to 1 because this means that it only has one CGI that is within 10000 kb of it.
            PAIRS.write(chopped[0] + "\t" +
                        chopped[4] + "\t" +
                        pairs[0] + "\n")
            # this prints:
            # location of start first CGI in pair, length first CGI in pair, location of second CGI in pair, distance
    first_.close()


main(low, high)
main(high, low)
main(low, low)
main(high, high)

PAIRS.close()
