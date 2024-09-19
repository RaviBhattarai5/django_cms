from django.shortcuts import redirect
from django.urls import reverse

class RedirectIfNotLoggedInMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        login_url = reverse('login')
        
        if request.path =='':
            return redirect('login')
        elif not request.user.is_authenticated and request.path != login_url:
            return redirect('login')
        elif request.user.is_authenticated and request.path == login_url:
            return redirect('dashboard')
        return self.get_response(request)
