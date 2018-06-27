print('\n\n' +
      '=========================================\n'
      ' AnLab CGImapper.py \n' +
      ' Created by Samyok Nepal, 2018. \n' +
      ' Version 1.0.0 \n' +
      '\n' +
      ' This takes the CGI data and the \n' +
      ' methylation data and outputs a map \n' +
      '\n' +
      ' The output file is in the form \n' +
      ' (Tab Seperated) \n' +
      '     start location, \n' +
      '     average methylation \n' +
      '     density\n' +
      '     average coverage\n' +
      '     CGI Length \n' +  # @TODO this needs ? to be fixed below.
      '     CPG Number\n' +
      '     Percent CPGs in CGI covered \n' +
      '=========================================\n'
      )

from globals.structs import *  # Make sure you have the globals package!

CGI_FILE = "test_data/test_CGI.txt"
METHLY_FILE = "test_data/test_methlyation.txt"
OUTPUT_FILE = "CGImap.out"

fcgi = open(CGI_FILE, "r")
cgi_data = []
for line in fcgi:
    cgi_data.append(CGI(line))
fcgi.close()

cpg_data = []
fmeth = open(METHLY_FILE, "r")
for line in fmeth:
    cpg_data.append(CPG(line))
fmeth.close()

cpg_data.sort()  # Make sure that the data is sorted by start/location
cgi_data.sort()  # this isn't necessary anymore, but it used to be.

# loop through all the CPGs:
out = open(OUTPUT_FILE, "w")
sum_prev = 0

for island in range(0, len(cgi_data)):
    for i in range(0, len(cpg_data)):
        if cgi_data[island].end >= cpg_data[i].location >= cgi_data[island].start:
            cgi_data[island].add_cpg(cpg_data[i])
            print("                                                                                 ", end="\r")
            print("On island", island, "/", str(len(cgi_data)) + ". Added", len(cgi_data[island].CPGs) - sum_prev,
                  "CPGs to this CGI. ", end="\r")

    # now get final table
    start = cgi_data[island].start
    density = len(cgi_data[island].CPGs) - sum_prev
    if density > 0:
        sum_coverage = 0
        sum_meth = 0
        for cp in range(sum_prev, len(cgi_data[island].CPGs)):
            sum_meth += cgi_data[island].CPGs[cp].percent_meth
            sum_coverage += cgi_data[island].CPGs[cp].coverage
        average_meth = sum_meth / float(density)
        average_coverage = sum_coverage / float(density)
        cgi_length = cgi_data[island].end - cgi_data[
            island].start  # @TODO this needs to be fixed -- +1? Will this effect anything?
        cpg_num = cgi_data[island].number
        percent_cpgs_covered = density / cgi_data[island].number * 100

        out.write(str(start) + "\t" +
                  str(average_meth) + "\t" +
                  str(density) + "\t" +
                  str(average_coverage) + "\t" +
                  str(cgi_length) + "\t" +
                  str(cpg_num) + "\t" +
                  str(percent_cpgs_covered) + "\n")
    sum_prev += density
out.close()
print("                                                                                                               ")
last = "Done! Outputted Mapped results to " + OUTPUT_FILE + "!                                                       \n"
print(last)
