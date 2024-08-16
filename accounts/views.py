



from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.urls import reverse_lazy
from publicblog import settings
from .forms import RegistrationForm
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_str
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.core.mail import EmailMessage, send_mail,BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import get_user_model
from .tokens import account_activation_token
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import views as auth_views


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        # Decode the uid and retrieve the user
        uid = force_str(urlsafe_base64_decode(uidb64))
        print(f"Decoded UID: {uid}")
        user = User.objects.get(pk=uid)
        print(f"User retrieved: {user}")
    except (TypeError, ValueError, OverflowError, User.DoesNotExist) as e:
        user = None
        print(f"Error retrieving user: {e}")
    
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        print("User activated and saved")
        messages.success(request, f"Thank you {user.username} for your Email Confirmation. Now you can login with your Account")
        return redirect('account_app:login')
    else:
        messages.error(request, "Activation Link is Invalid!")
    
    return redirect('blogpost:post-home')


def activate_email(request,user,to_email):
    print(f'activate_email function triggering')
    current_site = get_current_site(request)
    mail_subject="Activate Your Account."
    message=render_to_string("accounts/activation_email.html",{
                'user':user.username,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
               'protocol': 'https' if request.is_secure() else 'http'
            })
    email=EmailMessage(mail_subject,message,to=[to_email])
    activation_link = "https://mail.google.com"
    if email.send():
        return (
            f"Dear <b class='activate-text'>{user.username}</b>, go to your email "
            f"<b class='activate-text'>{to_email}</b> inbox and click the received "
            f"<a href='{activation_link}' target='_blank'  style='text-decoration: underline;' class='activate-text'>activation link</a>"
        )
    else:
        return f'problem sending the email to {to_email} check if you entered valid email'





def activate_message(username, to_email):
    activation_link = "https://mail.google.com"
    return (
        f"Dear <b class='activate-text'>{username}</b>, go to your email "
        f"<b class='activate-text'>{to_email}</b> inbox and click the received "
        f"<a href='{activation_link}' target='_blank'  style='text-decoration: underline;' class='activate-text'>activation link</a>"
    )


def register_view(request):
    loginpage_url=reverse("account_app:login")
    if request.user.is_authenticated:
        return redirect('blogpost:post-home')
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_active=False
            user.save()
            # message=activate_message(form.cleaned_data.get('username'),form.cleaned_data.get('email'))
            message=activate_email(request,user,form.cleaned_data.get('email'))
            print(f" username:{user.username} , password {user.password} email {user.email}")
            response={'success': True,'message': message, 'redirect_url':loginpage_url}
            return JsonResponse(response)
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
    




def password_reset_request(request):
    if request.method=='POST':
        print("request it post method")
        password_reset_form=PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            print("password rest form is valid")
            get_email=password_reset_form.cleaned_data['email']
            print(f"got meail from reset form {get_email}")
            User=get_user_model()
            current_site = get_current_site(request)
            user_email=User.objects.filter(Q(email=get_email))
            if user_email.exists():
                print(f"yes user email exists {user_email}")
                for user in user_email:
                    subject="Password Reset"
                    email_template_name='accounts/password_message.txt'
                    parameters={
                    'email':user_email,
                    'domain':current_site.domain,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':default_token_generator.make_token(user),
                     'protocol': 'https' if request.is_secure() else 'http'
                    }
                    
                    email=render_to_string(email_template_name,parameters)
                    try:
                        send_mail(subject,email,settings.EMAIL_HOST_USER,[user.email],fail_silently=False)
                        print("Email sent to the user")
                    except Exception as e:
                        print(f"Error sending email: {e}")
                        return HttpResponse('Error sending email')
                    return redirect('account_app:password_reset_done')
    else:
        password_reset_form=PasswordResetForm()
    context={
        'password_reset_form':password_reset_form
    }
    return render(request,'accounts/password_reset.html',context)




def password_reset_confirm(request, uidb64, token):
    User = get_user_model()
    uid = force_bytes(urlsafe_base64_decode(uidb64))
    user = get_object_or_404(User, pk=uid)

    if default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                return redirect(reverse_lazy('account_app:password_reset_complete'))
        else:
            form = SetPasswordForm(user)
        
        return render(request, 'accounts/password_reset_form.html', {'form': form})
    
    else:
        return HttpResponse('Invalid password reset link', status=400)








