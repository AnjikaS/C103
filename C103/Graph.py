import pandas as pd
import plotly_express as px

df = pd.read_csv("line_chart.csv")
print(df)

figure = px.bar(df,x="Year",y="Per capita income",title='Per Capita Income Graph')
figure.show()
