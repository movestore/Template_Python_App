Set of input data to test apps.

*Content*
- input1: 1 goat, median fix rate = 30mins, tracking duration 7.5 month, gps, local movement
- input2: 3 storks, median fix rate = 1sec, tracking duration 2 weeks, gps, local movement
- input3: 1 stork, median fix rate = 1h | 1day | 1 week, tracking duration 11.5 years, argos, includes migration
- input4: 3 geese, median fix rate = 1h | 4h, tracking duration 1.5 years, gps, includes migration

*I/O types*
- all data sets are provided as 'MovingPandas.TrajectoryCollection'


*Projection*
- data are provided in "lat/long" (EPSG:4326) and projected to "Mollweide" (ESRI:54009) in order to test your app accordingly for not projected and projected data. If your app does not allow projected data or only can deal with projected data, document and either build a automatic transformation in the app or make it fail with an informative error message. The app "Change projection" can be refered to for the user to change the projection of the data acordingly previous to your app.

*File names*
input1_LatLon.pickle
input1_Mollweide.pickle

input2_LatLon.pickle
input2_Mollweide.pickle

input3_LatLon.pickle
input3_Mollweide.pickle

input4_LatLon.pickle
input4_Mollweide.pickle


