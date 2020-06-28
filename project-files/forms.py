from wtforms import Form, StringField, TextAreaField, PasswordField, BooleanField, validators


class Register(Form):
    username = StringField("Användarnamn", [validators.DataRequired()])
    email = StringField("E-post", [validators.Email()])
    password = PasswordField("Lösenord", [validators.Length(min=10), validators.EqualTo("confirm", message="Fel lösenord")])
    confirm = PasswordField("Bekräfta lösenord")


class Login(Form):
    remember_me = BooleanField("Kom ihåg mig")


class ArticleForm(Form):
    title = StringField("Objekt som skall städas:", [validators.Length(min=1, max=200, message="Vänligen fyll i mer!")])
    body = TextAreaField("Innehåll:", [validators.Length(min=10, message="Vänligen fyll i mer!")])
