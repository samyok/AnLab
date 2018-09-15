from globals.config import *

print('\n\n' +
      '=========================================\n'
      ' AnLab high_low_split.py \n' +
      ' Created by Samyok Nepal, 2018. \n' +
      ' Version 1.0.0 \n' +
      '\n' +
      ' This characterizes our islands as low or\n' +
      ' high, and designates those that are \n' +
      ' single. Distance for single CGIs can be\n' +
      ' changed. \n' +
      '\n' +
      ' The output files are in the same form as\n' +
      ' input. \n' +
      '=========================================\n'
      )

high = open(folder + config['OUTPUT']['CGIs_HIGH'], "w")
low = open(folder + config['OUTPUT']['CGIs_LOW'], "w")
with open(folder + config['OUTPUT']['CGI_MAP']) as MAPPED:
    for line in MAPPED:
        data = line.split("\t")
        if float(data[1]) <= 20:
            low.write(line)
        elif float(data[1]) >= 80:
            high.write(line)
high.close()
low.close()
