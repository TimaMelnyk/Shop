from django.shortcuts import render_to_response
from polls.models import *
from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string
from django.core.context_processors import csrf

from datetime import *
import random
import string
from django.shortcuts import render_to_response
from django.core.mail import send_mail ,BadHeaderError
from django.template import RequestContext, loader
from django.core.context_processors import csrf
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
import re
from polls.models import User
from django.shortcuts import render, redirect
# Create your views here.

def home(request):
    category = Category.objects.all()
    context = {
        'sitename': 'InternetShop',
        'categories': category,
    }
    return HttpResponse(render_to_string('home.html',context))

def register(request):
    return render_to_response('register.html')

# def register(request):
#     error = "NOT VALID"
#     if request.method == 'POST':
#         login = request.POST['login']
#         password = request.POST['password']
#         password2 = request.POST['password2']
#         phoneNumber = request.POST['phone']
#         valid = check_register_input_fields(login, password, password2, phoneNumber)
#         if not valid:
#             raise Http404('NOT VALID')
#         new_user = create_user(login=login,password=password,phoneNumber=phoneNumber)
#         request.session['user_id'] = new_user.id
#     return render_to_response('register.html')
#     

def auth(request):
    c = {}
    try:
        if request.method == 'GET':
            try:
                request.GET['exit']
                del request.session['user_id']
                del request.session['is_admin']
            except KeyError:
                pass
            UserData = vk_user_authentication(request)
            if not UserData['created']:
                user_id = create_user(firstName=UserData['first_name'], lastName=UserData['last_name'],
                                     vkId=UserData['id']).id
            else:
                user_id = UserData['user_id']
            request.session['user_id'] = user_id
        if request.method == 'POST':
            lastName = request.POST['lastName']
            firstName = request.POST['firstName']
            print(lastName,firstName)
            login = request.POST['login']
            password = request.POST['password']
            phoneNumber = request.POST['phoneNumber']
            c.update({'lastName': lastName,'firstName': firstName,'login': login,'password': password,'phoneNumber': phoneNumber})
            valid = check_register_input_fields(lastName, firstName, login, password, phoneNumber)
            if not valid:
                raise Exception
            new_user = create_user(firstName=firstName, lastName=lastName, login=login,
                                        password=password,phoneNumber=phoneNumber)
            request.session['user_id'] = new_user.id
        request.session['is_admin'] = False
        return redirect('/',c)
    except:
        return redirect('/register/',c)
# 
# def check_register_input_fields(login, password, password2,  phoneNumber):
#     if not re.match('\w{4,20}', login):
#         return False
#     if not re.match('\w{4,20}', password):
#         return False
#     if  not password==password2:
#         return False
#     if not re.match('\d{6,15}', phoneNumber):
#         return False
#     return True
# 
# def create_user(login=None, password=None, phoneNumber=None):
#     client = User()
#     print(login)
#     if login:
#         clients = User.objects.filter(login=login)
#         if len(clients)>0:
#             raise Exception
#         client.login = login
#     if password:
#         client.password = password
#     if phoneNumber:
#         client.phoneNumber = phoneNumber
#     client.save()
#     return client

# def login(request):
#     args = {}
#     args.update(csrf(request))
#     print "test"
#     if request.POST:
#         username = request.POST.get('username','')
#         password = request.POST.get('password','')
#         user = auth.authenticate(username=username, password=password)
#         if user is not None:
#             auth.login(request ,user)
#             return redirect('/')
#         else:
#             args['login_error'] = 'user did not register'
#             return render_to_response('/',args)
#         
#     else:
#         return render_to_response('/',args)
#     
# def logout(request):
#     auth.logout(request)
#     return redirect("/")

def order(request):
    c = {}
    category = Category.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        c.update(csrf(request))
        if form.is_valid():
            cd = form.cleaned_data
            subject = request.POST['subject']
            send_mail('MAIL', subject, settings.EMAIL_HOST_USER, ['timofeimelnyk@gamil.com'])
            return HttpResponseRedirect('/order/thanks/')
    else:
        form = ContactForm()
    c = RequestContext(request, {'form': form,'categories': category})
    return render_to_response('korzina.html', c)

def item(request,alias):
    try:
        category = Category.objects.all()
        tovar = Item.objects.get(alias=alias)
    except:
        raise Http404('CANT FOUND OBJ')
    context = {        
        'tovar': tovar,
        'categories': category,
    }
    return HttpResponse(render_to_string('item.html',context))

def get_category(request,alias):
    try:
        category = Category.objects.get(alias=alias)
        cat = Category.objects.all()
        tovars = Item.objects.filter(category=category)
    except:
        raise Http404('CANT FOUND OBJ')
    context = {        
        'tovars': tovars,
        'category': category,
        'categories':cat,
    }
    return HttpResponse(render_to_string('index.html',context))

def search_in_form(request):
    return render_to_response('searching.html')
    
def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET["q"]
        if not q:
            errors.append('The field is empty')
        elif len(q) > 20:
            errors.append('You should write less than 20 symbols')
        else:
            items = Item.objects.filter(name__icontains=q)
            category = Category.objects.all()
            context = {        
            'query': q,
            'items': items,
            'categories': category,
            }
            return render_to_response('searching.html',context)
    return render_to_response('searching.html', {'errors': errors})



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