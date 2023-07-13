from flask import Flask, request, Response
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


@app.route('/<path:path>', methods=['GET', 'POST'])
def proxy(path):

    target_url = 'https://space.storemore.es:8082/Spacemanager' + request.path
    headers = {key: value for key, value in request.headers.items() if key not in ('Host', 'Content-Length')}
    headers['Access-Control-Allow-Origin'] = '*'

    if request.method == 'GET':
        resp = requests.get(target_url, params=request.args, headers=headers, verify=False)
    elif request.method == 'POST':
        resp = requests.post(target_url, data=request.form, files=request.files, headers=headers, verify=False)

    return Response(resp.content, resp.status_code)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
