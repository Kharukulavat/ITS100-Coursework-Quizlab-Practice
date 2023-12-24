probfn = {}
prob = True
while True:
    inp = input("Input: value, prob = ")
    if inp == "done":
        if prob == True:
            print("Output:")
            print("You have a well-defined probability function")
            print(probfn)
            sort = sorted(probfn.values())
            maxv = sort[-1]
            minv = sort[0]
            for k in probfn.keys():
                if maxv == probfn[k]:
                    print(k,"is the value with biggest probability (%.2f)"%maxv)
                elif minv == probfn[k]:
                    print(k,"is the value with smallest probability (%.2f)"%minv)
        else:
             print("Output: Probabilities must be within [0,1]")
    v,p = inp.split(":")
    p = float(p)
    if 1 >= p >= 0:
        if v not in probfn:
            probfn[v] = p
    else:
        prob = False