from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, validators


class FormEnergia(FlaskForm):
    kwatual = IntegerField(
        'Kw Atual',
        [validators.DataRequired("Campo numérico obrigatório")],
        render_kw={"placeholder": "Kw Atual"}
    )
    dataleitura = StringField(
        'Data de Leitura',
        [validators.DataRequired("Data obrigatória")],
        render_kw={"placeholder": "Data de Leitura"}
    )
    valorkwh = StringField(
        'Valor do kwh',
        [validators.DataRequired("Valor do kWh obrigatório")],
        render_kw={"placeholder": "Valor do Kwh"}
    )


class FormUsers(FlaskForm):
    username = StringField(
        'Usuário',
        [validators.DataRequired()],
        render_kw={"placeholder": "Usuário"}
    )
    password = PasswordField(
        'Senha',
        [validators.DataRequired()],
        render_kw={"placeholder": "Senha"}
    )
