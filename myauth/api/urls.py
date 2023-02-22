from django.urls import path, include
from rest_framework import routers
from .users_authentication import *


router = routers.DefaultRouter()
# router.register(r'formstructure', FormStructureViewSet)


urlpatterns=[
    
    path('', include(router.urls)),
    path('mid_level_user_register/', mid_level_user_register.as_view()),
    path('low_level_user_register/', low_level_user_register.as_view()),
    path('high_level_user_register/', high_level_user_register.as_view()),
    path('form/<int:pk>/', DynamicFormView.as_view(), name='dynamic_form_view'),
    path('ListFormView/', ListFormView.as_view()),
    path('form-values/', FormValuesCreateView.as_view(), name='form_values'),
    path('login/', LoginView.as_view(), name='login'),

]