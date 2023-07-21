def ask_ok(value,retries=4,reminder='please try again'):
    "writing to check defualt arguments"
    while True:
        ok=value
        if ok in ('y','yes','ye'):
            return True
        if ok in ("n","no","nope","nop"):
            return False
        retries=retries-1
        if retries<0:
            print("invalid user response")
        print(reminder)
        

print(ask_ok("ooo"))