import geopandas as gpd
from shapely.geometry import Polygon, LineString, Point
    
def process(lat,longi):
    
    try:
        fp="bgd_nhr_drought_barc/bgd_nhr_drought_sparsso.shp"
        data=gpd.read_file(fp)
        point=Point(longi,lat)
        l=data.contains(point)
        found=None
        for i in range(0,len(l)):
            if(l[i]==True):
                found=i
                break

        if found:
            thana_name=data.loc[found,'THANA_NAME']
            drought_class=data.loc[found,'DROU_CLASS']
            drought_class_name=data.loc[found,'DROUGHT_CL']
            return f"Thana Name: {thana_name} \nClass: {drought_class} \nType: {drought_class_name}"
        else:
            return "Coordinate Invalid"
    
    except Exception as e :
        return f" "+e.__class__+" has occured.\n"

    

