import logging
from pyx import *

def output( project, filename ):
	log = logging.getLogger( __name__ )

	log.debug( filename )

	c = canvas.canvas()
	c.text(0, 0, "Hello, world!")
	c.stroke(path.line(0, 0, 2, 0))
	c.writeEPSfile( filename )
