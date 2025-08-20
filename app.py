from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['POST'])
def hello():
    data = request.get_json()
    
    if not data or 'name' not in data:
        return {"error": "Missing 'name' in request body"}, 400

    name = data['name']
    return {"message": f"Hello, {name}!"}, 200

if __name__ == '__main__':
    app.run(debug=True)
