from django import forms
from .models import ToDoList

class ToDoListForm(forms.ModelForm):
    content = forms.CharField(label='')
    
    class Meta:
        model  = ToDoList
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super(ToDoListForm, self).__init__(*args, **kwargs)

        self.fields['content'].widget.attrs = {'class':'msg'}