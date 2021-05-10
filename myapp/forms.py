from django import forms
from .models import Resume

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
)

JOB_CITY_COICES = (
    ('Bangalore', 'Bangalore'),
    ('Hydrabad', 'Hyydrabad'),
    ('Chennai', 'Chennai'),
    ('Gurgaon', 'Gurgaon'),
    ('Noida','Noida'),
    ('Delhi', 'Delhi'),
    ('Mumbai', 'Mumbai'),
    ('Pune', 'Pune'),
)

class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect())
    job_city = forms.MultipleChoiceField(label='Preferred Job Location', choices=JOB_CITY_COICES, widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Resume
        fields = '__all__'
        labels = {
            'name':'Enter Full Name',
            'dob':'Date Of Birth',
            'gender':'Choose Gender',
            'locality':'Enter Your Address',
            'city':'Enter Your City',
            'pin':'Enter Pincode',
            'state':'Select State',
            'mobile':'Enter Mobile Number',
            'email':'Enter Email-Id',
            'job_city':'Select Preffered City',
            }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }




        

