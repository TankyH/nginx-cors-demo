from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Hello(Resource):
	def post(self):
		return {'result': 'Hello World!'}


api.add_resource(Hello, '/api')


if __name__ == '__main__':
	app.run(debug=True)
