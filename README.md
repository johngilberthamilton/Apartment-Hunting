# Apartment-Hunting

This is an analysis I conducted as a part of my most recent apartment search. I had recently been reading about OSM and the different API and packages people had developed to make hte data easier to access over the years, and while apartment hunting it hit me how useful it could be to score an apartment based on its colocation to other places of interest. This was especially important to me as I had chosen the Cobble Hill/Brooklyn Heights area based on its proximity to where I play squash (the Eastern Athletic Club).

So I created a list of places I care about: EAC, the Trader Joe's on Court and Atlantic, the Borough Hall subway stop, and the game store where I play Magic: the Gathering sometimes. I then created a grid of long/lat coordinates and scored each one based on its walking distance from each, and aggregated the scores. When thrown into a tableau file, the result is a heat map that I could then use as a reference.

While ultimately more of a fun exercise than anything useful (because 1. I already knew the area pretty well and 2. in NYC you don't really have the opportunity to have access to two equal-quality places that are just a few blocks apart), you could see where it would be useful. If you had never been to a place before, and you wanted to know the optimal place to live (not just the street, but the general neighborhood etc) based on distance from school, work, etc.

I stopped because without a full license you can only make so many calls with the API i'm using, but there are a number of ways to augment this algorithm:
1. distance from a line (not living too close to a main road)
2. driving distance vs walking distance vs subway distance
3. Using other code to pull in more general locations (ie distance from any grocery store as identified by Google or OSM or something)
