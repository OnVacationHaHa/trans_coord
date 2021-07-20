# trans_coord
What does this code do?

Taking the point containing the latitude and longitude coordinates in the input file as the reference point, the conversion relationship between the X-Y coordinate system and the latitude and longitude coordinate system is deduced, and the latitude and longitude coordinates of the nodes without latitude and longitude are further calculated


What is the conversion relationship between the two coordinate systems?
We consider the latitude and longitude coordinate system as a plane coordinate system. Since both the X-Y coordinate system and the latitude and longitude coordinate system take north as positive direction of Y axis, there is almost no rotation angle between the two coordinate systems. We have established two conversion equations, one is from X axis to longitude, the other is from Y axis to latitude. Both equations are solved with the goal of minimizing the sum of squares of errors. 
