import logging

class Project:
	tasks = []
	resources = []
	timetables = []

	def __init__( self, name ):
		self.log = logging.getLogger( "Project" )
		self.name = name
		self.log.debug( "new Project '%s'" % self.name )
	
	def addTask( self, task ):
		self.tasks.append( task )
	
	def addTasks( self, tasks ):
		for task in tasks[:]:
			self.addTask( task )
	
	def addResource( self, resource ):
		self.resources.append( resource )
	
	def addResources( self, resources ):
		for resource in resources[:]:
			self.addResource( resource )

	def addTimetable( self, timetable ):
		self.timetables.append( timetable )
	
	def addTimetables( self, timetables ):
		for timetable in timetables[:]:
			self.addTimetable( timetable )

class Task:
	childTasks = []

	def __init__( self, id, name ):
		self.log = logging.getLogger( "Task" )
		self.id = id
		self.name = name
		self.log.debug( "new Task '%s' (%s)" % (self.name, self.id) )

	def addTask( self, task ):
		self.childTasks.append( task )
	
	def addTasks( self, tasks ):
		for task in tasks[:]:
			self.addTask( task )
	
class Resource:
	childResources = []

	def __init__( self, id, name ):
		self.log = logging.getLogger( "Resource" )
		self.id = id
		self.name = name
		self.log.debug( "new Resource '%s' (%s)" % (self.name, self.id) )
	
	def addResource( self, resource ):
		self.childResources.append( resource )
	
	def addResources( self, resources ):
		for resource in resources[:]:
			self.addResource( resource )

class Timetable:
	childTimetables = []

	def __init__( self, id, name ):
		self.log = logging.getLogger( "Timetable" )
		self.id = id
		self.name = name
		self.log.debug( "new Timetable '%s' (%s)" % (self.name, self.id) )

	def addTimetable( self, timetable ):
		self.childTimetables.append( timetable )
	
	def addTimetables( self, timetables ):
		for timetable in timetables[:]:
			self.addTimetable( timetable )
