def compoundCal( values ):
    p = values[0]
    n = values[1]
    r = values[2]
    t = values[3]
    sum = p * (1 + (r/n)) ** (n*t)
    return sum;

def getValues():
    values = [float(x) for x in input(">>> ").split()]
    while len(values) != 4:
        print("Wrong number of values: ")
        values = [float(x) for x in input().split()]
    return values

print("Enter in Principal interest, the number of years, the rate and times annually: ")
values = getValues()

newValues = compoundCal(values)
print(newValues)

#p = 10000
#n = 12
#r = 0.08
#t = 3
#my_sum = compoundCal(p , n , r , t)
