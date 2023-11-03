from django.shortcuts import render
from django.views import View
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import login, logout
# from .forms import RegistrationForm
from django.http import HttpResponse, JsonResponse
from django.views.generic.edit import FormView
from django.contrib.auth.forms import (AuthenticationForm,PasswordChangeForm,PasswordResetForm,SetPasswordForm)
from django.contrib.auth import (REDIRECT_FIELD_NAME,get_user_model,login as auth_login, logout as auth_logout, update_session_auth_hash)
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import never_cache
from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import resolve_url
from django.conf import settings

# Create your views here.


class Login(View):
    def get(self, request):
        return render(request=request, template_name="user/login-index.html")

    def post(self, request):

        try:
            email = request.POST['username']
        except Exception as e:
            print(e)
            email = None
        try:
            password = request.POST['password']
        except Exception as e:
            password = None
        return HttpResponse(f" Email: {email} - Password: {password}")

        #
        response = {'status': False, 'message': ''}
        if email == "" or password == "":
            response['message'] = 'Username or password is not empty'
            return JsonResponse(response)
        print(request)
        user_login = ().authenticate(request=request, username=email, password=password)
        print(user_login)
        if user_login is None:
            response['message'] = 'Username or password is not invalid'
            return JsonResponse(response)

        login(request=request, user=user_login)
        request.session.set_expiry(10000)
        response['status'] = True
        response['message'] = 'User logged in successfully'
        return JsonResponse(response)

    def HomeView(request):
        if request.method == 'POST':
            # Xử lý dữ liệu gửi từ biểu mẫu ở đây
            email = request.POST.get('email')
            password = request.POST.get('password')

            # Thực hiện các xử lý khác (ví dụ: lưu vào cơ sở dữ liệu)

            # Trả lại kết quả
            response_data = {'message': 'Log in successfully!'}
            return JsonResponse(response_data)

class Register(View):
    def get(self, request):
            return render(request=request, template_name="home/../../templates/user/register.html")
    def post(self, request):
        try:
            email = request.POST['email']
        except Exception as e:
            print(e)
            email = None
        try:
            password = request.POST['password']
        except Exception as e:
            print(e)
            password = None
        return HttpResponse(f" Email: {email} - Password: {password}")

    # views.py
    from django.http import JsonResponse


    # def register(request):
    #     form = RegistrationForm()
    #     if request.method == 'POST':
    #         form = RegistrationForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return HttpResponseRedirect('/')
    #     return render(request, 'home/register.html', {'form': form})

class SuccessURLAllowedHostsMixin:
    success_url_allowed_hosts=set()
    def get_success_url_allowed_hosts(self):
        return (self.get_host(), self.success_url_allowed_hosts)

# class LoginView (SuccessURLAllowedHostsMixin, FormView):
#     form_class = AuthenticationForm
#     authentication_form=None
#     redirect_field_name= REDIRECT_FIELD_NAME
#     template_name='user/login-index.html'
#     redirect_authenticated_user = False
#     # extra_contact =
#
#     @method_decorator(sensitive_post_parameters())
#     @method_decorator(csrf_protect())
#     @method_decorator(never_cache())
#     def dispatch(self,request,*args,**kwargs):
#         if self.redirect_authenticated_user and self.request.user.is_authenticated :
#             redirect_to = self.get_success_url()
#             if redirect_to == self.request:
#                 raise ValueError(
#                     "Redirection loop for authenticated user detected. Check that 'your LOGIN_REDIRECT_URL doesn't point to a login page' "
#                 )
#             return HttpResponseRedirect (redirect_to)
#         return super.dispatch(request,*args,**kwargs)
#
#     def get_success_url(self):
#         url = self.get_redirect_url()
#         return url or resolve_url(settings.LOGIN_REDIRECT_URL)
#     def get_direct_url(self):
#         "return the user-originating redirect url if it's safe "
#         redirect_to = self.request.POST.get(
#             self.redirect_field_name,
#             self.request.GET.get(self.redirect_field_name,'')
#         )
#         # url_is_safe = is_safe_url (
#         #     url=redirect_to
#         #     allowed_hosts = self.get_success_url.allowed_hosts(),
#         #
#         # )
#



