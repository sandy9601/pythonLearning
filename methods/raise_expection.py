class Error(Exception):
    pass
class PrintError(Error):
    def __init__(self,message):
        self.message=message

try:
    print("hi there")
    raise PrintError("error while printing")
except PrintError as  e:
    print("print error occured",e)
finally:
    print("from finally")

