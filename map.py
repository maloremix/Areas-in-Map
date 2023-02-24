from flask import Flask, render_template, request, redirect, url_for
from rosreestr2coord import Area
import folium

app = Flask(__name__)
app.config['SECRET_KEY'] = 'our very hard to guess secretfir'

@app.route('/', methods=['GET', 'POST'])
def sign_up():
    infos = []
    if request.method == 'POST':
        areas = []
        s = request.form
        for area in s.values():
            areas.append(Area(area))
        center = areas[-1].get_center_xy()
        mapObj = folium.Map(location=[center[0][0][0][1], center[0][0][0][0]], zoom_start=20)

        for index, area in enumerate(areas, start=1):
            infos.append(area.get_attrs())
            folium.GeoJson(area.to_geojson_poly(), name=f"obj{index}").add_to(mapObj)
        mapObj.save('templates/map.html')
    return render_template('index.html', infos=infos)

@app.route('/map')
def map():
    return render_template('map.html')

# Run the application
app.run(debug=True)
