from django.shortcuts import render

def get_home(request):
    return render(request, "TrangChu.html")

def login_view(request):
    return render(request, "login.html")

def register_view(request):
    return render(request, "register.html")
def history_view(request):
    return render(request, "history.html")