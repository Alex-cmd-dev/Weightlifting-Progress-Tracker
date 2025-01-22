from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Workout, Exercise


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargss = {'password': {'write_only': True}} #no one can read the password

    def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            return user
    
class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'date', 'user']
        extra_kwargss = {'user': {'read_only': True}} 
    

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'workout', 'name', 'sets', 'reps', 'weight']
        extra_kwargss = {'workout': {'write_only': True}} 