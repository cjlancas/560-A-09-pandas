import pandas as pd


player = {
    "Last Name": ["Davis", "Bacot", "Trimble", "Washington", "Lebo", "Landry", "Okonkwo", "Wojcik", "Ingram", "Farris"],
    "First Name": ["RJ", "Armando", "Seth", "Jalen", "Creighton", "Rob", "James", "Paxson", "Harrison", "Duwe"],
    "Height": [72, 83, 75, 82, 73, 76, 80, 77, 79, 79],
    "Weight": [180, 240, 195, 230, 180, 190, 240, 195, 235, 210]
}
data = pd.DataFrame(player)

data["bmi"] = (data["Weight"]/2.205)/((data["Height"]/39.37)**2)

print(data)

data.to_csv("bmi.csv")