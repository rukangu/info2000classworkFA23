# logs informaiton to file
# a row at a time

import os
import time
print(__name__)
class Logger():
    def __init__(self, filename):
        self.path = filename

        # if it doesn't create it
        if not os.path.exists(filename):
            with open(filename, 'w') as F:
                pass
                ...
                
    def LogRow(self, data):
        t = time.ctime(time.time())
        with open(self.path, 'a') as F:
            F.write(t+","+ data+'\n')

        