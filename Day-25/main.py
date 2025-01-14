# with open("./weather_data.csv") as data:
#     weather = data.readlines()
#     print(weather)

# import csv
#
#
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("./weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].max())
# print(data["temp"].mean())
#
# #Get data in columns
# print(data["condition"])
# print(data.condition)

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print((monday.temp * (9 / 5)) + 32)

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = []
cinnamon = []
black = []

fur_color = data["Primary Fur Color"]
for color in fur_color:
    if color == "Gray":
        gray.append(color)
    if color == "Cinnamon":
        cinnamon.append(color)
    if color == "Black":
        black.append(color)

gray_count = len(gray)
cinnamon_count = len(cinnamon)
black_count = len(black)

squirrel_color = ["Gray", "Cinnamon", "Black"]
squirrel_count = [gray_count, cinnamon_count, black_count]

squirrels = pandas.DataFrame({"Fur Color": squirrel_color, "Count": squirrel_count})

squirrels.to_csv("./squirrel_count.csv")

