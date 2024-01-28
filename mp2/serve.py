from flask import Flask, request, jsonify
import subprocess
import socket
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        arguments = ['python3', 'stress_cpu.py']
        stress_out = subprocess.Popen(arguments)
        return jsonify({"stress": str(stress_out)})

    if request.method == "GET":
        return socket.gethostname()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)