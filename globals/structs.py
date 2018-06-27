class CGI(object):
    start = end = number = 0  # initialize variables
    CPGs = []

    def add_cpg(self, cpg):
        if self.start <= cpg.location <= self.end:
            self.CPGs.append(cpg)
        return 0

    def __init__(self, string):  # TAB DELIMITED
        arr = string.split()
        self.start = int(arr[0])
        self.end = int(arr[1])
        self.number = int(arr[2])  # number of CPGs

    def __lt__(self, other):
        return self.start < other.start


class CPG(object):
    location = percent_meth = coverage = 0

    def __init__(self, string):
        arr = string.split()
        self.location = int(arr[0])
        self.percent_meth = float(arr[1])
        self.coverage = int(arr[2])

    def __lt__(self, other):
        return self.location < other.location
