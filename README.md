# Project Name: Moving Basketball Hoop
Computer vision extends to several actions like object trajectory prediction. By OpenCV library, the color finder with HSV values could highlight the targeted object, the ball, among the rest of the objects. 
    
This aided to assign the location of the ball's center point in (x,y) coordinates and was saved to be connected. Accordingly, the polynomial curve of its motion in the future was predicted, and this could be a turning point for creating a flying hoop. Moreover, this formed a path to knowing whether the ball will be shotted inside the traditional fixed hoop or not. 
## Weakness point
The weakness point is contouring any object with the same color as a ball, and this can cause errors within the fitting polynomial curve.  
## Mechanical design:
The aim is to implement an H-bot gantry design attached to a basketball hoop that moves in XY plan to catch the ball. I am responsible for the software part: ball trajectory prediction. In this stage, I am searching for the polynomial fitting equation in 2D and the motion of a curve in 3D.
## Problems:
The complex problem is that I had to approximate the single 2D images into the 3D position. This decision was because the design of H-bot gantry is moving in XY plan, and the ball is projected from the Z axis that makes an angle with X and Y axes.
 
## Procedures
    1. Ball detection with its center at a position vector (X,Y,Z)
    2. Plotting the motion of ball in a 3D graph with matplotlib 
    3. Searching for motion in a 3D curve to predict an equation for the polynomial curve of the ball motion 
 
 ### Step 1 was done as shown below 
 
 ![image](https://user-images.githubusercontent.com/101527083/220137668-d189df1a-9c34-484c-9f02-c2569629dc97.png) ![image](https://user-images.githubusercontent.com/101527083/220137756-1f8017ba-892c-4b9f-9431-38c7d6ad1265.png)

Step 2 and 3 are (in progress)
    
The current stage is for searching regarding the object trajectory prediction in 3D motion as it is one of the most important and complex topics in the computer vision field.

