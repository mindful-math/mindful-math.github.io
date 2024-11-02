+++
author = "Someone"
title = "networkSwitching"
date = "2024-11-02"
description = "networkSniffer"
math = true
+++

- [How  do we move data through a network?](#how--do-we-move-data-through-a-network)
- [Delays in Packet-Switched networks](#delays-in-packet-switched-networks)
- [references](#references)


## How  do we move data through a network?

There are two primary answers that emerged in the late 90s that I'd like to discuss below metaphorically speaking.

> Circuit switching: the resources needed along a path (buffers, link transmission rate) to provide communication between two nodes are reserved for the duration of the communication session.

The analogy is restaurants that only take reservations. As a consumer, this is nice if you do not mind planning in advance to reserve the restaurant's resources (and you theoretically don't need to wait once you get there). BUT, consider the case of ties in reservations - it goes to the highest bidder/biggest pockets in capitalistic economies. Also, it's a pain in the butt to add this overhead each time to reserve resources. Restaurants generally do a blend of both because if they only took reservations, then there could be significant gaps of service/potential revenue and so the analogy is a simplification.

> In packet-switched networks, resources are not reserved and are first come, first serve (i.e. a queue is instantiated for those waiting to establish a communication link).

Borrowing the metaphor above, you can imagine that with more budget-friendly restaurants, they do not actually gain much by selectively choosing the highest bidder and instead rely on the voluume of orders to compound revenue and make money. Customers enjoy the convenience this affords (for not having to plan so far in advance), but this can of course bite if they have to wait in long lines to get their food. It all boils down to the velocity of orders (ice cream is easy, sushi might be slow and difficult as you increase customers arriving simultaneously).

## Delays in Packet-Switched networks

> Processing delay: time required to look at a packet's header and determine where to direct the packet

To carry on our analogy, this is like a person plugging in the directions to the restaurant in Google Maps. Back in the old days without Google Maps, this might add some serious overhead to get to restaurants in more urban environments but not today (similarly the actual packet delay is microseconds or less these days).

> Queueing delay: if it arrives at a queue, this is the time a packet must wait to be transmitted onto the link

So after the person has plugged in the directions to Google Maps and gets to the restaurant, this is the time the person must wait in line to be seated. Remember that packet-switched restaurants do not take reservations! For popular restaurants, this could add quite the delay (in milliseconds).

> Transmission delay: the amount of time required to transmit all of the packet's bits in the link

This is equivalent to the time required by the waiter and chef to decode the customer's order. As you increase the size and complexity of items on the menu ordered, you increase the time you will be waiting as the waiter helps transmit this to the chef to bring into reality.

> Propagation delay: the time required to propagate from the begining of the link to the router desired

Distinct from transmission delays, propogation delays could be equivalent to the physical distance from the chef to the customers. At a sushi bar, you're propogation delay is near zero, but if you're at a multi-level restaurant with spacious seating there could be a little overhead to send the message to the chef.

The analogy is missing some details, but I think does a good job at providing the gist of delays in packet-switched networks.

## references
- [Computer Networking by Kurose & Ross](https://gaia.cs.umass.edu/kurose_ross/index.php)
