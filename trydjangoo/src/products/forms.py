from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"})) #You can change something if it is required or not
    #email = forms.EmailField()
    description = forms.CharField(
        required=False, 
        widget=forms.Textarea(
            attrs={
                "placeholder":"Your description",
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows":20,
                'cols':120
            }
          )
        )
    price = forms.DecimalField(initial=198.99)
    
    class Meta:
        model = Product 
        fields = [
            'title',
            'description',
            'price'
        ]
        
    #def clean_title(self, *args, **kwargs):
    #    title = self.cleaned_data.get("title")
    #    if not "CFE" in title:
    #        raise forms.ValidationError("This is not a valid title")
    #    if not "news" in title:
    #        raise forms.ValidationError("This is not a valid title")
    #    return title 
    
    #def clean_email(self, *args, **kwargs):
    #    email = self.cleaned_data.get("email")
     #   if not email.endswitch("edu"):
     #       raise forms.ValidationError("This is not a valid email")
     #   return email
#        title = self.cleaned_data.get("title")
#        if not "CFE" in title:
#            raise forms.ValidationError("This is not a valid title")
#        if not "news" in title:
#            raise forms.ValidationError("This is not a valid title")
#        return title
        #title = self.cleaned_data.get("title")
        #if "CFE" in title:
        #    return title
        #else:
        #    raise forms.ValidationError("This is not a valid title") #This is used for validation
        #if not "CFE" in title:
        #   raise forms.ValidationError("This is not a valid title")
        #if not "news" in title:
        #    raise forms.ValidationError("This is not a valid title")
        #return title
    
class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"})) #You can change something if it is required or not
    description = forms.CharField(
        required=False, 
        widget=forms.Textarea(
            attrs={
                "placeholder":"Your description",
                "class": "new-class-name two",
                "id": "my-id-for-textarea",
                "rows":20,
                'cols':120
            }
          )
        )
    price = forms.DecimalField(initial=199.99)        
