from flask import render_template, redirect, request, url_for, flash, jsonify, current_app
from . import auth
from flask_login import login_user, logout_user, login_required, current_user
from .forms import LoginForm, RegisterForm
from ..models import User
from ..email import send_email

@auth.route('/login',methods = ['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = form.get_user()
        if user is not None:
            if user.verify_password(form.password.data):
                login_user(user, form.remember_me.data)
                flash('You are now logged in!', "success")
                return redirect(request.args.get('next') or url_for("main.dashboard"))
            else:               
                return render_template('auth/login.html',form=form)
        else:
            flash('Username not found',"danger")
            return render_template('auth/login.html',form=form)
    return render_template('auth/login.html',form=form)


@auth.route('/register', methods = ['GET','POST'])
def register():
    form = RegisterForm(request.form)
    
    if request.method == 'POST':
        if request.headers.get('request-type') == 'ev':
            email = request.form['email']
            if email is not None:
                if User.objects(email=email).first():
                    return jsonify(status="email already registered!",code="failed" )
                return jsonify(status="this email is not registered",code="success")
        else:
            if form.validate():
                user = User(email=form.email.data,username=form.username.data)
                user.password = form.password.data
                user.save()
                flash("You are now registered!", "success")
                token = user.generate_confirmToken()
                send_email(user.email, 'Confirm Your Account','auth/email/confirmation',user=user,token=token)
                flash('Please check your email to confirm the account.',"danger")
                return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are now logged out','success')
    return redirect(url_for('main.index'))

@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash('You are CONFIRMED!',"success")
        return redirect(url_for('main.index'))
    else:       
        return redirect(url_for('auth.unconfirmed'))

@auth.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.ping()
        if not current_user.confirmed \
        and request.endpoint != 'auth' \
        and request.blueprint != 'auth' \
        and request.endpoint != 'static':
            return redirect(url_for('auth.unconfirmed'))

@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous() or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template("auth/unconfirmed.html",current_user=current_user)

@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmToken()
    send_email(current_user.email, 'Confirm Your Account','auth/email/confirmation',user=current_user,token=token)
    flash('The confirmation link does not work',"danger")
    flash('A new confirmation email has been sent to you by email.',"success")
    return redirect(url_for('main.index'))
