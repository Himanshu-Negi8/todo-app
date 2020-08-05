from django.db import models
from django.contrib.auth import settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify
User = get_user_model()
# Create your models here.


class TaskList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    list_name = models.CharField(max_length=100)
    priority_list = models.BooleanField(default=False)
    task_list_slug = models.SlugField(allow_unicode=True, unique=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["priority_list", "created_at"]

    def __str__(self):
        return self.list_name

    def save(self, *args, **kwargs):
        self.task_list_slug = slugify(self.list_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        # return reverse('home')
        return reverse('tasks:task_lists')


class Tasks(models.Model):
    task_name = models.CharField(max_length=100)
    task_list = models.ForeignKey(TaskList, verbose_name=TaskList, on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_name

    def get_absolute_url(self):

        return reverse('home')









