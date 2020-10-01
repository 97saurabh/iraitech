from django import forms


class solutionForm(forms.Form):
    
    x = forms.IntegerField()
    a = forms.IntegerField()
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.fields['x'].label = "Value of X"
        self.fields['a'].label = "Value of N"
        



    def is_valid(self):
        
        valid = super(solutionForm, self).is_valid()
        
        if self.cleaned_data['x'] == 0:
            self._errors['x can not be zero'] = 'x can not be zero'
            return False
        
        return True