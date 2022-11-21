from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.shortcuts import render, redirect
from common.forms import UserForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from . forms import editInfoForm
from django.http import HttpResponse

#PasswordChangeForm2 불러옴 (5.27) -> 근데 안쓸듯?
from . forms import editInfoForm, PasswordChangeForm2



def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('/share/')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


def editinfo(request):
    if request.method == 'POST':
        form = editInfoForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/common/changed')
    else:
        form = editInfoForm(instance=request.user)
        context = {'form': form}
        return render(request, 'common/editinfo.html', context)

#PasswordChangeView.as_view 쓰니까 안써도 되는 듯?
""" def editpw(request):
    if request.method == 'POST':
        pwform = PasswordChangeForm(data=request.POST, user=request.user)
        if pwform.is_valid():
            pwform.save()
            return redirect('/share')
    else:
        pwform = PasswordChangeForm(user=request.user)
        context = {'form': pwform}
        return render(request, 'common/editpw.html', context) """

# editpw2 (5.28) -> PasswordChangeView.as_view 쓰니까 안써도 되는 듯?
""" def editpw2(request):
    if request.method == 'POST':
        pwform2 = PasswordChangeForm2(request.user, request.POST)
        if pwform2.is_valid():
            user = pwform2.save()
            #update_session_auth_hash(request, user)
            #messages.success(request, "Password has been hanged.")
            return redirect('/share')
    else:
        pwform2 = PasswordChangeForm2(request.user)
    return render(request, 'common/editpw.html', {'pwform2': pwform2}) """

#회원정보나 비밀번호 수정하고 나면 가게 되는 주소
def changed(request):
    return render(request, 'common/changed.html')

