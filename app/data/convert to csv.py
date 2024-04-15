import pandas as pd
import json

# Parse the json string to a python dictionary
data = json.loads("data/wordlists.json")

# The desired data is in the `Data` field, use pandas to construct the data frame
df = pd.DataFrame(data["Data"])

# Save to a csv file
df.to_csv("result.csv")