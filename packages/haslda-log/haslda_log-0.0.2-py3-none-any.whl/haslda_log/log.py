import sys
import time

# write log message to log file
def log(msg, source = "unknown", level = "INF", tag=""):

    # open logfile
    logfile = open("log.txt", "a", encoding="utf-8")

    # format name of source
    try:
        # source = str(sys.argv[0]) # get name of source
        source = source.replace("\\", "/")
        source = source[(source.rfind("/") + 1):] # extract name of source file (without the path)
        if len(source) > 20:
            source = "..." + source[-17:] # limit length to 20 digits
    except:
        source = "unknown"
    source = source + (20 - len(source)) * " " # make caller exactly 20 digits long

    tag = tag[:3] # tag is cut to a maximum length of 3 characters
    tag = ( 3 - len(tag) ) * " " + tag # tag length must always be 3 characters

    # write line to logfile
    logfile.write(
        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        + " " + tag
        + " " + source
        + " " + level
        + " --- " + msg + "\n"
        )

# clear log file
def clear():
    logfile = open("log.txt", "w", encoding="utf-8")
    logfile.writelines([])