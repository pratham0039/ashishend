from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record, Test

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	








class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
    
    
    total_price = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Price For Customer", "class":"form-control"}), label="")
    lab_choices = [
        ('Ashish_Lab', 'Ashish_Lab'),
        ('City_Lab', 'City_Lab'),
        ('Public_Lab', 'Public_Lab'),
        ('Modern_Lab', 'Modern_Lab'),
        ('lab5', 'Lab 5')
    ]
    lab = forms.ChoiceField(choices=lab_choices, widget=forms.Select(attrs={"class": "form-control"}), required=True, label="Lab")
    tests = forms.ModelMultipleChoiceField(queryset=Test.objects.all(), required=False, widget=forms.widgets.CheckboxSelectMultiple)
    paid = forms.ChoiceField(choices=(('paid', 'Paid'), ('udhaar', 'Udhaar')), widget=forms.widgets.RadioSelect(), required=True, label='Payment Option')



    class Meta:
        model = Record
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        super(AddRecordForm, self).__init__(*args, **kwargs)
        tests = Test.objects.all()
        for test in tests:

            self.fields['tests'].widget.attrs['data-price'] = test.Price

    def add_lab_choice(self, label, value):
        """
        Method to dynamically add a new lab choice.
        """
        self.fields['lab'].choices.append((label, value))
            


		



class ProductForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['code', 'testname', 'Price']