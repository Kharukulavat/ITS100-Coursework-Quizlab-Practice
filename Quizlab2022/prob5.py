#Problem5 Final labquiz 2022

while True:
    inp = input("Input initial money and interest rate: ")
    if inp == "exit":
        break
    elif inp.isalpha():
        print("Invalid input, please try again.")
        continue
    try:
        m,ir = inp.split()
        m,ir = float(m),float(ir)
        if m > 0 and ir > 0:
            interest = m*(ir/100)
            for i in range(1,6):
                totalmoney = m + interest
                print("YEAR %d --- %.2f + %.2f = %.2f"%(i,m,interest,totalmoney))
                interest = totalmoney*(ir/100)
                m = totalmoney
            print("*****")
        else:
            print("Invalid input, please try again.")
    except:
        print("Invalid input, please try again.")
    