from django import forms
from todo.models import Todo


# class TodoForm(forms.Form):
#     title = forms.CharField()
#     description = forms.CharField(widget=forms.Textarea)
#     status = forms.ChoiceField(
#         choices=[("TD", "todo"), ("IN", "in-progress"), ("DN", "done")]
#     )
#     due_date = forms.DateField(widget=forms.SelectDateWidget)


class AddTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "status": forms.Select(
                attrs={"class": "form-select"},
            ),
            "due_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
        }


class UpdateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        # fields = "__all__"
        exclude = ["title"]
        widgets = {
            # "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "status": forms.Select(
                attrs={"class": "form-select"},
            ),
            "due_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
        }