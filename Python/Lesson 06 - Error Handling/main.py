from area import rect_area

try:
    len = float(input("Enter the length:  "))
    wid = float(input("Enter the width:  "))
    rect_area(len, wid)
except ValueError:
    pass
except ArithmeticError:
    print("here's arithmetic")
else:
    print("No errors")
finally:
    print("This will always run")


print("But this printed anyway")