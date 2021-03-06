from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator

from django.http import JsonResponse
from django.forms.models import model_to_dict

from .models import Task
from .forms import TaskForm

@method_decorator(ensure_csrf_cookie, name='post')
class TaskView(View):
    def get(self, request):
        tasks = list(Task.objects.values())
        if request.is_ajax():
            return JsonResponse({'tasks': tasks}, status=200)
        
        return render(request, 'task/tasks.html')

    def post(self, request):
        bound_form = TaskForm(request.POST)

        if bound_form.is_valid():
            new_task = bound_form.save()
            return JsonResponse({'task': model_to_dict(new_task)}, status=200)
            
        return redirect('tasks_list_url')

@method_decorator(ensure_csrf_cookie, name='post')
class TaskComplete(View):
    def post(self, request, id):
        task = Task.objects.get(id=id)
        if task.completed == False:
            task.completed = True
        else:
            task.completed = False
        task.save()
        return JsonResponse({'task': model_to_dict(task)}, status=200)

@method_decorator(ensure_csrf_cookie, name='post')
class TaskDelete(View):
    def post(self, request, id):
        task = Task.objects.get(id=id)
        task.delete()
        return JsonResponse({'result': '200'}, status=200)