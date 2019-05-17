from flask import Flask,request,jsonify
from flask_jwt_extended import JWTManager,create_access_token
import liangqing.liangqing201806404122.ddd.qing as qing
import liangqing.liangqing201806404122.fff.zhuce_denglu as liang

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

app.register_blueprint(qing.ming)
app.register_blueprint(liang.min)

if __name__ == "__main__":
    app.run()


