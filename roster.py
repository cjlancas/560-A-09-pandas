import pandas as pd

roster = ["Davis", "Bacot", "Trimble"]
player = {
    "Last Name": roster,
    "First Name": ["RJ", "Armando", "Seth"],
    "Height": [72, 83, 75],
    "Weight": [180, 240, 195]
}
data = pd.DataFrame(player)

data["bmi"] = (data["Weight"]/2.205)/((data["Height"]/39.37)**2)

print(data)

data.to_csv("bmi.csv")