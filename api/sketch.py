from mongokit import Document, Connection
from base import BaseDocument
from sketchdb import connection

class Sketch(BaseDocument):

	collection = 'sketch'

	__collection__ = 'sketch'
	__database__ = 'opensketch'

	structure = {
		'sketchText': unicode
	}

	required_fields = [
		'sketchText'
	]

	use_dot_notation = True
	#def __repr__(self):
	#	return '<Sketch %r>' % (self.timestamp)


connection.register([Sketch])
