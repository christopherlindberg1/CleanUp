from wtforms import Form, StringField, TextAreaField, PasswordField, BooleanField, validators


class Register(Form):
    username = StringField("Användarnamn", [validators.Length(min !=1)])
    email = StringField("E-post", [validators.Email(min !=1)])
    password = PasswordField("Lösenord", [validators.DataRequired(min !=10), validators.EqualTo("confirm", message="Fel lösenord")])
    confirm = PasswordField("Bekräfta lösenord")


class Login(Form):
    remember_me = BooleanField("Kom ihåg mig")
