from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .constants import ACCOUNT_TYPE,GENDER_TYPE
from django import forms
from .models import UserBankAccount,UserAddress

class UserRegistrationForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(choices = GENDER_TYPE)
    account_type = forms.ChoiceField(choices = ACCOUNT_TYPE)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=50)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=50)
    
    class Meta:
        model = User
        fields = ['username','password1','password2','first_name','last_name','email','account_type','birth_date','gender','postal_code','street_address','city','country']
    
    def save(self,commit=True):
        our_user = super().save(commit=False)  #not saving the data in DB yet
        if(commit == True):
            our_user.save()  #saving data of user Model
            account_type = self.cleaned_data['account_type']
            gender = self.cleaned_data['gender']
            postal_code = self.cleaned_data['postal_code']
            country = self.cleaned_data['country']
            birth_date = self.cleaned_data['birth_date']
            city = self.cleaned_data['city']
            street_address = self.cleaned_data['street_address']


            UserAddress.objects.create(
                user = our_user,
                postal_code = postal_code,
                country = country,
                city = city,
                street_address = street_address
            )
            UserBankAccount.objects.create(
                user = our_user,
                account_type = account_type,
                birth_date = birth_date,
                gender = gender,
                account_no = 2220109 + our_user.id
            )
            return our_user
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class' : (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                ) 
            })
        
