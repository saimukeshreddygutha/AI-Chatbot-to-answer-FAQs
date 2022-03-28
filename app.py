from flask import Flask, render_template, request, jsonify

from chat import response

app = Flask(__name__)

@app.get('/')
def index_get():
    return render_template("base.html")
@app.post("/predict")
def predict():
    t = request.get_json().get("message")
    responset = response(t)
    message = {'answer': responset}
    return jsonify(message)


if __name__ == 'main':
    app.run(debug=True)
    