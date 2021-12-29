import pandas as pd
import numpy as np
import math as math
import openrouteservice as ors
import folium
import time
 

client = ors.Client(key='5b3ce3597851110001cf624811452552dc044532b2ea5cc57fb4bbcc')

 

#testing- using their example

coordinates = [[13.42731, 52.51088], [13.384116, 52.533558]]
route = client.directions(
    coordinates=coordinates,
    profile='foot-walking',
    validate=False,
)

 

print(route['routes'][0]['summary'])

 

#testing- going from the strat to squash

coordinates2 = [[-73.994087, 40.697827], [-73.995659, 40.682767]]

route = client.directions(

    coordinates=coordinates2,

    profile='foot-walking',

    validate=False,

)

 

print(route['routes'][0]['summary'])

 


 

#start southwest- that way adding is going north east

#do a 15 by 15- adding .001 each time

coord_zero = [-74.00181, 40.68141]

coord_strat = [-73.99562, 40.68277]

coord_squash = [-73.994239, 40.697816]

coord_tj = [-73.99254, 40.68956]

coord_train = [-73.990391, 40.693847]

    
 
df = pd.DataFrame(columns = ['lat', 'long', 'dist2strat', 'dist2squash', 'dist2tj', 'dist2train'])
for i in range(15):
    for j in range(15):
        coord_cur = [round(coord_zero[0] + i*.001, 5), coord_zero[1] + j*.001]
        print(coord_cur)
        dist2strat = client.directions(coordinates=[coord_cur, coord_strat], profile='foot-walking',validate=False,)['routes'][0]['summary']['distance']
        dist2squash = client.directions(coordinates=[coord_cur, coord_squash], profile='foot-walking',validate=False,)['routes'][0]['summary']['distance']
        dist2tj = client.directions(coordinates=[coord_cur, coord_tj], profile='foot-walking',validate=False,)['routes'][0]['summary']['distance']
        dist2train = client.directions(coordinates=[coord_cur, coord_train], profile='foot-walking',validate=False,)['routes'][0]['summary']['distance']
        new_row = {'lat':coord_cur[1], 'long':coord_cur[0], 'dist2strat':dist2strat, 'dist2squash':dist2squash, 'dist2tj':dist2tj, 'dist2train':dist2train}
        df = df.append(new_row, ignore_index = True)
        time.sleep(7)
df.to_csv('C:/Users/jgh67/Documents/location_optimizer.csv')
