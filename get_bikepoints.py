import urllib.request
import json
import pandas as pd

# Define bikepoint URL (from TfL Unified API)
bikepoint_url = "https://api.tfl.gov.uk/BikePoint"

# Request and open bikepoint url
response = urllib.request.urlopen(bikepoint_url)
bikepoints = json.loads(response.read())

# Load json file into a data frame
df = pd.read_json(bikepoint_url, orient='columns')

# Keep id, name and lat/long fields
df.drop(df.columns.difference(['id','commonName','lat','lon']), 1, inplace=True)
df.to_csv("bikepoints.csv",index=False)
