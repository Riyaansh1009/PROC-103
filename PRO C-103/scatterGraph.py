import pandas as pd
import plotly.express as pl 


df = pd.read_csv('Data.csv')

fig = pl.scatter(df, x="date", y="cases", color="country")
