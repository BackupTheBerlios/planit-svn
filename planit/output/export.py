import logging
from planit.output import epsPen

class Export:
	def __init__( self, project, pen ):
		self.project = project
		self.pen  = pen
	
	def output( self, filename ):
		self.pen.output( self.project, filename )
	

def write( project, filename, format ):
	log = logging.getLogger( __name__ )

	log.debug( "filename: %s" % filename )
	log.debug( "format: %s" % format )

	{
		'eps': Export( project, epsPen ).output( filename )
	}[ format ]
