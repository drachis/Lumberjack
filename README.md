# Lumberjack
 Minimal logging of function use as a decorator.

# Useage
    import lumber
    
    @lumber.jack
    def _function():
        pass

# side effects
User, machine, time, function name and funciton file name are logged into an sqlite database. 
The default location for the databse is adjacent to the lumber.py file, this makes it ideal for teams running code from a shared location. 
