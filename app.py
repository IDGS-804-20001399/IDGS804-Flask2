from flask import Flask, render_template, request, redirect, url_for, make_response, flash
import forms
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'esta es una clave encriptada'
csrf=CSRFProtect()

@app.route("/formprueba")
def formprueba():
    return render_template("formprueba.html")


@app.route("/Alumnos", methods=['GET', 'POST'])
def alumnos():
    reg_alum = forms.UserForm(request.form)
    datos = list()
    if request.method == 'POST' and reg_alum.validate():
        datos.append(reg_alum.matricula.data)
        datos.append(reg_alum.nombre.data)
        print(reg_alum.matricula.data)
        print(reg_alum.nombre.data)
    return render_template("alumnos.html", form=reg_alum, datos = datos)

@app.route("/cookie", methods=['GET', 'POST'])
def cookie():
    reg_user = forms.LoginForm(request.form)
    response = make_response(render_template('cookies.html', form = reg_user))
    if request.method == 'POST' and reg_user.validate():
        user = reg_user.username.data
        password = reg_user.password.data
        datos = f'{user}@{password}'
        succes_message = f"Bienvenido {user}"
        response.set_cookie("datos_usuario", datos)
        flash(succes_message)
    return response

@app.route("/resistencias", methods=['GET', 'POST'])
def resistencias():
    form1 = forms.ResistenciasForm(request.form)
    if request.method == 'POST':
        resistencias = []
        if request.form.get('historial') == '1':
            f = open('resistencias.txt', 'r', encoding='utf8')
            historial = f.readlines();
            f.close()
            for row in historial:
                color1, color2, color3, colort = row.split(',')
                colort = colort.strip()
                banda1 = [x[0] for x in form1.banda1.choices if x[1] == color1][0]
                banda2 = [x[0] for x in form1.banda2.choices if x[1] == color2][0]
                banda3 = [x[0] for x in form1.banda3.choices if x[1] == color3][0]
                tolerancia = [x[0] for x in form1.tolerancia.choices if x[1] == colort][0]
                resultado = int(f'{banda1}{banda2}') * banda3
                minimo = resultado * (1 - tolerancia)
                maximo = resultado * (1 + tolerancia)
                resistencias.append(
                    {'color1': color1,
                    'color2': color2,
                    'color3': color3,
                    'colort': colort,
                    'valor': resultado,
                    'min': minimo,
                    'max': maximo
                    }
                )
            return render_template('resistencias.html', 
                                form = form1,
                                resistencias = resistencias)
        banda1 = form1.banda1.data
        banda2 = form1.banda2.data
        banda3 = form1.banda3.data
        tolerancia = form1.tolerancia.data
        color1 = [x[1] for x in form1.banda1.choices if x[0] == banda1][0]
        color2 = [x[1] for x in form1.banda2.choices if x[0] == banda2][0]
        color3 = [x[1] for x in form1.banda3.choices if x[0] == banda3][0]
        colort = [x[1] for x in form1.tolerancia.choices if x[0] == tolerancia][0]
        resultado = int(f'{banda1}{banda2}') * banda3
        minimo = resultado * (1 - tolerancia)
        maximo = resultado * (1 + tolerancia)
        f = open('resistencias.txt', 'a', encoding='utf8')
        f.write(f'{color1},{color2},{color3},{colort}\n')
        f.close()
        resistencias.append(
            {'color1': color1,
             'color2': color2,
             'color3': color3,
             'colort': colort,
             'valor': resultado,
             'min': minimo,
             'max': maximo
             }
        )
        return render_template('resistencias.html', 
                            form = form1,
                            resistencias = resistencias)
    return render_template('resistencias.html', 
                           form = form1)

@app.route("/traductor", methods=['GET', 'POST'])
def traductor():
    form = forms.TraductorForm(request.form)
    form1 = forms.BuscarForm(request.form)
    if request.method == 'POST' and form.validate():
        espanol = form.espanol.data.lower()
        ingles = form.ingles.data.lower()
        f = open("traductor.txt", "a")
        f.write(f"{espanol},{ingles}\n")
        f.close()
        return redirect(url_for('traductor'))
    elif request.method == 'POST' and form1.validate():
        idioma = int(form1.idioma.data)
        palabra = form1.palabra.data.lower()
        f = open("traductor.txt", "r")
        palabras = f.readlines()
        f.close()
        palabra_traducida = "La palabra no está registrada"
        for p in palabras:
            if palabra in p:
                palabra_traducida = p.split(',')[idioma]
                break
        return render_template("traductor.html", form=form, form1 = form1, traduccion = palabra_traducida)
    return render_template("traductor.html", form=form, form1 = form1)

@app.route("/cajasDinamicas", methods=['GET', 'POST'])
def cajasDinamicas():
    if request.method == 'POST':
        n = int(request.form.get("num"))
        return render_template("cajas-dinamicas.html", n = n)
    return render_template("cajas-dinamicas.html", n = 0)

@app.route("/res-cajas", methods=['POST'])
def resCajas():
    nums = {}
    list_nums = []
    sum = 0
    n = int(request.form.get("num"))
    for i in range(n):
        nu = int(request.form.get(f"{i}"))
        sum += nu
        list_nums.append(nu)
        if nu in nums:
            nums[nu] += 1
        else:
            nums[nu] = 1

    _max = max(nums)
    _min = min(nums)
    avg = sum / n
    repetidos = dict((k, v) for k, v in nums.items() if v > 1)
    return render_template("cajas-res.html", nums = list_nums, 
    _max = _max,
    _min = _min,
    avg = avg,
    repetidos = repetidos
    )


if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True, port=3000)
