import folium
import pandas


def color_producer(elevation):
    if elevation < 2000:
        return 'blue'
    elif elevation < 2500:
        return 'red'
    else:
        return 'green'


'''opening data file which contains the information about coordinates'''
data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

map = folium.Map(location=[48, -121], zoom_start=6)

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(
        folium.CircleMarker(
            location=(lt, ln), radius=8,
            popup=str(el) + " metres",
            fill_color=color_producer(el),
            color='grey', fill=True, fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(
    data=open('world.json', 'r',
              encoding='utf-8-sig').read(),
    style_function=lambda x:
    {'fillColor': 'green'
    if x['properties']['POP2005'] < 20000000
    else 'red'
    if 10000000 <= x['properties']['POP2005'] < 50000000
    else 'blue'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
