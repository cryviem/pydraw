import sys, os
from pkg.logger import initLog, log
from pkg.gcode import gcode_parse

# Entry function
def app():
    initLog("./output/")
    intro()
    args = sys.argv[1:]
    if len(args) == 0:
        log.error('no command')    
    else:
        command, args = args[0], args[1:]
        if command == 'help':
            showHelp()
        if command == 'gcode':
            try:
                normal_work(args[0])
            except:
                log.error('gcode: missing file path') 
        else:
            log.info("unknown command!")



def normal_work(gcodePath):
    try:
        with open(gcodePath, 'r') as gcodeHdr:
            #--- whole logic inside ---
            line_num = 0
            for line in gcodeHdr:     
                line_num += 1
                # strip out space, \n characters
                line=line.strip()
                if not line or line.startswith('#'):
                    # ignore on empty or comment lines
                    continue

                log.info(str(line_num) + ' ' + line)
                gcode_parse(line)

    except Exception as e:
        log.error(e)
    finally:
        log.info('normal_work terminated')


def intro():
    log.info(" ------------------------------------ ")
    log.info(" -------------- PYDRAW -------------- ")
    log.info(" ------------------------------------ ")

def showHelp():
    log.info("cmd:                 Description")