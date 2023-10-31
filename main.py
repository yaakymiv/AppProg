from flask import Flask, jsonify

app = Flask(__name__)

variant_number = 26 

@app.route('/api/v1/hello-world-{}'.format(variant_number))
def hello_world():
    response_data = {'message': 'Hello World {}'.format(variant_number)}
    return jsonify(response_data), 200

if __name__ == '__main__':
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000)
