# screencast_server.py
from flask import Flask, Response, render_template_string
from mss import mss
from PIL import Image
import io, time

# ---- TUNE THESE ----
FPS = 10            # higher = smoother, more CPU/network
SCALE = 0.7         # 1.0 = full size; use 0.5~0.8 for 10 viewers
JPEG_QUALITY = 70   # 40–80 is a good range
MONITOR_INDEX = 1   # 1 = primary; change if you have multiple monitors
# --------------------

app = Flask(__name__)

HTML = """
<!doctype html>
<title>Python Screen Share</title>
<style> body{margin:0;background:#111;display:grid;place-items:center;height:100vh} img{max-width:100vw;max-height:100vh} </style>
<img src="/stream.mjpg" alt="Screen stream">
"""

def mjpeg_generator():
    with mss() as sct:
        mon = sct.monitors[MONITOR_INDEX]
        frame_interval = 1.0 / max(FPS, 1)
        while True:
            start = time.time()
            shot = sct.grab(mon)                 # raw screen
            img = Image.frombytes("RGB", shot.size, shot.rgb)

            if SCALE != 1.0:
                w = int(img.width * SCALE)
                h = int(img.height * SCALE)
                img = img.resize((w, h), Image.BILINEAR)

            buf = io.BytesIO()
            img.save(buf, format="JPEG", quality=JPEG_QUALITY, optimize=True)
            jpg = buf.getvalue()

            yield (b"--frame\r\n"
                   b"Content-Type: image/jpeg\r\n"
                   b"Cache-Control: no-cache\r\n\r\n" + jpg + b"\r\n")

            # simple FPS limiter
            dt = time.time() - start
            if dt < frame_interval:
                time.sleep(frame_interval - dt)

@app.route("/")
def index():
    return render_template_string(HTML)

@app.route("/stream.mjpg")
def stream():
    return Response(mjpeg_generator(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
    # 0.0.0.0 makes it reachable from other laptops on your network
    app.run(host="0.0.0.0", port=5000, threaded=True)
