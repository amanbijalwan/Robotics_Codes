# idea for position platform switch with nested loops and other methods
# there are four stations and robot is moving from one to other
# for testing we will start from each station and go to other postions.
# example position 1 goes to 2,3,4 and 2 goes to 1,3,4 and so-on.

# this contains logic for skipping same station access
# adding graphs for visualizations.

import matplotlib.pyplot as plt

#available stations
stn = ["P1","P2","P3","P4"]

#print(stn[2])

print("Task set 1 starting...")
for i in range (0,4):
    print("Test access: ", stn[i])

print("Task set 1 over 2 starting...\n")

xplt = stn
yplt = stn


for i in range (0,4):
    for j in range (0,4):
        if(i==j):
            pass
            plt.plot(stn[i],stn[j],"x:r")
        else:
            print("Station ",stn[i]," is accessing station ",stn[j])
            plt.plot(stn[i],stn[j],"o:b")




plt.title("Station access plot")
plt.xlabel("Accessing Port")
plt.ylabel("Destination Port")
plt.show()