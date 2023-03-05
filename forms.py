from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField, PasswordField
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

class LoginForm(Form):
    username = StringField('usuario',
    [validators.DataRequired(message="El campo Usuario es requerido"),
    validators.length(min=5, max=10, message="Ingresa min 5 max 10")
    ]
    )
    password = PasswordField('Contraseña',
    [validators.DataRequired(message="El campo Contraseña es requerido"),
    validators.length(min=5, max=10, message="Ingresa min 5 max 10")
    ]
    )

class ResistenciasForm(Form):
    banda1 = SelectField('Banda 1', 
        choices=[('0', 'Negro'),
                 ('1', 'Café'), 
                 ('2', 'Rojo'),
                 ('3', 'Naranja'),
                 ('4', 'Amarillo'),
                 ('5', 'Verde'),
                 ('6', 'Azul'),
                 ('7', 'Violeta'),
                 ('8', 'Gris'),
                 ('9', 'Blanco'),
                 ])
    banda2 = SelectField('Banda 2', 
        choices=[('0', 'Negro'),
                 ('1', 'Café'), 
                 ('2', 'Rojo'),
                 ('3', 'Naranja'),
                 ('4', 'Amarillo'),
                 ('5', 'Verde'),
                 ('6', 'Azul'),
                 ('7', 'Violeta'),
                 ('8', 'Gris'),
                 ('9', 'Blanco'),
                 ])
    banda3 = SelectField('Banda 3', 
        choices=[(1, 'Negro'),
                 (10, 'Café'), 
                 (100, 'Rojo'),
                 (1000, 'Naranja'),
                 (10000, 'Amarillo'),
                 (100000, 'Verde'),
                 (1000000, 'Azul'),
                 (10000000, 'Violeta'),
                 (100000000, 'Gris'),
                 (1000000000, 'Blanco'),
                 ], coerce=int)
    tolerancia = RadioField('Tolerancia', 
        choices=[(0.05, 'Dorado'),
                 (0.10, 'Plata')], coerce=float)
                