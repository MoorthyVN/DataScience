# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import win32com.client as cl
import pandas as pd

#Create a new intance of excel
#excelApp = cl.Dispatch("Excel.Application")
#excelApp.Visible = True

df = pd.read_excel(r"C:\Users\j1013189\OneDrive - Blue Yonder\Personal\DataScienceClass\GitRepo\DataScience\Python\Others\PythonFromExcel\SourceData.xlsx")
#workbook = excelApp.Workbooks.open(r"C:\Users\j1013189\OneDrive - Blue Yonder\Personal\DataScienceClass\GitRepo\DataScience\Python\Others\PythonFromExcel\SourceData.xlsx")

print(df.head())
