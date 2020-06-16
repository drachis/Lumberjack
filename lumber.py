import datetime
import socket
import getpass
import sqlite3
import os
import pprint
import inspect

#decorator which logs the current user, time and function to commandline and database
def jack(func, *args, **kwargs):
    def log(*args):
        '''
        wrap the decorated function to inspect it's properties
        '''
        # print (
        #     "jack::\nUser: {_user}\nHost: {_host}\nTime: {_time}\nFunction: {_function}\nFile: {_file}".format(
        #     _user = getpass.getuser(),
        #     _host = socket.gethostname(),
        #     _time = str(datetime.datetime.utcnow()),
        #     _function = func.__name__,
        #     _file = __file__
        #     )
        # )
        
        # use inspect to find filename by walking the stack.
        frame = inspect.stack()
        filename = frame[1][0].f_code.co_filename
        sqlCommand = "INSERT INTO logs VALUES ('{_user}','{_host}','{_time}','{_function}','{_file}')".format(
            _user = getpass.getuser(),
            _host = socket.gethostname(),
            _time = str(datetime.datetime.utcnow()),
            _function = func.__name__,
            _file = filename)
        c.execute(sqlCommand)
        connection.commit()
        return func(*args, **kwargs)
    return log

#create or connect to a database adjacent to this file
connection = sqlite3.connect(
    os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 
        "lumberjack_000.db")
        )
c = connection.cursor()

# check if the table we're logging to exists
c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='logs' ''')

# create the a fresh table if it doesn't exist
if not c.fetchone()[0]==1 :
    c.execute("""CREATE TABLE logs
            (user text, host text, time text, function text, file text)
            """)

#minimal example function
@jack
def demoFunction(ab=None):
    if ab:
        return ab + ab
    else:
        return None

def readLogs():
    c.execute("SELECT * FROM logs")
    logs = c.fetchall()
    print("Last 10 logs::")
    pprint.pprint(logs[-10:])

# demo the new found power!
if __name__ == "__main__":
    demoFunction("I'm functional.\n")
    readLogs()
