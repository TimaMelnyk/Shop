import urllib.request
from polls.models import User
import json
import re


class UserInfo:
    def __init__(self, userId, isAdmin):
        self.userId = userId
        self.isAdmin = isAdmin


def check_register_input_fields(lastName, firstName, login, password, phoneNumber):
    if not re.match('[A-Z][a-z]{2,30}', lastName):
        return False
    if not re.match('[A-Z][a-z]{2,30}', firstName):
        return False
    if not re.match('\w{4,20}', login):
        return False
    if not re.match('\w{4,20}', password):
        return False
    if not re.match('\d{6,15}', phoneNumber):
        return False
    return True


def get_user_authenticated(request):
    try:
        request.session['user_id']
        request.session['is_admin']
        userInfo = UserInfo(request.session['user_id'], request.session['is_admin'])
        return userInfo
    except KeyError:
        return None


def vk_user_authentication(request):
    code = request.GET['code']
    response = urllib.request.urlopen("https://oauth.vk.com/access_token?client_id=5148730&"
                                      "client_secret=9av2abz5ucZ6fy7XHvRx&"
                                      "redirect_uri=http://127.0.0.1:8000/auth&code=" + code)
    responseData = json.loads(response.read().decode('utf-8'))
    user_id = responseData['user_id']
    respon=urllib.request.urlopen("https://api.vk.com/method/users.get?user_id="+str(user_id)+"&v=5.40"
                                  "&access_token="+str(responseData['access_token']))
    responseData = json.loads(respon.read().decode('utf-8'))
    UserData = responseData['response'][0]
    users = User.objects.filter(vkId=UserData['id'])
    if len(users) == 0:
        UserData['created'] = False
    else:
        UserData['user_id'] = users[0].id
        UserData['created'] = True
    return UserData


def create_user(lastName, firstName, login=None, password=None, phoneNumber=None, vkId=None, permissions=None):
    user = User(lastName=lastName, firstName=firstName)
    if login:
        users = User.objects.filter(login=login)
        if len(users)>0:
            raise Exception
        user.login = login
    if password:
        user.password = password
    if phoneNumber:
        user.phoneNumber = phoneNumber
    if vkId:
        user.vkId = vkId
    if permissions:
        user.permissions = permissions
    user.save()
    return user