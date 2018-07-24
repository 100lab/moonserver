from flask import Flask, json, request, Response

app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'


#curl -H "Content-type: application/json" -X GET http://127.0.0.1:5000/api/get_tops
#curl -H "Content-type: application/json" -X GET -i http://127.0.0.1:5000/api/get_tops
@app.route('/api/get_tops', methods=['GET'])
def api_get_tops():
    if request.method != 'GET':
        return ""
    
    if request.headers['Content-Type'] != 'application/json':
        return ""

    data = {
        'jmt' : 800000,
        'jjang' : 3001
    }
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://www.mooncle.com'

    return resp

if __name__ == '__main__':
    app.run()
