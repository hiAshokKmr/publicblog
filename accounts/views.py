


from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse
from .forms import RegistrationForm
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.sessions.models import Session



def register_view(request):
    loginpage_url=reverse("account_app:login")
    if request.user.is_authenticated:
        return redirect('blogpost:post-home')
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True,'message': 'Registration successful!', 'redirect_url':loginpage_url})
        else:
            print(form.errors)
            return JsonResponse({'success': False, 'errors': form.errors},status=400)
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})








from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.http import JsonResponse

def login_view(request):
    homepage_url=reverse("blogpost:post-home")
    if request.user.is_authenticated:
        return redirect('blogpost:post-home')  # Redirect to the home page

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not email or not password:
            return JsonResponse({'success': False, 'error': 'Email and Password cannot be empty.'})
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            response = JsonResponse({
                'success': True, 
                'message': f'Login successful! {user.email}', 
                'redirect_url': homepage_url,
              
            })
            # Prevent back navigation to the login page
            response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
            response['Pragma'] = 'no-cache'
            return response
        else:
            return JsonResponse({'success': False, 'error': "Account doesn't exist or incorrect Email or Password"})
    
    response = render(request, 'accounts/login.html')
    # response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    # response['Pragma'] = 'no-cache'
    return response





def logout_view(request):
    loginpage_url = reverse('account_app:login')
    if request.method == 'POST':
        Session.objects.filter(session_key=request.session.session_key).delete()
        logout(request)
        response= JsonResponse({
            'success': True,
            'message': 'Logout successful!',
            'redirect_url': loginpage_url, 
        })
        response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response['Pragma'] = 'no-cache'
        return response
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method. Use POST to log out.'})



from django.http import JsonResponse
from django.views import View

class CheckAuthView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({'is_authenticated': request.user.is_authenticated})