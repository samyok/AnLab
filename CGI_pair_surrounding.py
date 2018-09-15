from globals.config import *
from globals.structs import *
# Full disclosure: This file is the one I feel most unsure of as of 6/29/18 15:19:06.

print('\n\n' +
      '=========================================\n'
      ' AnLab CGI_pair_surrounding.py \n ' +
      ' Created by Samyok Nepal, 2018. \n ' +
      ' Version 0.0.3dev \n' +
      ' \n ' +
      ' To find the surrounding CpG methylation \n for pairs.'
      ' \n ' +
      ' The output files are in the same form as\n' +
      ' input. \n' +
      '=========================================\n'
      )

meth_file = open(folder + config['INPUT']['METHLYATION_FILE'], "r")
cpg_data = []
for line in meth_file:
    cpg_data.append(CPG(line))
meth_file.close()

pairs = open(folder + config['OUTPUT'][''])