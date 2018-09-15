from globals.config import *
from globals.structs import *

print('\n\n' +
      '=========================================\n'
      ' AnLab Single_CGI_finder.py \n' +
      ' Created by Samyok Nepal, 2018. \n' +
      ' Version 1.0.0\n'+
      '\n' +
      ' I *think* this characterizes as (not)\n single. \n' +
      '\n' +
      ' The output files are in the same form as\n' +
      ' input. \n' +
      '=========================================\n'
      )

single_def = config['INFO']['Single_definition']

cgi_low = open(folder + config['OUTPUT']['CGIs_LOW'], "r")
cgi_high = open(folder + config['OUTPUT']['CGIs_HIGH'], "r")

cgi_low_out = open(folder + config['OUTPUT']['CGIs_LOW_SINGLE'], "w")
cgi_high_out = open(folder + config['OUTPUT']['CGIs_HIGH_SINGLE'], "w")

CGI_FILE = folder + config['INPUT']['CGI_FILE']

print(" Using config.json.\n\n")

# read into cgi_data

fcgi = open(CGI_FILE, "r")
cgi_data = []
for line in fcgi:
    cgi_data.append(CGI(line))
fcgi.close()

# read low_cgis into array (?)
for line in cgi_low:
    current_cgi = CGI
    chopped = line.split("\t")
    current_cgi.start = chopped[0]
    current_cgi.end = chopped[0] + chopped[4]

    good_arr = []
    for i in range(0, len(cgi_data)):
        distance = abs(int(current_cgi.start) - cgi_data[i].start)

        if distance <= single_def:  # CHANGE IN CONFIG.JSON!
            good_arr.append(cgi_data[i].start)

    if len(good_arr) == 1:
        # the below comment was in the pl script. I don't know what this means.
        #  needs to be equal to 1 because the island will be 0 distances from itself.
        cgi_low_out.write(line)

cgi_low.close()
cgi_low_out.close()


# read low_cgis into array (?)
for line in cgi_high:
    current_cgi = CGI
    chopped = line.split("\t")
    current_cgi.start = chopped[0]
    current_cgi.end = chopped[0] + chopped[4]
    current_cgi.number = chopped[5]

    good_arr = []
    for i in range(0, len(cgi_data)):
        distance = abs(int(current_cgi.start) - cgi_data[i].start)

        if distance <= single_def:  # CHANGE IN CONFIG.JSON!
            good_arr.append(cgi_data[i].start)

    if len(good_arr) == 1:
        # the below comment was in the pl script. I don't know what this means.
        #  needs to be equal to 1 because the island will be 0 distances from itself.
        cgi_high_out.write(line)
