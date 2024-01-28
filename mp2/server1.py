from flask import Flask, request, jsonify
app = Flask(__name__)

num = 0

@app.route('/', methods=["GET", "POST"])
def serve():
    global num
    if request.method == "POST":
        data = request.get_json()
        update = data.get('num')
        if update is not None:
            num = update
            return jsonify({'message': 'Update successful'}), 200
        else:
            return jsonify({'error': 'Invalid'}), 400

    if request.method == "GET":
        return str(num), 200    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)