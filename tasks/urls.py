from django.urls import path, include
from tasks import views

app_name = 'tasks'


urlpatterns = [
        path('create_task_list/', views.CreateTaskListView.as_view(), name='create_task_list'),
        path('<slug:slug>/create_task/', views.CreateTaskView.as_view(), name='create_task'),
        path('task_lists/', views.TaskListView.as_view(), name='task_lists'),
        path('<slug:slug>/task_list_item/', views.TaskItemView.as_view(), name='task_list_item'),
        path('<slug:slug>/update_task_priority/', views.UpdateTaskListPriority.as_view(), name='update_task_priority'),
        path('users_priority_task/', views.UserPriorityList, name='users_prior_list'),
        path('<slug:slug>/user_priority_task', views.showPriority,name='user_priority_task'),
        # path('login/', views.loginview, name='login'),
        # path('logout/', views.logOut, name='logout'),
]
