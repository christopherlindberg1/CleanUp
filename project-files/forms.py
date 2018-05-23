from wtforms import Form, StringField, TextAreaField, PasswordField, BooleanField, validators


class Register(Form):
    username = StringField("Användarnamn", [validatiors.Length(min=1, max=50)])
    email = StringField("E-post", [validators.Email(min=1, max=50)])
    password = PasswordField("Lösenord", [validators.DataRequired(min=10, max=50), validators.EqualTo("confirm", message="Fel lösenord")])
    confirm = PasswordField("Bekräfta lösenord")


class Login(Form):
    remember_me = BooleanField("Kom ihåg mig")
