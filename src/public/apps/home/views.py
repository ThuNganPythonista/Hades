from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Items, Img
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import login, logout
# from .forms import RegistrationForm
from django.http import HttpResponseRedirect


class HomeView(View):
    def get(self,request):
        # logout(request)
        # if request.user.is_authenticated:
        #      return HttpResponse(request.user.email)

        return render(request=request,template_name="home/index.html")


class AboutUs(View):
    def get(self,request):
        return render(request=request,template_name="home/messenger.html")

class News(View):
    def get(self,request):
        return render(request=request,template_name="home/product.html")
class Sell(View):
    def get(self,request):
        return render(request=request,template_name="home/test.html")

class Quyen(View):
    def get(self,request):
        return render(request=request,template_name="home/quyengop.html")

class Map(View):
    def get(self,request):
        return render(request=request,template_name="home/map.html")
class Footwear(View):

    def get(self,request):
        context = {
            'products': Items.objects.all()
        }

        # test code
        products = Items.objects.all()
        for item in products:
            print(item.img_set.first().img.url)
        return render(request=request,template_name="home/product.html", context=context)

class Login(View):
    def get(self, request):
        return render(request=request, template_name="home/login-index.html")

    def post(self, request):
        # try:
        #     email = request.POST['email']
        # except Exception as e:
        #     print(e)
        #     email = None
        # try:
        #     password = request.POST['password']
        # except Exception as e:
        #     password = None

        try:
            email = request.POST['username']
        except Exception as e:
            print(e)
            email = None
        try:
            password = request.POST['password']
        except Exception as e:
            password = None
        #
        response = {'status': False, 'message': ''}
        if email == "" or password == "":
            response['message'] = 'Username or password is not empty'
            return JsonResponse(response)

        user_login = ModelBackend().authenticate(request=request, username=email, password=password)
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
            return render(request=request, template_name="home/register.html")
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
    #


    # def get(self,request):
    #     productArray = []
    #     products = Items.objects.all()
    #     for product in products:
    #         try:
    #             product_image = Img.objects.filter(product_id=product.id).all().first().img.url
    #         except Exception as e:
    #             product_image = None
    #             print(f"product_image: {e}")
    #
    #         productArray.append({
    #             'product': product,
    #             'product_image': product_image
    #         })
    #     context = {
    #         'products': productArray,
    #     }
    #     return render(request=request,template_name="home/product.html", context=context)