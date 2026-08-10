from area import rect_area

try:
    len = float(input("Enter the length:  "))
    wid = float(input("Enter the width:  "))
    rect_area(len, wid)
except ValueError as e:
    print(f"{e} You got a ValueError")
except ZeroDivisionError:
    pass
except:
    print("There was some other error")
else:
    print("No errors!!!!")
finally:
    print("This always runs!")
    raise FileNotFoundError

print("The rest of the program!")
