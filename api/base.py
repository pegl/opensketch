from mongokit import Document, Connection
from sketchdb import connection
import datetime

class BaseDocument(Document):
    structure = {
      'created': datetime.datetime,
      'modified': datetime.datetime,
    }

    default_values = {
      'created': datetime.datetime.now,
      'modified': datetime.datetime.now
    }
    use_autorefs = True
    use_dot_notation = True
