import gmplot
import pandas as pd 
gmap = gmplot.GoogleMapPlotter.from_geocode("Chicago")

df =pd.read_csv('data_1000.csv')

df1 = df[['Latitude','Longitude','Primary Type']] 
 
class1 = df['Primary Type'] == 1 
sf1= df1[class1]
class2 = df['Primary Type'] == 2 
sf2 = df1[class2]
class3 = df['Primary Type'] == 3 
sf3 = df1[class3]
gmap.scatter(sf1['Latitude'], sf1['Longitude'], '#ff0000', size=50, marker=False)
gmap.scatter(sf2['Latitude'], sf2['Longitude'], '#FFA500', size=50, marker=False)
gmap.scatter(sf3['Latitude'], sf3['Longitude'], '#228B22', size=50, marker=False)        
gmap.draw("mymap.html")
