from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import Fcuser

# Create your views here.
def register(request):
    if request.method == 'GET':
        res_data = {}
        # res_data['error'] = '비밀번호가 다릅니다!'

        return render(request, 'register.html', res_data)
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['re-password']

        res_data = {}
        if password != re_password:
            res_data['error'] = '비밀번호가 다릅니다!'

        fcuser = Fcuser(
            username=username,
            password=make_password(password),
        )

        fcuser.save()

        return render(request, 'register.html', res_data)
