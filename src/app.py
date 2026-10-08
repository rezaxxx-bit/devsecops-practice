from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return "DevSecOps Practice App is Running!"

@app.route("/ping")
def ping():
    ip = request.args.get("ip", "127.0.0.1")
    # Pengujian simulasi DAST
    return f"Pinging {ip}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)