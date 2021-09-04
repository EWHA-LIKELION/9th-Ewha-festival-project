from django import forms
from django.forms.widgets import ClearableFileInput
from .models import User #pip install argon2-cffi

class RegisterForm(forms.ModelForm):
    user_id = forms.CharField(
        label='아이디',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'user-id',
                'placeholder':'아이디',
            }
        ),
        error_messages={'required':'아이디를 입력해주세요.',
                        'unique': '중복된 아이디입니다.'}
    )

    user_pw = forms.CharField(
        label='비밀번호',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'user-pw',
                'placeholder':'비밀번호',
            }
        ),
        error_messages={'required':'비밀번호를 입력해주세요.'}
    )

    user_pw_confirm = forms.CharField(
        label='비밀번호 확인',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class' : 'user-pw-confirm',
                'placeholder':'비밀번호 확인',
            }
        ),
        error_messages={'required':'비밀번호가 일치하지 않습니다.'}
    )
    
    user_name = forms.CharField(
        label='이름',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'user-name',
                'placeholder':'이름',
            }
        ),
        error_messages={'required':'이름을 입력해주세요.'}
    )

    user_image = forms.ImageField(
        label='학생증 사진',
        required=True,
    )

    user_phone = forms.CharField(
        label='전화번호',
        required=True,
    )


    user_nickname = forms.CharField(
        label='닉네임',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'user-nickname',
                'placeholder':'닉네임',
            }
        ),
        error_messages={'required':'닉네임을 입력해주세요.',
                        'unique': '중복된 닉네임입니다.'}
    )

    user_email = forms.EmailField(
        label='이메일',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class' : 'user-nickname',
                'placeholder':'이메일',
            }
        ),
        error_messages={'required':'이메일을 입력해주세요.',
        'unique': '중복된 이메일입니다.'}
    )
    
    field_order =[
        'user_name',
        'user_nickname',
        'user_id',
        'user_pw',
        'user_pw_confirm',
        'user_email'
    ]

    class Meta:
        model = User
        fields = [
            'user_id',
            'user_pw',
            'user_name',
            'user_image',
            'user_phone',
            'user_nickname',
            'user_email'
        ]

    def clean(self):
        cleaned_data = super().clean() # super().clean() 메서드를 호출하게 되면 부모 클래스의 모든 유효성 검사 논리가 유지됩니다.

        user_name = cleaned_data.get('user_name','')
        user_nickname = cleaned_data.get('user_nickname','')
        user_id = cleaned_data.get('user_id','')
        user_pw = cleaned_data.get('user_pw','')
        user_pw_confirm = cleaned_data.get('user_pw_confirm','')
        user_email = cleaned_data.get('user_email','')

        if user_pw != user_pw_confirm:
            return self.add_error('user_pw_confirm', '비밀번호가 다릅니다.')
        elif not (4 <= len(user_id) <= 16):
            return self.add_error('user_id', '아이디는 4~16자로 입력해 주세요.')
        elif 8 >len(user_pw):
            return self.add_error('user_pw', '비밀번호는 8자 이상 입력해 주세요.')
        else:
            self.user_id = user_id
            self.user_pw = user_pw
            self.user_pw_confirm = user_pw_confirm
            self.user_name = user_name
            self.user_nickname = user_nickname
            self.user_email = user_email

class LoginForm(forms.Form):
    user_id = forms.CharField(
        max_length=32,
        label='아이디',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class':'user-id',
                'placeholder' : '아이디'
            }
        ),
        error_messages={'required':'아이디를 입력해주세요.'}
    )
    user_pw = forms.CharField(
        max_length=128,
        label='비밀번호',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class':'user-pw',
                'placeholder':'비밀번호'
            }
        ),
        error_messages={'required':'비밀번호를 입력해주세요.'}
    )

    field_order =[
        'user_id',
        'user_pw',
    ]

    def clean(self):
        cleaned_data = super().clean()

        user_id = cleaned_data.get('user_id','')
        user_pw = cleaned_data.get('user_pw','')

        if user_id == '':
            return self.add_error('user_id', '아이디를 다시 입력해주세요.')
        elif user_pw =='':
            return self.add_error('user_pw','비밀번호를 다시 입력해 주세요.')
        else:
            try:
                user = User.objects.get(user_id=user_id)
            except User.DoesNotExist :
                return self.add_error('user_id','아이디가 존재하지 않습니다.')
            
            try:
                user = User.objects.get(user_pw=user_pw)
            except User.DoesNotExist :
                return self.add_error('user_pw','비밀번호가 존재하지 않습니다.')
            
            self.login_session = user.user_id
            #try:
                #PasswordHasher().verify(user.user_pw, user_pw)
            #except exceptions.VerifyMismatchError:
                #return self.add_error('user_pw','비밀번호가 다릅니다.')
