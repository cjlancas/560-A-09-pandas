import pandas as pd

roster = ["Davis", "Bacot", "Trimble"]
player = {
    "Last Name": roster,
    "First Name": ["RJ", "Armando", "Seth"],
    "Height": [72, 83, 75],
    "Weight": [180, 240, 195]
}
data = pd.DataFrame(player)
print(data)