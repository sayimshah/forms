from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework import permissions, authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import GenericAPIView
from .serializers import *
from ..models import *
from rest_framework import status
from rest_framework import generics



class mid_level_user_register(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = Mid_level_UserSerializer
    def post(self, request):
        first_name = request.data['first_name']
        last_name = request.data['last_name'] 
        company_id = request.data['last_name'] 
        phone_number = request.data['phone_number']
        email = request.data['email']
        password = request.data['password']
        address = request.data['address']
        Is_user = User.objects.filter(username=phone_number).exists()
        if Is_user:
            response={
                "message" : 'Already Registered!',
            }
        else:
            user = User.objects.create_user(phone_number, email, password)
            user_info=Mid_level_User.objects.create(first_name=first_name,last_name=last_name,phone_number=phone_number,address=address,email=email,user=user)
            
            user.is_active=True
            user.is_midlevel=True
            user.save()
            refresh = RefreshToken.for_user(user)
            if user_info is not None:
                user_serializer=Mid_level_UserSerializer(user_info)
                response={
                    "result" : user_serializer.data,
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    "message" : 'Registered Successfully',
                    "status" : 1
                }
            else:
                response={
                    "message" : 'Sorry, something went wrong !',
                    "status" : 0
                }
        return Response(response)


class low_level_user_register(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = Low_level_UserSerializer
    def post(self, request):
        first_name = request.data['first_name']
        last_name = request.data['last_name'] 
        phone_number = request.data['phone_number']
        email = request.data['email']
        password = request.data['password']
        address = request.data['address']
        Is_user = User.objects.filter(username=phone_number,email=email)
        if Is_user.exists():
            response={
                "message" : 'Already Registered!',
            }
        else:
            user = User.objects.create_user(phone_number, email, password)
            user_info=Low_level_User.objects.create(first_name=first_name,last_name=last_name,phone_number=phone_number,address=address,email=email,user=user)
            user.is_active=True
            user.is_lowlevel=True
            user.save()
            refresh = RefreshToken.for_user(user)
            if user_info is not None:
                user_serializer=Low_level_UserSerializer(user_info)
                response={
                    "result" : user_serializer.data,
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    "message" : 'Registered Successfully',
                    "status" : 1
                }
            else:
                response={
                    "message" : 'Sorry, something went wrong !',
                    "status" : 0
                }
        return Response(response)



class high_level_user_register(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = High_level_UserSerializer
    def post(self, request):
        first_name = request.data['first_name']
        last_name = request.data['last_name'] 
        phone_number = request.data['phone_number']
        email = request.data['email']
        password = request.data['password']
        address = request.data['address']
        Is_user = User.objects.filter(username=phone_number).exists()
        if Is_user:
            response={
                "message" : 'Already Registered!',
            }
        else:
            user = User.objects.create_user(phone_number, email, password)
            user_info=High_level_User.objects.create(first_name=first_name,last_name=last_name,phone_number=phone_number,address=address,email=email,user=user)
            user.is_active=True
            user.is_highlevel=True
            user.save()
            refresh = RefreshToken.for_user(user)
            if user_info is not None:
                user_serializer=High_level_UserSerializer(user_info)
                response={
                    "result" : user_serializer.data,
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    "message" : 'Registered Successfully',
                    "status" : 1
                }
            else:
                response={
                    "message" : 'Sorry, something went wrong !',
                    "status" : 0
                }
        return Response(response)

class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]



    def post(self, request):
        company_id = request.data.get("company_id")
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},status=status.HTTP_400_BAD_REQUEST)
        companyid = User.objects.filter(id =company_id).exists()
        if companyid :
            user = authenticate(username=username, password=password)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({ 
                "message" : 'Success',
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
            else:
                return Response({'error': 'Invalid username or password'},status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Invalid company ID'},status=status.HTTP_400_BAD_REQUEST)
        
        
class ListFormView(APIView):
    def get(self, request):
        form_structures = FormStructure.objects.select_related('form', 'input_type',).all()
        data = []
        for form_structure in form_structures:
            form_data = {
                'form_name': form_structure.form.form_name,
                'input_type': form_structure.input_type.input_type,
                'is_required':form_structure.is_required,
                'input_name':form_structure.input_name,
            }
            data.append(form_data)
        return Response(data)


class DynamicFormView(APIView):
    def get(self, request, pk):
        form_structures = FormStructure.objects.select_related('form', 'input_type').filter(form__pk=pk)
        data = []
        for form_structure in form_structures:
            form_data = {
                'input_type': form_structure.input_type.input_type,
                'input_name':form_structure.input_name,
                'is_required':form_structure.is_required,
            }
            data.append(form_data)
        return Response(data)


# class FormValuesView(APIView):
#     def post(self, request, format=None):
#         form_id = request.data.get('form_id')
#         values = request.data.get('values')
#         try:
#             values_str = str(values)
#             form_values = FormValues(form_id=form_id, values=values_str)
#             form_values.save()
#             return Response(status=status.HTTP_201_CREATED)
#         except Exception as e:
#             return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": str(e)})


# class FormValuesCreateView(generics.CreateAPIView):
#     queryset = FormValues.objects.all()
#     serializer_class = FormValuesSerializer

#     def post(self, request, *args, **kwargs):
#         form_structure_id = request.data.get('form_structure_id')
#         input_values = request.data.get('input_values')

#         form_structure = FormStructure.objects.get(id=form_structure_id)
#         FormValues.objects.create(form=form_structure, values=str(input_values))

#         return Response({'message': 'Form values saved successfully'})

# class FormValuesCreateView(generics.CreateAPIView):
#     queryset = FormValues.objects.all()
#     serializer_class = FormValuesSerializer

#     def post(self, request, *args, **kwargs):
#         form_id = request.data.get('form_id')
#         form_structure_id = request.data.get('form_structure_id')

#         if not form_id or not form_structure_id:
#             return Response({'status': 'error', 'message': 'Missing form or form structure ID.'}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             form = Form.objects.get(id=form_id)
#             form_structure = FormStructure.objects.get(id=form_structure_id, form=form)
#         except (Form.DoesNotExist, FormStructure.DoesNotExist):
#             return Response({'status': 'error', 'message': 'Invalid form or form structure ID.'}, status=status.HTTP_400_BAD_REQUEST)

#         input_values = request.data.get('input_values')

#         if not input_values:
#             return Response({'status': 'error', 'message': 'Missing input values.'}, status=status.HTTP_400_BAD_REQUEST)

#         for input_value in input_values:
#             if not input_value:
#                 return Response({'status': 'error', 'message': 'Input value cannot be empty.'}, status=status.HTTP_400_BAD_REQUEST)

#         for input_value in input_values:
#             form_value = FormValues.objects.create(form=form_structure, values=str(input_value))

#         return Response({'status': 'success'}, status=status.HTTP_201_CREATED)

class FormValuesCreateView(generics.CreateAPIView):
    queryset = FormValues.objects.all()
    serializer_class = FormValuesSerializer

    def post(self, request, *args, **kwargs):
        form_id = request.data.get('form_id')

        if not form_id:
            return Response({'status': 'error', 'message': 'Missing form or form structure IDs.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            form = Form.objects.get(id=form_id)
        except (Form.DoesNotExist, FormStructure.DoesNotExist):
            return Response({'status': 'error', 'message': 'Invalid form or form structure IDs.'}, status=status.HTTP_400_BAD_REQUEST)

        input_values = request.data.get('input_values')

        if not input_values:
            return Response({'status': 'error', 'message': 'Missing input values.'}, status=status.HTTP_400_BAD_REQUEST)

        for input_value in input_values:
            if not input_value.get('value') or not input_value.get('form_structure_id'):
                return Response({'status': 'error', 'message': 'Input value or form structure ID cannot be empty.'}, status=status.HTTP_400_BAD_REQUEST)

        for input_value in input_values:
            form_structure_id = input_value.get('form_structure_id')
            form_structure = FormStructure.objects.get(id=form_structure_id)
            form_value = FormValues.objects.create(form=form_structure, values=(input_value.get('value')))

        return Response({'status': 'success'}, status=status.HTTP_201_CREATED)