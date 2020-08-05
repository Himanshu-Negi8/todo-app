from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from .models import Tasks, TaskList
from .forms import TaskListForm, TaskForm, TaskListUpdateForm
from User.models import User
from django.contrib.auth.decorators import login_required


class CreateTaskListView(LoginRequiredMixin, CreateView):
    model = TaskList
    form_class = TaskListForm
    template_name = 'tasks/tasklist_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        user = self.request.user
        if self.object.priority_list is True:
            TaskList.objects.filter(user=user).update(priority_list=False)
            self.object.priority_list = True

        self.object.user = user

        self.object.save()
        return super().form_valid(form)


class UpdateTaskListPriority(LoginRequiredMixin, UpdateView):
    model = TaskList
    template_name = 'tasks/update_task_priority.html'
    form_class = TaskListUpdateForm
    slug_url_kwarg = 'slug'
    slug_field = 'task_list_slug'

    def post(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        user = request.user
        obj = TaskList.objects.get(task_list_slug=slug, user=user)
        self.object = self.get_object()

        if self.object.priority_list is False:
            obj.priority_list = False
            obj.save()
        elif self.object.priority_list:
            TaskList.objects.filter(user=user).update(priority_list=False)
            obj.priority_list = True
            obj.save()
        return super().post(request, *args, **kwargs)


class CreateTaskView(LoginRequiredMixin, CreateView):
    model = Tasks
    form_class = TaskForm
    template_name = 'tasks/task_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        task_list = TaskList.objects.get(task_list_slug=self.kwargs['slug'])

        self.object.task_list = task_list

        user = self.request.user

        self.object.created_by = user

        self.object.save()
        return super().form_valid(form)


class TaskListView(LoginRequiredMixin, ListView):
    model = TaskList
    template_name = 'tasks/task_list.html'


class TaskItemView(LoginRequiredMixin, ListView):
    model = Tasks
    template_name = 'tasks/task_item.html'

    def get_queryset(self):
        ob = TaskList.objects.get(task_list_slug=self.kwargs['slug'])
        return Tasks.objects.filter(task_list=ob)


@login_required
def UserPriorityList(request):
    user = User.objects.all()
    context = {'user': user}
    return render(request, 'tasks/user_list.html', context)


@login_required
def showPriority(request, slug):
    user = User.objects.get(username=slug)
    try:
        ob = TaskList.objects.get(priority_list=True, user=user)
    except TaskList.DoesNotExist:
        return HttpResponse("no priority list")
    context = {'priority': ob}
    return render(request, 'tasks/priority_list.html', context)
