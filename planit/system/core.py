import logging

class Project:
	def __init__( self, name ):
		self.log = logging.getLogger( "Project" )
		self.name = name
		self.log.debug( "new Project '%s'" % self.name )

class Task:
	def __init__( self, name ):
		self.log = logging.getLogger( "Task" )
		self.name = name
		self.log.debug( "new Task '%s'" % self.name )

class Resource:
	def __init__( self, name ):
		self.log = logging.getLogger( "Resource" )
		self.name = name
		self.log.debug( "new Resource '%s'" % self.name )

class Timetable:
	def __init__( self, name ):
		self.log = logging.getLogger( "Timetable" )
		self.name = name
		self.log.debug( "new Timetable '%s'" % self.name )
