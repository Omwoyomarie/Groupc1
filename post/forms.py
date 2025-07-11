from django import forms

from post.models import ItemList


class ItemListForm(forms.ModelForm):
    class Meta:
        model = ItemList
        fields = '__all__'