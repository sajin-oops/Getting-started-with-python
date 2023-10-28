print("Basic I/O programming")
print("*********************")
n = int(input("enter no of processes:"))
print("No of Processes=",n)
a_time = []
b_time = []
for x in range(n):
 print("enter the arrival time of process p{}".format(x+1))
 a = int(input())
 a_time.append(a)
print("arrival time of the processes:",a_time)
for x in range(n):
 print("enter the burst time of process p{}".format(x+1))
 a = int(input())
 b_time.append(a)
print("burst time of the processes:",b_time)
print("Pno\t\t AT\t\t BT")
for i in range(n):
 print("p{}".format(i+1),"\t\t",a_time[i],"\t\t",b_time[i])
