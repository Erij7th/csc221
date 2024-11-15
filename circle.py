from gasp import *

begin_graphics()

Circle((300, 200), 100)

update_when('key_pressed')  # again, this keeps the graphics window open...
end_graphics()
