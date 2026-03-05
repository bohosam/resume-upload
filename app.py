import subprocess
import os
import signal
import atexit
import time
from flask import Flask, render_template

app = Flask(__name__)

# Config
TUS_PORT = 1080
TUS_DATA_DIR = './data'
TUSD_BINARY = os.path.join(os.path.dirname(__file__), 'bin', 'tusd')

# Ensure data directory exists
if not os.path.exists(TUS_DATA_DIR):
    os.makedirs(TUS_DATA_DIR)

# Start tusd as a subprocess
print(f"Starting tusd on port {TUS_PORT}...")
tusd_process = subprocess.Popen(
    [
        TUSD_BINARY,
        '-upload-dir',
        TUS_DATA_DIR,
        '-port',
        str(TUS_PORT)
    ],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)


# Ensure tusd stops when Flask stops
def stop_tusd():
    print("Stopping tusd...")
    tusd_process.send_signal(signal.SIGTERM)
    tusd_process.wait()


atexit.register(stop_tusd)


@app.route('/')
def index():
    return render_template(
        'index.html',
        tus_endpoint=f"http://localhost:{TUS_PORT}/files/"
    )


if __name__ == '__main__':
    # Give tusd a moment to start
    time.sleep(1)
    app.run(port=5000, debug=False)
