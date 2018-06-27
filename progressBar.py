from progress.bar import *
import time

bar = Bar('Processing', max=1000000)
for i in range(0,1000000):
    # time.sleep(0.01)
    bar.next()

bar.finish()