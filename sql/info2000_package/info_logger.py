import time
import os

# print ("In the info logger module!!" + __name__)


class Logger():
    def __init__(self, filename):
        self.filename = filename

        # make sure that the file exists

        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as F:
                pass   


    def LogRow(self, data):
        with open(self.filename, 'a') as f:
            # current time
            # t = time.time()
            t = time.ctime(time.time())

            f.write(f"{t}, {data} \n")
