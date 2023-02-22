from flask import Flask, render_template, request
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
    if request.method == 'POST':
        datos.append(reg_alum.matricula.data)
        datos.append(reg_alum.nombre.data)
        print(reg_alum.matricula.data)
        print(reg_alum.nombre.data)
    return render_template("alumnos.html", form=reg_alum, datos = datos)

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
