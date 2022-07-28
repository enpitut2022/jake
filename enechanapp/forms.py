from django import forms

from enechanapp.models import Post

#フォームクラス作成
class EnechanFormClass(forms.Form):
    content = forms.CharField(widget=forms.Textarea(), max_length=1000, label="内容")


class PostFrom(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('date', 'text')