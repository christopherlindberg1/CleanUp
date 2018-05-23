from wtforms import Form, StringField, TextAreaField, PasswordField, BooleanField, validators


class Register(Form):
    email = StringField("E-post", [validators.Email()])
    password = PasswordField("Lösenord", [validators.DataRequired(), validators.EqualTo("confirm", message="Fel lösenord")])
    confirm = PasswordField("Bekräfta lösenord")


class Login(Form):
    remember_me = BooleanField("Kom ihåg mig")
