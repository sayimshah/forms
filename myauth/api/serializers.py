from ..models import *
from rest_framework import serializers ,viewsets



class Low_level_UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Low_level_User
        fields = '__all__'

class Mid_level_UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mid_level_User
        fields = '__all__'

class High_level_UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = High_level_User
        fields = '__all__'


# class Custom_userSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['password']

# class CombinedSerializer(serializers.Serializer):
#     model1 = User_detailsSerializer()
#     model2 = Custom_userSerializer()

class LoginSerializer(serializers.ModelSerializer):
    company_id = serializers.IntegerField()
    class Meta:
        model = User
        fields = ['company_id','username','password']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id",'username','email',"is_midlevel","is_lowlevel","is_highlevel"]



class FormValuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormValues
        fields = ('id', 'form', 'values')


# class FormValuesSerializer(serializers.Serializer):
#     form_id = serializers.IntegerField()
#     form_structure_id = serializers.IntegerField()
#     input_values = serializers.ListField(child=serializers.CharField())

#     def validate_form_id(self, form_id):
#         try:
#             Form.objects.get(id=form_id)
#         except Form.DoesNotExist:
#             raise serializers.ValidationError("Form with id {} does not exist.".format(form_id))
#         return form_id

#     def validate_form_structure_id(self, form_structure_id):
#         try:
#             form_structure = FormStructure.objects.get(id=form_structure_id)
#         except FormStructure.DoesNotExist:
#             raise serializers.ValidationError("FormStructure with id {} does not exist.".format(form_structure_id))
#         if form_structure.form_id != self.initial_data.get('form_id'):
#             raise serializers.ValidationError("FormStructure with id {} is not associated with form with id {}.".format(form_structure_id, self.initial_data.get('form_id')))
#         return form_structure_id

