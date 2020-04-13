from passlib.hash import sha256_crypt
from flask import Flask, request, render_template, url_for, redirect, flash
from flask_login import (
    login_user, logout_user, current_user, LoginManager, login_required)
from forms import FormEnergia, FormUsers
from models import Valor, Users, db

app = Flask(__name__)
app.config.from_object('settings')
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)

with app.app_context():
    db.create_all()


@app.teardown_appcontext
def teardown_app(exception):
    db.session.commit()
    db.session.close()


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))


@login_manager.user_loader
def loader_user(id):
    try:
        return Users.query.filter_by(id=id).first()
    except:
        return None


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = FormUsers()
    if request.method == 'GET':
        if not current_user.is_authenticated:
            return render_template('login.html', form=form)
        else:
            return redirect(url_for('energia'))

    if request.method == 'POST':
        if form.validate_on_submit():
            form = FormUsers(request.form)
            username = form.username.data
            passwd = form.password.data

            user = Users.query.filter_by(username=username).first()

            if user:
                dbuser = user.username
                dbpass = user.password

                if username == dbuser and sha256_crypt.verify(passwd, dbpass):
                    login_user(user)
                    return redirect(url_for('energia'))
                else:
                    flash('Usuário ou senha inválida')
            else:
                flash('Usuário ou senha inválida')

        else:
            flash('Entre com o usuário e senha')

        return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('energia'))


@app.route('/', methods=['GET', 'POST', 'DELETE'])
@login_required
def energia():
    form = FormEnergia()
    if request.method == 'GET':
        energias = Valor.query.order_by(Valor.id.desc()).all()

        if request.args.get('confirm'):
            confirm = request.args.get('confirm')

            return render_template(
                'index.html', form=form, energias=energias, confirm=confirm)

        if request.args.get('delete'):
            delete = request.args.get('delete')
            leitura = Valor.query.filter_by(id=delete).first()
            db.session.delete(leitura)
            flash('Leitura apaga')

            return redirect(url_for('energia'))

        return render_template('index.html', form=form, energias=energias)

    if request.method == 'POST':
        if form.validate_on_submit():
            leitura = FormEnergia(request.form)
            energia = Valor.query.order_by(Valor.id.desc()).first()

            if energia:
                kwAntigo = int(energia.kwAtual)
                kwAtual = int(leitura.kwatual.data)
                kwValor = float(leitura.valorkwh.data)
                kwTotal = kwAtual - kwAntigo
                total = ('%.2f' % (kwTotal * kwValor))
                query = Valor(
                    kwAtual=kwAtual,
                    data=leitura.dataleitura.data,
                    kwValor=kwValor,
                    kwTotal=kwTotal,
                    totalPagar=total
                )

                db.session.add(query)
            else:
                kwAtual = int(leitura.kwatual.data)
                kwValor = float(leitura.valorkwh.data)
                total = ('%.2f' % (kwAtual * kwValor))
                query = Valor(
                    kwAtual=kwAtual,
                    data=leitura.dataleitura.data,
                    kwValor=kwValor,
                    kwTotal=kwAtual,
                    totalPagar=total
                )

                db.session.add(query)

            return redirect(url_for('energia'))
        else:
            energias = Valor.query.order_by(Valor.id.desc()).all()
            return render_template('index.html', form=form, energias=energias)
