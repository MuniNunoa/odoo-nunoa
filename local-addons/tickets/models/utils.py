import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from geopy.geocoders import Nominatim
import os

geolocator = Nominatim(user_agent="nunoa", timeout=3, scheme='http')

dir_path = os.path.dirname(os.path.realpath(__file__))

uv_df = gpd.read_file(os.path.join(dir_path, "data/uv/Unidades_Vecinales-polygon.shp"))
uv_df["Name"] = uv_df["Name"].str.strip()
uv_num_df = pd.read_csv(os.path.join(dir_path, "data/uv_num.csv"))
uv_df = uv_df.merge(uv_num_df, on="Name")

cuadrantes_df = gpd.read_file(os.path.join(dir_path, "data/cuadrantes/CUADRANTES.shp"))
cuadrantes_df = cuadrantes_df[cuadrantes_df["COMUNA"]=="NUNOA"]
cuadrantes_df["NUM_CUAD"] = cuadrantes_df["NUM_CUAD"].astype("int")

streets_df = pd.read_csv(os.path.join(dir_path, "data/maestro_calles_nunoa_2018.csv"))

def get_coordinates(address):
  location = geolocator.geocode(address)
  if location:
    return (location.latitude, location.longitude)
  
def geomatch_data(x, y, df, col):
  p = Point(x, y)
  for i, row in df.iterrows():
    if row["geometry"].contains(p):
      return str(row[col])

def get_uv(lat, lon) -> str:
  return geomatch_data(lon, lat, uv_df, "UV")

def get_cuadrante(lat, lon) -> str:
  return geomatch_data(lon, lat, cuadrantes_df, "NUM_CUAD")

def get_street_names():
    street_names = streets_df["NOMBRE_MAESTRO"].str.extract("\w\s(.*)", expand=False).drop_duplicates().sort_values()
    return list(zip(street_names, street_names))