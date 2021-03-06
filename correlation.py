import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
  with open(data_path) as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df,x="Days Present",y="Marks In Percentage")
    fig.show()

def getDataSource(data_path):
  Days_Present = []
  Marks_In_Percentage = []
  with open(data_path) as csv_file:
    csv_reader = csv.DictReader(csv_file)
  for row in csv_reader:
    Days_Present.append(float(row["Days Present"]))
    Marks_In_Percentage.append(float(row["Marks In Percentage"]))

  return{"x":Days_Present , "y":Marks_In_Percentage}

def findCorrelation(datasource):
  correlation = np.corrcoef(datasource["x"], datasource["y"])
  print("correlation between Days Present vs Marks In Percentage : \n---v",correlation[0,1])

data_path = "Student Marks vs Days Present.csv"
datasource = getDataSource(data_path)
findCorrelation(datasource)
plotFigure(data_path)