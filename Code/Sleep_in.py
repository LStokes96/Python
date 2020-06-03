def sleep_in(weekday,vacation):
    if vacation == True:
        return True
    elif weekday == vacation:
        return True
    else:
        return False

print(sleep_in(True,False))
