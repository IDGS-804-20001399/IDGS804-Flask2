from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField
from wtforms import validators

from wtforms.fields import EmailField

def mi_validacion(form, field):
    if len(field.data) == 0:
        raise validators.ValidationError("El campo no tiene datos")

class UserForm(Form):
    matricula = StringField('Matricula',
    [
        validators.DataRequired(message="El campo Matricula es requerido"),
        validators.length(min=5, max=10, message = "Ingresa min 5 max 10")
    ]
    )
    nombre = StringField('Nombre', [validators.DataRequired(message="El campo Nombre es requerido")])
    apaterno = StringField('Apaterno', [
        mi_validacion
    ])
    amaterno = StringField('Amaterno')
    email = EmailField('Correo')

class TraductorForm(Form):
    espanol = StringField('Español',
    [
        validators.DataRequired(message="El campo es requerido"),
    ])
    ingles = StringField('Inglés',
    [
        validators.DataRequired(message="El campo es requerido"),
    ])

class BuscarForm(Form):
    palabra = StringField('Palabra',
    [
        validators.DataRequired(message="El campo es requerido"),
    ])
    idioma =  RadioField('Idioma', choices=[(1,'ingles'),(0,'español')]) 