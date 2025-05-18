import time
months = {1 : "Jan", 2 : "Feb", 3 : "Mar", 4 : "Apr", 5 : "May", 6 : "Jun", 7 : "Jul", 8 : "Aug", 9 : "Sep", 10 : "Oct", 11 : "Nov", 12 : "Dec"}

print("Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation")
result = time.localtime()
print(months[result.tm_mon], result.tm_mday, result.tm_year)
