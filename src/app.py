from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return "DevSecOps Practice App is Running!"

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Tidak boleh bagi nol")
    return a / b

def run_command(cmd_list):
    result = subprocess.run(cmd_list, shell=False, capture_output=True, text=True)
    return result.stdout

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)