list = []
for i in range(4):
    a = int(input("Hour/Minutes : ")) 
    list.append(a)
    
hour = int(list[0])
minute = int(list[1])
hourout = int(list[2])
minuteout = int(list[3])
thour = abs(int(list[0]) - int(list[2]))
tmin = abs(int(list[1]) - int(list[3]))

if hour < 7 or (hourout == 23 and minuteout !=0):
    print()
else:
    
    price = 0
    if minuteout < minute:
        thour -= 1
        tmin += 60
    if thour == 0 and tmin <= 30:
        price = "Free" 
    if (1 <= thour <= 2) or (thour == 0 and tmin > 30):
        thour += 1
        tmin = 0
        price = 10*thour
        price += 10 if tmin != 0 and thour < 2 else 0
    if (4 < thour <= 6) or (thour == 4 and tmin != 0):
        price = 20*(thour-3) + 30
        price += 20 if tmin != 0 else 0
    if thour > 6 or (thour == 6 and tmin != 0):
        price = 300
    
print("You parked your car for:", thour, "Hour", tmin, "Minute", "Price:", price)