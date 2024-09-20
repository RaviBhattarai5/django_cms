from django.shortcuts import redirect
from django.urls import reverse

class RedirectIfNotLoggedInMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        login_url = reverse('login')
        register_url = reverse('register') 
        # role_url = reverse('role') 
        
        # Redirect unauthenticated users trying to access any page except login or register
        if request.path =='':
            return redirect('login')
        elif not request.user.is_authenticated:
            if request.path not in [login_url, register_url]:
                return redirect('login')
        
        # Redirect authenticated users from login page to dashboard
        elif request.user.is_authenticated:
            if request.path == login_url:
                return redirect('dashboard')

        return self.get_response(request)
