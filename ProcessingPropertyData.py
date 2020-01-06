property=raw_input("What property would you like to aggregate")
val = raw_input("What action do you want aggregate information about")
print(val)

dict ={

"lake":{"fixes":5,"repairs":10},
"meadow":{"fixes":6,"repairs":9},
"beach":{"fixes":5,"repairs":8},
"mountain":{"fixes":5,"repairs":6},
"country":{"fixes":3,"repairs":8}
}

collateral= dict[property][val]
print(collateral)


if(val=="repairs"):
if(collateral>5):
print "You should sell the property"

def summing(collateral):
sum = dict["lake"][val]+dict["meadow"][val]+dict["beach"][val]+dict["mountain"][val]+dict["country"][val]
print sum
summing(collateral)

