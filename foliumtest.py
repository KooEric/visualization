import folium
from folium import plugins
import pandas as pd
import matplotlib
from matplotlib import pyplot
import numpy as np
np.set_printoptions(threshold=50)

us = folium.Map(location=[35.543884, 129.256341], zoom_start=12, tiles = 'Cartodb Positron')
minimap = plugins.MiniMap()
us.add_child(minimap)
us_trip=pd.read_csv(r'C:\Users\Atech\Conda_project\울산주요관광지.csv',encoding='utf-8')
us_trip.head(15)
usdf=pd.DataFrame(data=us_trip[0:], columns=['위도','경도'])
des = pd.DataFrame(data=us_trip[0:], columns =['여행지'])

print(usdf.values)
print(des.values)

for i in range(len(usdf)):
    folium.Circle(
        location = usdf.values[i],
        radius = 1000,
        color = '#FF0000',
        fill = 'crimson',
        popup = des.values[i]
    ).add_to(us)
    
folium.PolyLine(usdf, color="#F78181", weight=2.5).add_to(us)
us.save('trip_us.html')