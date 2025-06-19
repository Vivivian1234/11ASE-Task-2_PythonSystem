# Assessment_Task_2-PythonSystem

This is a python powered text-based adventure game, where you are trapped in an escape room and you must find the 3 keys to escape through the locked room.

Read the text carefully, becasue thhose are the biggest clues of what you need!

This game uses directional commands ("n", "e", "s", "w") and others such as "show".

Specific commands can be used ("use", "play", "eat", etc) for story circumstances.

You may view all you items in your backpack, which can be accessed by typing "show" when available. You may type an item you own into the console and a description will appear for you, sometimes giving you hints. You must type "exit" to stop viewing your backpack and continue your escape in the room you were in.

There will be a turn-based combat system in this game, and it relies on the items in your inventory, so be careful!


P.S. If you are playing this game, a lot of text may appear on your screen at once, and even with the console window the the largest, you may have to scroll up to start reading from the top.

THIS IS EXTREMELY IMPORTANT IN THESE ROOMS: Library, Kitchen

This note is ESSENTIAL when you are in combat, as it may lead to confusion and an unpleasant experience.

It would be preferable if you did this every time for the best experience (example: Casino).

Thank you!

![MAP](/images.py/MAP.png)

Map:



                                     +------+
                                     | Cafe |
                                     +------+
                                         ^
                                         |
                       +----------+      |
                       | AndyRoom | ---->^
                       +----------+      |
                                         |
                                    HallwayNorth()
                                         |
                		                 |           +-----------+
                        	             ^ <-------- | PartyRoom |
                	                     |  	     +-----------+
                                         |
                 +----------+            ^            +----------+
                 |  Kitchen |            |		      | Dog Room |
                 +----------+            |            +----------+
                       |                 |                  |
                       |                 |                  |
+----------+           v            +----------+            v           +----------+
|  Library |<-----HallwayWest()-----|  Cellar  |-----HallwayEast()----->| Bathroom |
+----------+           ^            +----------+                        +----------+ 
	     	           |                 |
               	       |                 v
                 +-----------+      +-----------+
                 |  Casino   |      |LockedRoom |
        		 +-----------+      +-----------+
