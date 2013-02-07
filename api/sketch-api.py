#############################################
#
# API to save and load sketches from database
#
#############################################

from flask import Flask, request, make_response, jsonify
from flask.ext import restful
from flask.ext.restful import reqparse
from mongokit import ObjectId

from sketchdb import connection
from sketch import Sketch

import datetime
import json

app = Flask(__name__)
api = restful.Api(app)

# setup args
parser = reqparse.RequestParser()
parser.add_argument('oid', type=unicode)
parser.add_argument('sketchText', type=unicode)

# TODO: decorator? check jsonp decorator
def make_jsonp(o):
    if 'callbackFunc' in request.args:
        cb = request.args['callbackFunc']
        resp = cb + '(' + json.dumps(o) + ');'
        response = make_response(resp)
        response.headers['Content-Type'] = 'text/javascript'
        return response

class SketchApi(restful.Resource):

    # put sketch to db
    # this is unused now that put is unsupported
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

        #return jsonify(success=True, _id=str(sketch._id))
        return make_jsonp(success=True, _id=str(sketch._id))

    # load sketch from db
    def get(self):

        args = parser.parse_args()

        # get the rates collection
        sketch = connection.Sketch.find_one({
                '_id': ObjectId(args.oid)
        })

        # can't return document?
        #return jsonify(
        #    success=True, 
        #    sketchText=sketch['sketchText']
        #)
        return make_jsonp({'success': True, 'sketchText': str(sketch.sketchText)})

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

class SaveSketch(restful.Resource):

    # put sketch to db
    def get(self):

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

        #return jsonify(success=True, _id=str(sketch._id))
        return make_jsonp({
            'success': True, 
            '_id': str(sketch._id)
        })

api.add_resource(SketchApi, '/sketch')
api.add_resource(SaveSketch, '/sketch/save')

if __name__ == '__main__':
    app.run(debug=True)
