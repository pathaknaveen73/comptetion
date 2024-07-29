# Python program to convert
# JSON file to CSV

''''
import json
import csv


# Opening JSON file and loading the data
# into the variable data

#open
with open('data.json') as json_file:
	data = json.load(json_file)
#-----

data['country']='india'
data['response_status']='Failure'

print(data)
data['domain_name']= "naveen"


print(data)



#save
with open('new.json','w') as file:
	json.dump(data,file)







# now we will open a file for writing
data_file = open('data_file.csv', 'w')

# create the csv writer object
csv_writer = csv.writer(data_file)

# Counter variable used for writing
# headers to the CSV file
count = 0

for emp in employee_data:
	if count == 0:

		# Writing headers of CSV file
		header = emp.keys()
		csv_writer.writerow(header)
		count += 1

	# Writing data of CSV file
	csv_writer.writerow(emp.values())

data_file.close()
'''
# Python program to convert
# JSON file to CSV

 
import json
import csv


# Opening JSON file and loading the data
# into the variable data

#open
with open('khan.json') as json_file:
	data1 = json.load(json_file)
#-----

# data1['country']='india'
# data1['response_status']='Failure'

# print(data1)
# data1['domain_name']= "naveen"

b = data1['0']
# print(b['price'])
b['Status']='processed'
# print(b['price'])
# print(b)
# print([i for i in b])
# print(b['price_symbol'])

# b['price_symbol'] = 'rupees'
# print('-----')

# c = b['countryCount']

# for k in c:
# 	k['country_code']='IN'


# print(data1)



# #save
with open('vivek.json','w') as file:
	json.dump(data1,file)