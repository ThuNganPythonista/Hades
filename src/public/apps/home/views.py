from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Items, Img

class Homeview(View):
    def get(self,request):
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

class Login(View):
    def get(self, request):
        return render(request=request, template_name="home/login-index.html")

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