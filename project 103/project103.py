from turtle import color
import pandas as ps
import plotly.express as px

#read file is one variable to store data frame we can get it by pandas
readfile=ps.read_csv("scatter chart.csv")
scattergraph=px.scatter(readfile,x='date',y='cases',size='cases',color='country',)

scattergraph.show()