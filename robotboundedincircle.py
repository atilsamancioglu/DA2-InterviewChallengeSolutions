'''
On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:

The north direction is the positive direction of the y-axis.
The south direction is the negative direction of the y-axis.
The east direction is the positive direction of the x-axis.
The west direction is the negative direction of the x-axis.
The robot can receive one of three instructions:

"G": go straight 1 unit.
"L": turn 90 degrees to the left (i.e., anti-clockwise direction).
"R": turn 90 degrees to the right (i.e., clockwise direction).
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

'''

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directionX = 0
        directionY = 1
        positionX = 0
        positionY = 0
       
        for inst in instructions:
            if inst == "G":
                positionX = positionX + directionX
                positionY = positionY + directionY
            elif inst == "L":
                (directionX, directionY) = (- 1 * directionY, directionX)
            elif inst == "R":
                (directionX, directionY) = (directionY, -1 * directionX)
       
        return (positionX,positionY) == (0,0) or (directionX,directionY) != (0,1)
