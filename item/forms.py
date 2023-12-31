from django import forms

from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description','price', 'image',)
    
        widgets = {
            'category': forms.Select(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border bg-gray-200'
                }),
                'name': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border bg-gray-200'
                }),
                'description': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border bg-gray-200'
                }),
                'price': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border bg-gray-200'
                }),
                'image': forms.FileInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border bg-gray-200'
                }),
}
        
class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description','price', 'image', 'is_sold',)
    
        widgets = {
                'name': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border bg-gray-200'
                }),
                'description': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border bg-gray-200'
                }),
                'price': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border bg-gray-200'
                }),
                'image': forms.FileInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border bg-gray-200'
                }),
}