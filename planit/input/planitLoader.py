import logging
from planit.system.core import Project

def load( filename ):
	log = logging.getLogger( "input.planitLoader.load" )

	return Project( filename )
