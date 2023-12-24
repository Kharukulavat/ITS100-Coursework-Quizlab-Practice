#Problem4 Labquiz2022
while True:
    inp = input("Input x,y,z :")
    if inp == "Exit" or inp =="exit":
        print("Program ended.")
        break
    elif inp.isalpha():
        print("Invalid input.")
        continue
    try:
        x,y,z = inp.split(",")
        try:
            x,y,z = float(x),float(y),float(z)
            if x > 0 and y > 0 and z > 0:
                V = (1/3)*((1/2)*x*y)*z
                print("Volume of Tetrahedron is %.2f cubic unit."%V)
            else:
                print("Invalid input.")
        except:
            print("Invalid input.")
    except:
        print("Enter 3 values.")
    