import pandas as pd
cities_df = pd.read_csv("cities.csv", encoding="utf-8")
cities_df.set_index("City_ID", inplace=True)
print(cities_df.head())
cities_df.to_html("cities_table.html")