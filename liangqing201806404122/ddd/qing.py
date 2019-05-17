from flask import Blueprint
ming = Blueprint('ming',__name__)
@ming.route('/ok',methods= ['POST'])
def ok():
    return "I have a dream!"
