from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from catalog.form import ProductForm, VersionForm
from catalog.models import Product, Version


class UserLoginRequiredMixin(LoginRequiredMixin):
    login_url = "/users/"
    permission_denied_message = "только для авторизованных пользователей"


class ProductListView(UserLoginRequiredMixin, ListView):
    model = Product
    template_name = "catalog/products_list.html"
    context_object_name = "products"
    ordering = ["price_pay"]  # сортирует товары по цене в порядке возрастания
    paginate_by = 10  # на странице показывает товары по 10 штук

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset

    def get_context_data(self, *args, object_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        for product in context_data['object_list']:
            status_version = Version.objects.filter(product=product, status_version=True).first()
            product.status_version = status_version
        return context_data


class ProductDetailView(UserLoginRequiredMixin, DetailView):
    model = Product
    # template_name = "catalog/product_detail.html"  # выводит подробную информацию о товаре


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Имя пользователя : {name}\nТелефон: {phone}\nСообщение: {message}")

    return render(request, 'catalog/contacts.html')


class ProductDeleteView(UserLoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:products_list')


class ProductCreateView(UserLoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm

    success_url = reverse_lazy('catalog:products_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(UserLoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))




