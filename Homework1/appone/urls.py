from django.urls import path
from .views import (EmployeeListView,
                    EmployeeAddView,
                    EmployeeUpdateView,
                    EmployeeDeleteView,
                    EmployeeDetailView
                    )

urlpatterns = [
    path('', EmployeeListView.as_view(), name='home'),
    path('employee/new/', EmployeeAddView.as_view(), name='employee-create'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee-create'),
    path('employee/<int:pk>/update/', EmployeeUpdateView.as_view(), name='employee-update'),
    path('employee/<int:pk>/update/', EmployeeDeleteView.as_view(), name='employee-delete'),
]
