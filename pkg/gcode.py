from pkg.logger import log

def gcode_parse(line):
    """ Parse Gcode command into a dict of data 
        out {"cmd": str_value,
            "X": float_value,
            "Y": float_value,
            ...} """
    out = dict()
    args = line.split()
    cmd, args = args[0], args[1:]
    out['cmd'] = cmd
    for arg in args:
        # arg forrmat: [Letter][Number...]
        out[arg[0]] = float(arg[1:])

    return out

    
    
