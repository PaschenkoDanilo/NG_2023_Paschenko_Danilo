numberOfSecond =int(input("Input number of second: "))

day = numberOfSecond / 86400
daymod = numberOfSecond % 86400
hour = daymod / 3600
hourmod = daymod % 3600
minute = hourmod / 60
minutemod = hourmod % 60
second = minutemod

print (str(int(day)) + " : " + str(int(hour)) + " : " + str(int(minute)) + " : " + str(int(second)))