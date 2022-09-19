

import time

# importing datetime module for now()
import datetime

print("Printed immediately.")
time.sleep(2.4)
print("Printed after 2.4 seconds.")

# using now() to get current time
current_time = datetime.datetime.now()

# Printing value of now.
print ("Time now at greenwich meridian is : "
									, end = "")
print (current_time)
