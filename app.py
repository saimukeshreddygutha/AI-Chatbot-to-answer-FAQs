from flask import Flask, render_template, request, jsonify

from bot import response

app = Flask(__name__)

@app.get('/')
def index_get():
    return render_template(base.html)
@app.post("/predict")
def predict():
    t = request.get_json().get("message")
    response = response("t")
    message = {'answer': response}
    return jsonify(message)


if __name__ == 'main':
    app.run(debug=True)
    