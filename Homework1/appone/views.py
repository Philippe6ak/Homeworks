from django.shortcuts import render
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from .models import Products, Employee
# Create your views here.


class EmployeeListView(ListView):
    model = Employee
    template_name = 'appone/EmpList.html'
    context_object_name = 'employees'
    paginate_by = 5


class ProductsListView(ListView):
    model = Products
    template_name = 'appone/ProdList.html'
    context_object_name = 'products'
    paginate_by = 5


class EmployeeAddView(CreateView):
    model = Employee
    fields = ['first_name', 'last_name']

    def form_valid(self, form):
        return self.form_valid(form)


class ProductAddView(CreateView):
    model = Products
    fields = ['prod_name', 'price']

    def form_valid(self, form):
        return self.form_valid(form)


class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ['first_name', 'last_name']

    def form_valid(self, form):
        return self.form_valid(form)


class ProductUpdateView(UpdateView):
    model = Products
    fields = ['prod_name', 'price']

    def form_valid(self, form):
        return self.form_valid(form)


class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = '/'


class ProductDeleteView(DeleteView):
    model = Products
    success_url = '/'


class EmployeeDetailView(DeleteView):
    model = Employee
