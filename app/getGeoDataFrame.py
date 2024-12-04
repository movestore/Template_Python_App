# showcase for defining functions in a file other than ./app/app.py 

import logging
from movingpandas import TrajectoryCollection
from geopandas.geodataframe import GeoDataFrame

def get_GDF(data: TrajectoryCollection) -> GeoDataFrame:

    logging.info("Translating to GeoDataFrame")
      
    # Transfer the data to a GeoDataFrame
    data_gdf = data.to_point_gdf()
    
    # Return the data
    return data_gdf
