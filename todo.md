


# To Do or Not to Do:

1. Starting tile, with power, should have Y shape, and so have 3 exits.
2. I have done: added some more 0,3 tiles. And some other shapes. But no 5 ot 6 arms as those are forbiden, we dont have budget for this. I hope tiles are picked at random, not cycle. 
3. UNDO button: there should be button, which would score the last placed tile. And we can press it for -2 score to delete last tile. In case we make some hirrible mstake and shut down last city or something.
4. Storage UI: In UI side there should be 1 storage tile. We can click it to place our tile instead of pile. We could also click storage and bin, to clear it.
5. DRAW ME A RIVER: during map creation pick one of the top row tile, and start a river. River has 2 arms, 1 top, 1 bottom half. It travels in pattern, it jump on next tile at bottom tile, and random pick one of bottom edges, it should be 2,3,4 edges. And it continues untill we reach rock bottom. Placing track on river cost -1 score.
6. LAKE CANT TOUCH THIS. After river we have 4 lake tiles, which are very low prob. But if tile has river it actually is 0.15. Also if our last tile was river the next one also has 0.25 . Generally we want lakes either on river, or big lakes (multi hex). And only 4 total. We cant anything on lakes.
7. When pe place track on city it turns yellow too.
8. We create 2 forest tile, and 2 sawmill tile. Forest is more on left side, sawmill more on right side. We dont have to connect forest and forest. But for each pair we get 10score. UI can have field Forest/Swamil: 0/0. And it gets +1 when we have powered tile. In final score we get min (sawmill/forest) *10. So quite a lot of points. You can draw tiny icon, either small circle with traingle over perimeter inside (sawmill). Or 3 triangles on top of each other (forest) Or just write small text.
9. Once we finish game (last city), game counts loose ends. Edge of map is ok. But if we have track to nowhere that would be -1 score. 
