#Problem7 Final labquiz2022

freq = {} #to check timestamp frequencies for each employee 
eid_start = {} #to keep the start time value (employee ID : start time)
eid_stop = {} #to keep the stop time value (employee ID : stop time)
eid_worktime = {} #to keep the working time of employee

while True:
    inp = input("Timestamp: ")
    if inp == "done":
        break
    time,eid = inp.split()
    time = time.split(":")
    if eid not in freq:
        freq[eid] = 1
        eid_start[eid] = int(time[0])*60 + int(time[1]) #minutes of start time
    else: 
        freq[eid] += 1
        eid_stop[eid] = int(time[0])*60 + int(time[1]) #minutes of stop time
        eid_worktime[eid] = eid_stop[eid] - eid_start[eid] 
        #Worktime is the difference of start time and stop time
        #Because stop time is always greater than the start time

for k,v in sorted(freq.items()): #to sort employee ID 
    if v > 1: #Condition that timestamp frequency for each employee > 1
        for eid,time in sorted(eid_worktime.items()):
            if k == eid: #To avoid printing duplicated condition of nested for loop
                # So, we let it prints only when the sorted employee ID of these loops is the same
                print("Employee %s working time is %d minutes."%(eid,time))
    else: #when timestamp frequency of employee is only 1
        print("Employee %s working time is undefined."%k)
        

# if eid not in eids:
#         start_h = int(time[0])
#         start_m = int(time[1])
#         eids[eid] = 1
#     elif eid in eids:
#         eids[eid] += 1
#         stop_h = int(time[0])
#         stop_m = int(time[1])
#         worktime = (stop_h - start_h)*60 + (stop_m - start_m)
#         eid_worktime[eid] = worktime

    