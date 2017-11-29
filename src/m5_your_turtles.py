"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Stephen Acomb.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
yertle = rg.SimpleTurtle('turtle')
yertle.pen = rg.Pen('blue', 3)
yertle.speed = 1
yertle.pen_down()
for k in range(9):
    yertle.forward(k*10)
    yertle.right(k*10)

mertle = rg.SimpleTurtle('turtle')
mertle.pen = rg.Pen('red', 3)
mertle.speed = 1
mertle.pen_down()
for k in range(9):
    mertle.forward((10-k)*10)
    mertle.left((10-k)*10)

print("Presenting the low-poly snowman!")

window.close_on_mouse_click()
