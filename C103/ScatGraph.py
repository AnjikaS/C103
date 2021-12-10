import pandas as pd
import plotly_express as px

data=pd.read_csv("line_chart.csv")
print(data)

figure = px.scatter(data,x="Year",y="Per capita income",size="Per capita income",color="Country",title="Annual Per Capita Income of each Country", size_max=50)
figure.show()