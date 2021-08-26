import requests
import geojson
import geopandas
import os

API = "http://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_110m_land.geojson"


file_name = "temp.geojson"


def write_json(features):
    # feature is a shapely geometry type
    geom_in_geojson = geojson.FeatureCollection(features)
    with open(file_name, 'w') as outfile:
        geojson.dump(geom_in_geojson, outfile)


def get_data_from_api():
    try:
        response = requests.get(API)
        if response.status_code == 200:
            data = response.json()
            print(data.keys())
            write_json(data["features"])

    except Exception as e:
        print(e)


def convert_geojson_to_shp():
    get_data_from_api()
    path = os.path.join(os.getcwd(), "bt.geojson")
    file_g = open(path)
    df = geopandas.read_file(file_g)
    df.to_file('bt.shp')


if __name__ == '__main__':
    convert_geojson_to_shp()
