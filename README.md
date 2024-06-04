# Locates Distribution

This is an interview task written by Niv Zelber, handed out to Dana/Nimrod from qSpark.  
The task at hand is joined to this repo for convince only.

## Logic

The same logic is performed for each symbol (without regards of other symbols).

The basic cases is simple - if enough locates are available, distribute all of them. If none are available, distribute none.  
If there aren't enough locates:

1. Start by assigning each client the proportional share of what they asked for from the available locates
2. Sort the list of client by one's closest to getting a full locate first
   1. i.e. 91 comes before 270 since $100-91=9<300-270=30$
   2. When it comes to round locates (an exact duplicate of 100) they will be at the bottom of the sorted list
3. Count the number of partial locates available
   1. $[91, 270, 100] \longrightarrow 91+70+0=161$
4. Round each of the clients assigning down to the nearest full locate
5. Loop on the clients by the sorted list order and give a full locate whenever possible
   1. One client might still receive a partial locate if the sum on stage 3 was not devisable by 100

This logic is better then a complete fair distribution since it prioritizes giving out full locates.  
It is very optimized to this demand since it starts by giving out a full extra locate to whichever client was closest to getting one in case of a fair distribution, meaning the number of full locates to be handed out will be maximal.  
It also adheres to all the requirements of the task:

1. No client gets more locates than requeued
2. All available locates are distributed

## Run Me

This task was written using python 3.12, but will probably run on older version as well.

To run all cases just run `python main.py`.
To run a specific case run `python main.py [case-index]` (`case-index` is 0 based).

Feel free to change:

- The constants in `constants.py`
- The cases in `dummy_data.py`