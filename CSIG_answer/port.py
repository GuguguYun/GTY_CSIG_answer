from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/test', methods=['GET'])
def test_api():
    # 获取参数
    a = request.args.get('a', type=int)  # 选填参数
    b = request.args.get('b')  # 必填参数

    # 参数验证
    if b is None:
        return jsonify({
            "error_code": "1",
            "error_message": "Parameter 'b' is required",
            "reference": ""
        }), 400

    return jsonify({
        "error_code": "0",
        "error_message": "success",
        "reference": "111"
    })


if __name__ == '__main__':
    app.run(port=5000)