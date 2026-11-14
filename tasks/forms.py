from django import forms
from .models import Todo


# ModelForm builds its fields and validation rules from the Todo model.
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        # Only these fields appear on the form. created_at is deliberately left out
        # so the user cannot change when a task was created.
        fields = ["title", "description", "completed"]

    def clean_title(self):
        # Django calls clean_<fieldname>() automatically during is_valid().
        # strip() removes leading/trailing spaces, so "   " becomes "".
        title = self.cleaned_data["title"].strip()
        if not title:
            # Rejects an empty or whitespace-only title on the server side.
            raise forms.ValidationError("Title cannot be empty or only spaces.")
        # The cleaned (stripped) title is the value that gets saved.
        return title
