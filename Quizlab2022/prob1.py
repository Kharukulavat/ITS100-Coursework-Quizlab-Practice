#Problem1
Park_time = 0
dfee = 0
hfee = 0
days = 0
while True:
    hour = input("A number of hours: ")
    if hour == "done":
        break
    if hour.isnumeric(): #check if hour is number and not negative,float
        hour = int(hour)
        Park_time += hour
        if Park_time > 24:
            daypt = hour // 24
            days += daypt
            dfee += daypt*250
            Park_time -= daypt*24
            if Park_time < 24:
                hourleft = hour % 24
                if hourleft == 1:
                    hfee += 25
                elif hourleft == 2:
                    hfee += 50
                elif hourleft == 3:
                    hfee += 80
                elif hourleft == 4:
                    hfee += 110
                elif hourleft == 6:
                    hfee += 180
                elif 24 > hourleft >= 7:
                    hfee += 250 
        else:
            hourleft = hour % 24
            if hourleft == 1:
                hfee += 25
            elif hourleft == 2:
                hfee += 50
            elif hourleft == 3:
                hfee += 80
            elif hourleft == 4:
                hfee += 110
            elif hourleft == 6:
                hfee += 180
            elif 24 > hourleft >= 7:
                hfee += 250 
        totalfee = dfee+hfee
        if totalfee != 0:
            print("%d days = %d THB."%(days,dfee))
            print("%d hours = %d THB."%(hourleft,hfee))
            print("Total fee is %d THB."%totalfee)
            print("******")
            break
        else:
            print("Invalid input, please try again.")
    else:
        print("Invalid input, please try again.")