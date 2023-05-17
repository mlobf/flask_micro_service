from flask import session, request
from . import USER_API_URL


class UserClient:
    @staticmethod
    def login(form):
        api_key = None
        payload ={
            'username':form.username.data,
            'password':form.password.data,
        }

        url = USER_API_URL +'/api/user/login'

        response = request.post(url,data=payload)

        if response:
            api_key = response.json().get('api_key')

        return api_key

    @staticmethod
    def get_user():
        headers = {
            "Authorization":session['user_api_key']
        }
        url = USER_API_URL + '/api/user'

        response =  request.get(url,headers=headers)

        return response.json()
    

    @staticmethod
    def create_user():
        user = None
        payload ={
            'username':form.username.data,
            'password':form.password.data,
        }

        url = USER_API_URL +'/api/user/create'
        response = request.post(url=url,data=payload)

        if response:
            user = response.json()

        return user
    @staticmethod
    def user_exists(username):
        url = USER_API_URL +'/api/user/'+ username +'/exist'

        return None



