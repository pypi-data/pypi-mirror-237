This package provides a simple logging functionality.
In the current version it allows you to
- post log messages that are added in a local file (log.txt)
- completely clear the log file

The package provides two functions:

### Posting a log message
log("message")
optional params are
- source: i.e. the __file__ variable
- level: i.e. "ERR", default is "INF"

### Clearing the log file
clear()
no params