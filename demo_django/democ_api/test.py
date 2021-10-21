import datetime

cust_id = int(f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')[:-4]}{1212}")

print(cust_id)
#print(cust_id[-8:])