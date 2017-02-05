Artificial Intelligence, WPI 2016 Spring.

Some python codes for homework and proj, including robot localization (HMM) and Recurrent Reinforcement Learning (or ANN) in financial trading. Codes must run in 64bit python3.

Another issue is that there are many typos in the report. Too lazy to update, since I've lost the original Tex file. The math part should be good in the program, though I found typos in the derivation in the report. Please refer to the original papers.

HM Problem: Aritficial Intelligence A Modern Approach pp.607, ex 15.9
This exercise is concerned with filtering in an environment with no landmarks. Consider a vacuum robot in an empty room, represented by n x m rectangular grid. The robot’s location is hidden; the only evidence available to the observer is a noisy location sensor that gives an approximation to the robot’s location. If the robot is at location (x, y) then with probability 0.1 the sensor gives the correct location, with probability 0.05 each it reports one of the 8 locations immediately
surrounding (x, y), with probability 0.025 each it reports one of the 16 locations that surround those 8, and with the remaining probability of 0.1 it reports “no reading”. The robot’s policy is to pick a direction and follow it with probability
0.8 on each step; the robot switches to a randomly selected new heading with probability 0.2 (or with probability 1 if it encounters a wall). Assume only horizontal or vertical moves. Implement this as an HMM and do filtering to
track the robot. How accurately can we track the robot’s path?


