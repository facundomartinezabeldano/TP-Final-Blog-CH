from django import forms


class CreateBlogForm(forms.Form):
    title = forms.CharField(max_length=10)
    sub_title = forms.CharField(max_length=15)
    body = forms.CharField(max_length=300)
    author = forms.CharField(max_length=10)
    #date = forms.DateTimeField(auto_now=True)
    # img = forms.BinaryField
