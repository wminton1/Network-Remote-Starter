# Network-Remote-Starter
Welcome, 

If you are familiar with Batman, this project is pretty simple. On the surface, it's a button controlled starter, but under the hood(pun intended), it's an Embedded Systems-IOT Device.

The inspiration for this project comes from the Son of Batman movie. (https://www.youtube.com/watch?v=47mgPOKKFZk) @1:25, specifically where Batman taps his belt and opens the car.

Considering I live in a residential area and don't have a nuclear car with military ordnance, was to use what I have was an ESP32, WiFi and FordPass. Unfortunately, it wasn't until after I found out Ford doesn't allow such API requests so this project, functionally, was a dud.

ESP32 (C++)
Libraries: WiFi.h, HTTPClient.h

This is the part that would be the belt buckle. I defined the network login credentials and server IP first. From there, I enabled the serial monitor to let me know when each significant event happened.
Then in the main loop, the program waits for a button press. Once the button is pressed, it checks again for a connection to the network, then sends a post out to the network, destination being the (Raspberry Pi) server's IP address on the network.

Server (Python)

This is where the problem initially arose. Not only does Ford generally discourage api use, they actively are restricting people's forpbass accounts for using them.
Still in Development
