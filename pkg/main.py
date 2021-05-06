import sys, os
from pkg.log import initLog, log

# Entry function
def app():
    initLog("./output/")
    intro()
    args = sys.argv[1:]
    if len(args) == 0:
        log.info('normal operation --> ')
    else:
        command, args = args[0], args[1:]
        if command == 'help':
            showHelp()
        else:
            log.info("unknown command!")





def intro():
    log.info(" ------------------------------------ ")
    log.info(" -------------- PYDRAW -------------- ")
    log.info(" ------------------------------------ ")

def showHelp():
    log.info("cmd:                 Description")