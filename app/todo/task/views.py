from django.shortcuts import render
from django.views.generic import View

class TaskView(View):
    def get(self, request):
        return render(request, 'task/tasks.html', context = {'name': 'RED'})

# Create your views here.
