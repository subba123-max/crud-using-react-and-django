from rest_framework import  serializers
from studentapp.models import Student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('pk','name','email','document','phone','registrationDate')