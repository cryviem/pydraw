import os
import logging

# create a custom logger name pyDraw
log = logging.getLogger("pyDraw")
# set input level to DEBUG
log.setLevel(logging.DEBUG)

def initLog(logPath):
    logFile = os.path.join(logPath, 'pydraw.txt')
    if os.path.exists(logFile):
        os.remove(logFile)
    
    # Console logging config
    c_handler = logging.StreamHandler()
    c_handler.setLevel(logging.INFO)
    c_format = logging.Formatter('%(name)s:%(levelname)s: %(message)s')
    c_handler.setFormatter(c_format)
    log.addHandler(c_handler)

    # File logging config
    f_handler = logging.FileHandler(logFile, "w")  
    f_handler.setLevel(logging.DEBUG)
    f_format = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s: %(message)s')
    f_handler.setFormatter(f_format)
    log.addHandler(f_handler)
    log.debug('logger init complete!')