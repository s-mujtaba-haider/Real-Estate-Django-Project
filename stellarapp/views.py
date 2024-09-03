from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import os
# Create your views here.

class UpdateTable(APIView):

    def get(self,request):

        inspectdb_command = "python manage.py inspectdb --database=second_db > stellarapp/models.py"
        os.system(inspectdb_command)
        os.system('python manage.py makemigrations stellarapp')
        os.system('python manage.py migrate')

        return Response ('hello')
