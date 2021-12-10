import pandas as pd
import plotly_express as px

data=pd.read_csv("data.csv")
print(data)

figure = px.scatter(data,x="InternetUsers",y="Population",size="Percentage",color="Country",title="Total Internet Users in a Country",size_max=60)
figure.show()