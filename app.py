from flask import Flask, jsonify, request, send_from_directory
import os

app = Flask(__name__)

@app.route('/list', methods=['GET'])
def list_templates():
    id = request.args.get('id')
    data = None
    templates = []
    for filename in os.listdir('tpls'):
        if filename.endswith('.md'):
            templates.append(filename)
            if id == filename:
                with open(os.path.join('tpls', filename), 'r') as f:
                    data = f.read()
    return jsonify({'list': templates, 'data': data})

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/scripts/<path:path>')
def send_script(path):
    return send_from_directory('scripts', path)

@app.route('/tpls/<path:path>')
def send_template(path):
    return send_from_directory('tpls', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
