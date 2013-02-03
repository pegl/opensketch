#############################################
#
# API to save and load sketches from database
#
#############################################

from flask import Flask, jsonify
from flask.ext import restful
from flask.ext.restful import reqparse
from mongokit import ObjectId

from sketchdb import connection
from sketch import Sketch

import datetime

app = Flask(__name__)
api = restful.Api(app)

# setup args
parser = reqparse.RequestParser()
parser.add_argument('oid', type=unicode)
parser.add_argument('sketchText', type=unicode)

class SketchApi(restful.Resource):

    # put sketch to db
    def put(self):

        args = parser.parse_args()
        try:
            sketch = connection.Sketch()
            # TODO: if args.oid is an objectid
            if len(args.oid) > 0:
                sketch = connection.Sketch.find_one({'_id': ObjectId(args.oid)})
        except Exception, e:
            # sketch doesn't exist
            pass

        try:
            sketch['sketchText'] = args.sketchText
            sketch['modified'] = datetime.datetime.now()
            sketch.save()
        except Exception, e:
            return jsonify(success=False, message="Could not save sketch")

        return jsonify(success=True, _id=str(sketch._id))

    # load sketch from db
    def get(self):

        args = parser.parse_args()

        # get the rates collection
        sketch = list(
            connection.Sketch.find({
                '_id': ObjectId(args.oid)
            }).limit(1)
        )

        # can't return document?
        return jsonify(
            success=True, 
            sketchText=sketch[0]['sketchText']
        )

    # delete sketch from db
    def delete(self):
        args = parser.parse_args()

        # get the rates collection
        try:
            connection.Sketch.find_one({
                '_id': ObjectId(args.sketchId)
            }).delete()
        except Exception, e:
            return jsonify(success=False, oid=args.oid)
        return jsonify(success=True, oid=args.oid)

api.add_resource(SketchApi, '/sketch')

if __name__ == '__main__':
    app.run(debug=True)
