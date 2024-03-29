

from flask import Flask, request  # 导入Flask类库和request类库

app = Flask('fapi')  # 实例化，定义一个Flask实例
@app.route('/get_request_info', methods=['post', 'get'])
def get_request_info():
    request_info = dict()
    request_info['headers'] = dict(request.headers)
    request_info['params_form'] = dict(request.form)
    request_info['params_data'] = dict(request.data)
    request_info['params_query'] = dict(request.args)

    return request_info


if __name__ == '__main__':
    app.run(port=4500, debug=True, host='0.0.0.0')  # host='0.0.0.0' 表示内网和外网都可以访问本Flask服务
