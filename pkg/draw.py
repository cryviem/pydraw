import json
from math import hypot
from pkg.logger import log
from pkg.uart import uart


setting = {}

def loadSetting(jsonPath):
    global setting
    with open(jsonPath, 'r') as js:
        setting = json.load(js)
        log.info('Drawing setting %s', setting)


class draw:
    def __init__(self):
        self.cur_x = 0.0
        self.cur_y = 0.0
        loadSetting('./config/drawing.json')
        self.cur_speed = setting.get('speed').get('default')
        self.is_absolute = True
        self.com = uart()

    def updateSpeed(self, mmpm):
        mmps = mmpm / 60
        log.info(mmps)
        if mmps < setting.get('speed').get('min'):
            self.cur_speed = setting.get('speed').get('min')
        elif mmps > setting.get('speed').get('max'):
            self.cur_speed = setting.get('speed').get('max')
        else:
            self.cur_speed = mmps
        log.info('updated speed: %d', self.cur_speed)

    def setAbsolute(self):
        self.is_absolute = True

    def setRelative(self):
        self.is_absolute = False

    def showProperties(self):
        log.info('cur_x %f cur_y %f cur_speed %f', self.cur_x, self.cur_y, self.cur_speed)

    def calcDistance(self, x, y):
        if self.is_absolute:
            dx = x - self.cur_x
            dy = y - self.cur_y 
        else:
            dx = x
            dy - y
        return dx, dy

    def updateCurPos(self, x, y):
        if self.is_absolute:
            self.cur_x = x
            self.cur_y = y
        else:
            self.cur_x += x
            self.cur_y += y
        return dx, dy

    def drawLine(self, x, y):
        dx, dy = self.calcDistance(x, y)
        pathLength = hypot(dx, dy)
        

    def exeGcode(self, gcodePath):
        """ To execute gcode command in the gcodePath file
            line by line """
        try:
            with open(gcodePath, 'r') as gcodeHdr:
                #--- whole logic inside ---
                line_num = 0
                for line in gcodeHdr:    
                    # loop through line in file 
                    line_num += 1
                    # strip out space, \n characters
                    line = line.strip()
                    if not line or line.startswith('#'):
                        # ignore on empty or comment lines
                        continue

                    log.info(str(line_num) + ' ' + line)
                    gc_box = gcode_parse(line)
                    # update speed if F is available
                    if 'F' in gc_box:
                        self.updateSpeed(gc_box.get('F'))
                    
                    gc_cmd = gc_box.get('cmd')
                    if gc_cmd == 'G0':
                        pass
                    elif gc_cmd == 'G1':
                        pass
                    elif gc_cmd == 'G2':
                        pass
                    elif gc_cmd == 'G3':
                        pass
                    elif gc_cmd == 'G90':
                        self.is_absolute = True
                    elif gc_cmd == 'G91':
                        self.is_absolute = False
                    elif gc_cmd == 'M03':
                        pass
                    elif gc_cmd == 'M05':
                        pass


        except Exception as e:
            log.error(e)
        finally:
            log.info('execute gcode terminated')



def draw_test():
    pass




