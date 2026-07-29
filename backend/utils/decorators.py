from functools import wraps

from flask import jsonify

from flask_jwt_extended import get_jwt_identity

from models.user import User




def get_logged_in_user():

    user_id = get_jwt_identity()


    user = User.query.get(user_id)


    return user





def admin_required(fn):

    @wraps(fn)

    def wrapper(*args, **kwargs):


        user = get_logged_in_user()


        if not user:

            return jsonify({

                "message":"User not found"

            }),404




        if user.role != "ADMIN":


            return jsonify({

                "message":"Admin access required"

            }),403




        return fn(*args, **kwargs)



    return wrapper






def company_required(fn):


    @wraps(fn)

    def wrapper(*args, **kwargs):


        user=get_logged_in_user()



        if not user:

            return jsonify({

                "message":"User not found"

            }),404




        if user.role!="COMPANY":


            return jsonify({

                "message":"Company access required"

            }),403




        return fn(*args,**kwargs)



    return wrapper







def student_required(fn):


    @wraps(fn)

    def wrapper(*args, **kwargs):


        user=get_logged_in_user()



        if not user:

            return jsonify({

                "message":"User not found"

            }),404





        if user.role!="STUDENT":


            return jsonify({

                "message":"Student access required"

            }),403




        return fn(*args,**kwargs)



    return wrapper