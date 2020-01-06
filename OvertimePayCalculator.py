employees =['raj','ram','shyam','himanshu']

overtime=0
workerpay=[]
totalpay=[]
workinghours=[40,36,24,60]
payrate=[10,9,15,17]
def prompting():
name =raw_input("Please Enter Your Employee Name:")
hoursworked=raw_input("Please Enter Your Hours Worked:")
ratepayed =raw_input("Please Enter Your Rate Paid")
employees.append(name)
workinghours.append(hoursworked)
payrate.append(ratepayed)
print(employees)
print(workinghours)
print(payrate)
x=1 
while(x>0): 
prompting()
break;

def pay(workinghours,payrate):
for i in range(4):
if(workinghours[i]<=40):
totalpay =workinghours[i]*payrate[i]
print totalpay
elif(workinghours[i]>40):
totalpay =(1.5*(workinghours[i]-40)*payrate[i]) +(40*payrate[i])
print totalpay
pay(workinghours,payrate)
