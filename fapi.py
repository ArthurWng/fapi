from flask import Flask, request



app = Flask('fapi')  # 实例化，定义一个Flask实例

@app.route('/get_request_info', methods=['post','get'])
def get_request_info():
    request_info = dict()

    request_info['headers'] = dict(request.headers)
    request_info['params_form'] = dict(request.form)
    request_info['params_data'] = dict(request.data)
    request_info['params_query'] = dict(request.args)

    return request_info

if __name__ == '__main__':
    app.run(port=4500, debug=True, host='0.0.0.0')