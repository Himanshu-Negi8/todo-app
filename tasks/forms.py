from django import forms
from .models import TaskList, Tasks


class TaskListForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ('list_name', 'priority_list',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.label = ''
            visible.field.widget.attrs['placeholder'] = visible.name


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('task_name', )


class TaskListUpdateForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ('priority_list', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.label = ''
            visible.field.widget.attrs['placeholder'] = visible.name
