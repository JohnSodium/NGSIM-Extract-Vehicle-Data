# NGSIM_Record_Adjacent_Vehicle
This program will record data of vehicles that are adjacent to and in front the ego vehicle.
<pre>
These are conditions where we do not record the vehicle:
<pre>
    1. If a vehicle is behind the ego vehicle
    2. If a vehicle on the right or left is too ahead of the ego vehicle
    3. If the vehicle on the right or left is ahead of the vehicle in front
The data we record is the vehicle class, x position, y position, velocity, and acceleration of the ego vehicle and the vehicles in the front, left, and right.
