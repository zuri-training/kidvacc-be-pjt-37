from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Child, Parent, Hospital_Details, Hospital_Type,  Appointment


# creating a model serializer


class ChildSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Child
        fields = [
            'id', 'First_name', 'Middle_name', 'Last_name', 'Gender', 'Date_of_birth',
                        'Blood_group', 'Genotype', 'Vaccination_history','images'
        ]


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
            'First_name', 'Last_name', 'Gender', 'Email_address','Password', 'Phone_number', 'images' 
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
            'hospital_type','name' 
        ]



class AppointmentSerializer(serializers.ModelSerializer):

    class Meta :
        models = Appointment
        fields = [
            'date', 'start_time', 'end_time', 'parent'
        ]



