# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     t = []
#     for row in data:
#         if row[1] != "temp":
#             t.append(int(row[1]))
#
#     print(t)