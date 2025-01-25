from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer,WorkoutSerializer,ExerciseSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Workout,Exercise

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class WorkoutCreate(generics.ListCreateAPIView):
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user1 = self.request.user
        return Workout.objects.filter(user=user1)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)
        else:
            print(serializer.errors)

class WorkoutDelete(generics.DestroyAPIView):
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user1 = self.request.user
        return Workout.objects.filter(user=user1)
    

class ExerciseCreate(generics.ListCreateAPIView):
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
     user = self.request.user
     return Exercise.objects.filter(workout__user=user)#underscore follows relationships
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            workout_id = self.request.data.get('workout')  # Get workout ID from the request body
            workout = Workout.objects.get(id=workout_id, user=self.request.user)  # Validate ownership
            serializer.save(workout=workout)
        else:
            print(serializer.errors)
class ExerciseDelete(generics.DestroyAPIView):
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
     user = self.request.user
     return Exercise.objects.filter(workout__user=user)#underscore follows relationships


        
        




    
    



