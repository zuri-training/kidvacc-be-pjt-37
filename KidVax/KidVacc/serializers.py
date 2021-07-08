from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Child, Parent, Hospital_Details, Hospital_Type, Appointment


# creating a model serializer

class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    Phone_number = serializers.IntegerField(required=True, write_only=True) #n
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    ("A user is already registered with this e-mail address."))
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(
                ("The two password fields didn't match."))
        return data

    def get_cleaned_data(self):
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'Phone_number': self.validated_data.get('Phone_number', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.save()
        return user


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = [
            'id', 'First_name', 'Middle_name', 'Last_name', 'Gender', 'Blood_group', 'Genotype', 'Vaccination_history', 'images',
        ] #'Date_of_birth'

class ParentSerializer(serializers.ModelSerializer):
    First_name = serializers.CharField(required=True,
                                       validators=[UniqueValidator(queryset=Parent.objects.all())])

    Last_name = serializers.CharField(required=True,
                                      validators=[UniqueValidator(queryset=Parent.objects.all())])

    Gender = serializers.CharField(required=True,
                                   validators=[UniqueValidator(queryset=Parent.objects.all())])

    Email_address = serializers.EmailField(required=True,
                                           validators=[UniqueValidator(queryset=Parent.objects.all())])

    Password = serializers.CharField(min_length=8, write_only=True)

    Phone_number = serializers.IntegerField(required=True,
                                            validators=[UniqueValidator(queryset=Parent.objects.all())])

    images = serializers.ImageField(required=True,
                                    validators=[UniqueValidator(queryset=Parent.objects.all())])

    def create(self, validated_data):
        parent = Parent.objects.create(validated_data['First_name'],
                                       validated_data['Last_name'],
                                       validated_data['Gender'],
                                       validated_data['Email_address'],
                                       validated_data['Password'],
                                       validated_data['Phone_number'],
                                       validated_data['images']
                                       )

        return parent

    class Meta:
        model = Parent
        fields = [
            'First_name', 'Last_name', 'Gender', 'Email_address', 'Password', 'Phone_number', 'images'
        ]


class Hospital_DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital_Details
        fields = [
            'hospital_Name', 'name', 'hospital'
        ]


class Hospital_TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital_Type
        fields = [
            'hospital_type', 'name'
        ]


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        models = Appointment
        fields = [
            'date', 'start_time', 'end_time', 'parent'
        ]




