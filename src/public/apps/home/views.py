from django.shortcuts import render
from django.views import View
from .models import Items, Img, Categories
from django.http.response import HttpResponse
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


class AddProductView(View):
    def get(self,request):
        # logout(request)
        # if request.user.is_authenticated:
        #      return HttpResponse(request.user.email)

        return render(request=request,template_name="product/addProduct.html")

    def post(self, request):
        title = request.POST['title']
        price = request.POST['price']
        code = request.POST['code']
        category = request.POST['categories']

        category_instance = Categories.objects.get(id=category)
        # condition
        create = Items.objects.create(
            title=title,
            price=price,
            code=code,
            categories=category_instance
        )

        return HttpResponse(f"Them moi san pham thanh cong ID: {create.id}")

