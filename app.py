from flask import Flask, request, jsonify
from torch import FloatTensor
from load import model

app = Flask(__name__)

'''
Web => AI 보내는거
Request:
    body:
    
    1)include
     사용자가 선택한 좋아하는 음식의 index 값의 리스트
     ex) [1,3,5,7,9,]  // 12개
     
    2)exclude
     사용자가 선택한 싫어하는 음식의 이름 리스트
     ex)["가지", "생선"]

AI=> Web으로 보내줘야하는거
Response:
    body:
        food: []
        //추천 음식 리스트 (6개)
'''

@app.route('/', methods=['POST'])
def AiModel():
    include= request.json['include']
    exclude=request.json['exclude']

    print(include)
    print(exclude)


    data =include

    return jsonify(data)

if __name__ == "__main__":
    app.run(port=5000)