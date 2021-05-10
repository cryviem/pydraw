import sys, os
from pkg.logger import initLog, log
from pkg.gcode import gcode_parse
from pkg.draw import draw, draw_test
from pkg.uart import com, createUart

# Entry function
def app():
    initLog("./output/")
    intro()
    args = sys.argv[1:]
    if len(args) == 0:
        log.error('no command')    
    else:
        d = draw()
        createUart()
        command, args = args[0], args[1:]
        if command == 'help':
            showHelp()
        elif command == 'gcode':
            try:          
                d.exeGcode(args[0])
            except:
                log.error('gcode: missing file path') 

        elif command == 'test':
            com.send('abcd')
        else:
            log.info("unknown command!")


def intro():
    log.info(" ------------------------------------ ")
    log.info(" -------------- PYDRAW -------------- ")
    log.info(" ------------------------------------ ")

def showHelp():
    log.info("cmd:                 Description")