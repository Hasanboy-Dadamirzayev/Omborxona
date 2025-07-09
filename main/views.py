from django.shortcuts import render, redirect, get_object_or_404
from django.template.context_processors import request
from django.views import View
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "bo'limlar.html")




class ProductsView(LoginRequiredMixin, View):
    def get(self, request):
        products = Product.objects.filter(branch=request.user.branch).order_by('name')
        context = {
            'products': products
        }
        return render(request, 'mahsulotlar.html', context)

    def post(self, request):
        Product.objects.create(
            name=request.POST.get('name'),
            brand=request.POST.get('brand'),
            import_price=request.POST.get('price1'),
            export_price=request.POST.get('price2') or None,
            amount=request.POST.get('amount'),
            branch=request.user.branch,
        )
        return redirect('products')


class ProductUpdateView(LoginRequiredMixin, View):
    def get(self, request, product_id):
        product = Product.objects.filter(id=product_id, branch=request.user.branch)
        context = {
            'product': product
        }
        return render(request, 'mahsulot-tahrirlash.html', context)

    def post(self, reuqest, product_id):
        product = get_object_or_404(Product, id=product_id, branch=request.user.branch)
        product.name=reuqest.POST.get('name')
        product.brand=reuqest.POST.get('brand')
        product.export_price=reuqest.POST.get('price2')
        product.import_price=reuqest.POST.get('price1')
        product.amount=reuqest.POST.get('amount')
        product.branch=request.user.branch
        product.save()
        return redirect('products')


class ProdcutDeleteView(View):
    def get(self, request, product_id):
        if request.is_authenticated:
            product = get_object_or_404(Product, id=product_id)
            context = {
                'product': product
            }
            return render(request, 'mahsulot_delete.html', context)
        else:
            return redirect('login')

    def post(self, request, product_id):
        if request.is_authenticated:
            product = get_object_or_404(Product, id=product_id)
            product.delete()
            return redirect('products')

class CustomersView(LoginRequiredMixin, View):
    def get(self, request):
        customers = Customer.objects.filter(branch=request.user.branch).order_by('name')
        context = {
            'customers': customers
        }
        return render(request, 'mijozlar.html')

    def post(self, request):
        pass
