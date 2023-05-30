from django import forms

CHOICES = [
    ("male", "MALE"),
    ("female", "male"),
]

# CHOICES = [
#     "male"
# ]

class AddForm(forms.Form):
    usn_number = forms.CharField(label="",max_length=10, widget=forms.Textarea(attrs={"class":"shadow form-control mr-05 ml-03","columns":"5", "rows":"1","placeholder":"USN number","name":""})) #, widget=forms.Textarea(attrs={"class":"form-sml"}))
    name = forms.CharField(label="", max_length=64, widget=forms.Textarea(attrs={"class":"shadow form-control mr-05 ml-03","columns":"5", "rows":"1","placeholder":"Name","name":""}))
    email = forms.EmailField(label="", max_length=64, widget=forms.EmailInput(attrs={"class":"shadow form-control", "type":"email", "id":"email-1", "name":"email", "placeholder":"Email"}))
    gpa = forms.FloatField(label="", max_value=10.0, min_value=0.0, widget=forms.NumberInput(attrs={"class":"shadow form-control", "placeholder":"gpa" }))
    subject = forms.CharField(label="", max_length=65, required=False,widget=forms.Textarea(attrs={"class":"shadow form-control mr-05 ml-03","columns":"5", "rows":"1","placeholder":"Subject","name":""}))
    gender = forms.ChoiceField(label="", required=False ,choices=CHOICES, widget=forms.Textarea(attrs={"class":"shadow form-control mr-05 ml-03","columns":"5", "rows":"1","placeholder":"Gender","name":""})) #[("MALE","MALE"), ("FEMALE", "FEMALE")])

    # gender = forms.ChoiceField( choices=["male", "femla"], required=False)
    # gender = forms.CharField(max_length=100, choices=CHOICES, null=True)

    # forms.CharField(max_length=65, forms.ChoiceField(, choices=[CHOICES], required=False))

    # def clean(self):
    #     cleaned_data = super().clean()
    #     first_name = cleaned_data.get("first_name")
    #     last_name = cleaned_data.get("last_name")
    #     email = cleaned_data.get("email")
    #     gpa = cleaned_data.get("gpa")
    #     subject = cleaned_data.get("subject")
        

    #     if not first_name and not last_name and not email and not gpa and not subject:
    #         raise forms.ValidationError("You have to write something!")
        
    # widgets = [
        
    # ]