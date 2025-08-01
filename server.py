from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "Servidor activo"

@app.route("/lento")
def lento():
    time.sleep(2)
    return "Respuesta lenta"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, threaded=True)
