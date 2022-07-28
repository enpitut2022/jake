from django import forms

#フォームクラス作成
class EnechanFormClass(forms.Form):
    content = forms.CharField(widget=forms.Textarea(), max_length=1000, label="内容")