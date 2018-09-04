from django import forms
from django.contrib.auth import get_user_model
from .models import Profil
from django.core.validators import RegexValidator
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class LoginForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields=['username','password']
        widgets = {
            'password':forms.PasswordInput(attrs={
				'class':'form-control',
				'placeholder':'Password'
				}),
			'username':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'ID'
				}),
		}

class UserCreationForm(forms.ModelForm):
	password = forms.CharField(
		label = 'Password',
		widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'password',})
	)

	password2 = forms.CharField(
		label = 'Password Confirmation',
		widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'password',})
	)

	phone_num = forms.IntegerField( widget=forms.NumberInput(
		attrs = {
			'class' : 'form-control',
			'placeholder':'-없이 번호만 입력하세요.',
		})
	)

	address = forms.CharField(widget=forms.TextInput(
		attrs = {'class':'form-control','placeholder':'주소를입력해주세요.'}),
		required=False
	)

	email = forms.CharField(widget=
		forms.EmailInput(attrs={
			'class':'form-control',
			'placeholder':'email@xxxxx.com',
			}))

	class Meta:
		model = get_user_model()
		fields = ['username','nickname','Photo','in_short']
		widgets = {
			'username':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'id'
				}),
			'nickname':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'닉네임을 입력해주세요.'
				}),
			'Photo':forms.FileInput(attrs={
				'class':'form-control',
				
				}),
			'in_short':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'한마디를 입력해주세요.'
				}),
		}
		
	def clean_username(self):
		username = self.cleaned_data.get('username', None)
		if username is None:
			raise forms.ValidationError("아이디를 입력해주세요.")
		else:
			unique_test= get_user_model().objects.all().filter(username=username)
			if unique_test:
				raise forms.ValidationError("동일한 아이디가 존재합니다.")
		return username

	def clean_nickname(self):
		nickname = self.cleaned_data.get('nickname',None)
		if nickname is None:
			raise forms.ValidationError("닉네임을 입력해주세요.")
		else:
			unique_test= get_user_model().objects.all().filter(nickname=nickname)
			if unique_test:
				raise forms.ValidationError("동일한 닉네임이 존재합니다.")
		return nickname

	def clean(self):
		email = self.cleaned_data.get("email",None)
		password = self.cleaned_data.get("password",None)
		password2 = self.cleaned_data.get("password2",None)
		password_isalpha = password[0].isalpha()
		
		if len(password) < 8:
			raise forms.ValidationError("비밀번호가 짧습니다. 최소 8글자 이상 입력해 주세요(영문+숫자)")
		if all(c.isalpha() == password_isalpha for c in password):
			raise forms.ValidationError("비밀번호는 영문과 숫자 조합으로 다시 입력해 주세요.")
		if password and password2 and password != password2:
			raise forms.ValidationError("두 비밀번호가 다릅니다.")
		
		if email is None:
			raise forms.ValidationError("이메일을 입력해주세요.")
		else:
			user_data= Profil.objects.all().filter(email=email)
			if user_data:
			 	raise forms.ValidationError("동일한 이메일이 존재합니다.")
		return self.cleaned_data

	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data["password"])
		if commit:
			user.save()
			email = self.cleaned_data['email']
			address = self.cleaned_data['address']
			phone_num = self.cleaned_data.get('phone_num',000)
			Profil.objects.create(user=user, email=email, address=address,phone_number=phone_num)
			
		return user

class UserUpdateForm(forms.ModelForm):
	phone_num = forms.IntegerField( widget=forms.NumberInput(
		attrs = {
			'class' : 'form-control',
			'placeholder':'-없이 번호만 입력하세요.',
		})
	)

	address = forms.CharField(widget=forms.TextInput(
		attrs = {'class':'form-control','placeholder':'주소를입력해주세요.'}),
		required=False
	)

	email = forms.CharField(widget=
		forms.EmailInput(attrs={
			'class':'form-control',
			'placeholder':'email@xxxxx.com',
			}))

	class Meta:
		model = get_user_model()
		fields = ['username','nickname','Photo','in_short']
		widgets = {
			'username':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'id'
				}),
			'nickname':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'닉네임을 입력해주세요.'
				}),
			'Photo':forms.FileInput(attrs={
				'class':'form-control',
				
				}),
			'in_short':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'한마디를 입력해주세요.'
				}),
		}
		
	def clean_username(self):
		username = self.cleaned_data.get('username', None)
		if username is None:
			raise forms.ValidationError("아이디를 입력해주세요.")
		else:
			unique_test= get_user_model().objects.all().filter(username=username)
			if unique_test:
				raise forms.ValidationError("동일한 아이디가 존재합니다.")
		return username

	def clean_nickname(self):
		nickname = self.cleaned_data.get('nickname',None)
		if nickname is None:
			raise forms.ValidationError("닉네임을 입력해주세요.")
		else:
			unique_test= get_user_model().objects.all().filter(nickname=nickname)
			if unique_test:
				raise forms.ValidationError("동일한 닉네임이 존재합니다.")
		return nickname

	def clean(self):
		email = self.cleaned_data.get("email",None)
		
		if email is None:
			raise forms.ValidationError("이메일을 입력해주세요.")
		else:
			user_data= Profil.objects.all().filter(email=email)
			if user_data:
			 	raise forms.ValidationError("동일한 이메일이 존재합니다.")
		return self.cleaned_data

	def save(self, commit=True):
		user = super().save(commit=False)
		if commit:
			user.save()
			email = self.cleaned_data['email']
			address = self.cleaned_data['address']
			phone_num = self.cleaned_data.get('phone_num',000)
			
		return user

#admin전용
class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = get_user_model()
        fields = ['username','nickname','level','exp','point', 'password', 'is_active', 'is_staff']

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]