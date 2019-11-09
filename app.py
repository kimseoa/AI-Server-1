from flask import Flask, request, jsonify
from torch import FloatTensor
from load import model

app = Flask(__name__)

'''
Request:
    body:
        foods: number[]

Response:
    body:
        recommendation: number[]

'''
@app.route('/', methods=['POST'])
def AiModel():
    body = request.get_json(force=True)
    output = model(FloatTensor(body['foods'])).detach().numpy()
    # result를 가공하는 작업
    result = [1, 2, 3, 4]
    return jsonify({ 'recommendation': result })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
