from pydoc import describe

import  pandas as pd

data = pd.read_csv("weather_data.csv")
data.describe()

# print(data.day)
# print(data["day"])

# days_of_the_week = data.day
# week =pd.DataFrame(days_of_the_week)
# print(week)
# week.to_csv("days_of_week")


