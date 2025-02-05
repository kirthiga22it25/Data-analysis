import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Creating a synthetic dataset
np.random.seed(42)
countries = ["India", "Nigeria", "Pakistan", "Ethiopia", "Bangladesh", "Democratic Republic of the Congo", 
             "Tanzania", "Sudan", "Afghanistan", "Yemen", "Haiti", "Madagascar", "Mozambique", "South Sudan", "Nepal"]

malnutrition_rates = np.random.uniform(10, 45, len(countries))  # Generating random malnutrition rates

# Creating DataFrame
df = pd.DataFrame({"Country": countries, "Malnutrition Rate (%)": malnutrition_rates})

# Sorting data for better visualization
df = df.sort_values(by="Malnutrition Rate (%)", ascending=False)

# Visualizing the data using a bar chart
plt.figure(figsize=(12, 6))
sns.barplot(x="Malnutrition Rate (%)", y="Country", data=df, palette="Reds_r")

plt.xlabel("Malnutrition Rate (%)")
plt.ylabel("Country")
plt.title("Malnutrition Rates Across Different Countries")
plt.show(

# Creating a Choropleth Map
fig = px.choropleth(df, 
                    locations="Country", 
                    locationmode="country names", 
                    color="Malnutrition Rate (%)", 
                    hover_name="Country", 
                    color_continuous_scale="Reds", 
                    title="Malnutrition Rates Across Different Countries")

fig.show()
