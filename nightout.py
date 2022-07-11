#!/usr/bin/env python3

import random

# TODO: Create dict of key values pairs 
# TODO: Randomly select a key values pair from the array 
# TODO: Print to the console the selected item in the array

restaurants = {'Serafina': 'https://serabythewater.com/', 
               'El Camino':'https://elcaminoftlauderdale.com/', 
               'Shooters Waterfront':'https://www.shooterswaterfront.com/', 
               'Casa Sensai':'https://casasensei.com/' }

selection = key, val = random.choice(list(restaurants.items()))

print(f"Lets go to {selection[0]} tonight. Click this link, {selection[1]} to rsvp...")
