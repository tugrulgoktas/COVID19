#tugrulrobfinalassignment
#can only import basemap on mac

from flask import Flask, render_template
from mpl_toolkits.basemap import Basemap
import socket 
import pandas as pd
import numpy as np
import pyodbc
import urllib
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import os
import urllib.request, urllib.parse, urllib.error
import ssl
import http
import requests
    

# connect to the data source and create a dataframe
# change column names to avoid SQL errors later
# link = 'http://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-2020-03-21.xlsx'
# df = pd.read_excel(link)
# df = df.rename(columns={'Countries and territories':'Countries'})

# Connect to a SQL Server
# I have run out of Azure credit and the server is now disabled
# server = 'mysqlerverrr.database.windows.net'
# database = 'BDAT1004W20'
# username = 'azureuser'
# password = 'P@ssw0rd'
# driver= '{ODBC Driver 17 for SQL Server}'
# odbc_str = 'DRIVER='+driver+';SERVER='+server+';PORT=1433;UID='+username+';DATABASE='+ database + ';PWD='+ password
# connect_str = 'mssql+pyodbc:///?odbc_connect=' + urllib.parse.quote_plus(odbc_str)
# engine =create_engine(connect_str)
# print("connection is ok")
# create SQL Table on Azure server
# df.to_sql('covid', con = engine,if_exists='replace' ,chunksize = 1000)
# print("table created")  

# creates an unreadable graph of countries and deaths, saves it
# my_path = os.path.dirname(__file__)
# print(my_path)
# df1 = df
# df1.plot(x = 'Countries', y = 'Deaths')
# plt.savefig(('/Users/tugrulgoktas/Desktop/Final Assignment Data Programing/Final Assignment/static/images/Covid 19 Chart 1.png'), bbox_inches='tight')



# Draw the map - can only be run on Apple
# the next two sections make an unreadable map showing circles over cities, not connected to the data source we used before.
# Make a data frame with the latitude and longitude of a few cities:
data = pd.DataFrame({
'lat':[116.4074, 2, 39.9, -3.7, 12.5, 4.8, -0, -77, 13.3],
'lon':[39.9042, 49, 32.8, 40.5, 41.8, 52.3, 51.5, 39, 52.5],
'name':['China', 'France', 'Iran', 'Spain', 'Italy', 'Netherlands', 'United Kingdom', 'United State', 'Germany'],
})

# A basic map
m=Basemap(llcrnrlon=-160, llcrnrlat=-75,urcrnrlon=160,urcrnrlat=80)
m.drawmapboundary(fill_color='#A6CAE0', linewidth=0)
m.fillcontinents(color='grey', alpha=0.7, lake_color='grey')
m.drawcoastlines(linewidth=0.1, color="white")
startlat = 39; startlon = -77
arrlat = 39.9042; arrlon = 116.4074
m.drawgreatcircle(startlon,startlat,arrlon,arrlat, linewidth=1, color='orange')
startlat = 39; startlon = -77
arrlat = 49; arrlon = 2
m.drawgreatcircle(startlon,startlat,arrlon,arrlat, linewidth=1, color='orange')
startlat = 49; startlon = 2
arrlat = 32.8; arrlon = 13.3
m.drawgreatcircle(startlon,startlat,arrlon,arrlat, linewidth=1, color='orange')
startlat = 40.5; startlon = -3.7
arrlat = 52.5; arrlon = 39.9

m.drawgreatcircle(startlon,startlat,arrlon,arrlat, linewidth=1, color='orange')


 
#  Add a marker per city of the data frame!
m.plot(data['lat'], data['lon'], linestyle='none', marker="o", markersize=16, alpha=0.6, c="orange", markeredgecolor="black", markeredgewidth=1)



plt.savefig('COVID-19 EXPAND MAP', bbox_inches='tight')


# Receive Information From WEBSITE.
# x = requests.get("https://tugrulandrobert.000webhostapp.com/wp-content/uploads/2020/03/index1.html")

# print(x.text)

# COnnection between website and program
# weburl = urllib.request.urlopen("https://tugrulandrobert.000webhostapp.com/")
# print("Result code:" + str(weburl.getcode()))
# api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'

# if api_key is False:
#     api_key = 42
#     serviceurl = "https://tugrulandrobert.000webhostapp.com/"
# else :
#     serviceurl = "https://tugrulandrobert.000webhostapp.com/"

# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE


#If you acces provide to WEBSITE, the result would be 200.
# print("Result code:200: Acces was provided between Program and HTML server.")

# app = Flask(__name__, static_url_path='/static')

# @app.route("/")
# def index():
#     return render_template('index.html')
# if __name__ == "__main__":
#     app.run()