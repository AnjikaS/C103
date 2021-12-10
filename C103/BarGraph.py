import pandas as pd
import plotly_express as px

df = pd.read_csv("data.csv")
print(df)

Bar = px.bar(df,x="Country",y="Population",title="Total Population of a Country")
Bar.show()