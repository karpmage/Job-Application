"""
I perform a mean filter on the data using 1 adjacent data point on each side.

A median filter would work better for removing outliers, but this data set
doesn't seem to have any.

I attained the data from:
https://machinelearningmastery.com/time-series-datasets-for-machine-learning/
and it is the "Shampoo Sales Dataset".
"""

import json
import matplotlib.pyplot as plt
import statistics

# Loads in the json data
with open('distros.json', 'r') as f:
    distros_dict = json.load(f)
    
# I put the original sales values in a list
value_list = []
for key in distros_dict:
    value_list += [float(key['Value'])]

# I compute the mean values and put them in a new list    
new_value_list = []
new_value_list += [(value_list[0]+value_list[1])/2]
for i in range(1,len(value_list)-1):
    new_value = (value_list[i-1]+value_list[i]+value_list[i+1])/3
    new_value_list += [new_value]
new_value_list += [(value_list[-2]+value_list[-1])/2]


# The unfiltered graph is black
# The filtered graph is red
plt.plot(value_list, 'black')
plt.plot(new_value_list, 'red')
plt.ylabel('Sales')
plt.xlabel('Month')
plt.show()

minimum = min(new_value_list)
print("minimum:", "{:.1f}".format(minimum))
total = 0
n = 0
for element in new_value_list:
	total += element
	n += 1
mean = total/n

print("mean:", "{:.1f}".format(mean))

#By "average", I assume you mean "median"

median = statistics.median(new_value_list)
print("median:", "{:.1f}".format(median))

"""
{
   "$schema": "http://json-schema.org/draft-04/schema#",
   "title": "Product",
   "description": "A graph of Shampoo product sales over time",
   "type": "object",
	
   "properties": {
	
      "Date": {
         "description": "Gives the month and year",
         "type": "string"
      },
		
      "Value": {
         "description": "Shampoo product sales",
         "type": "float"
      }
}
}
"""
