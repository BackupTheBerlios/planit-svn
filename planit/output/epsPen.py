import logging
from pyx import *

def output( project, filename ):
	log = logging.getLogger( __name__ )

	log.debug( filename )

	c = canvas.canvas()
	c.text(0, 0, "Hello, world!")
	c.stroke(path.line(0, 0, 2, 0))
	#cross = path.path(path.moveto(0, 0), path.rlineto(1, 1),
        #          path.moveto(1, 0), path.rlineto(-1, 1))
	#c.stroke( cross )
	#rect2 = path.path(path.moveto(0, 0), path.lineto(0, 1), 
        #          path.lineto(1, 1), path.lineto(1, 0), path.lineto(0, 0))
	#c.stroke(rect2, [deco.filled([color.grey(0.95)])])
	c.writeEPSfile( filename )
