import subprocess

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Tidak boleh bagi nol")
    return a / b

def run_command(cmd):
    # Penggunaan shell=True berisiko tinggi terhadap Command Injection
    result = subprocess.run(
        cmd, shell=True, capture_output=True, text=True
    )
    return result.stdout