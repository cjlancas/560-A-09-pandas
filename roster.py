import pandas as pd

roster = ["Davis", "Bacot", "Trimble"]
player = {"Last Name": roster}
data = pd.DataFrame(player)
print(data)