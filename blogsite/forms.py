from django import forms  

class PostForm(forms.Form):  
    title = forms.CharField(label="Title",max_length=255)
    content = forms.CharField(label="Content")
    author = forms.CharField(label="Author")