from app import app, db
from flask import render_template, redirect, url_for, flash, request
from app.forms import SignUpForm, LoginForm, AddressForm
from app.models import User, Address
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
def index():
    addresses = db.session.execute(db.select(Address)).scalars().all()
    print(addresses)
    #user = db.session.execute(db.select(User).order_by(db.desc(User.date_created))).scalars().all()
    # posts = db.session.execute(db.select(User).order_by(db.desc(User.date_created))).scalars().all()
    return render_template('index.html', addresses=addresses)
    
    #return render_template('index.html', posts=posts)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = SignUpForm()
    if  request.method=="POST":
        print('made here')
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        password = form.password.data
        phone= form.phone.data
        address = form.address.data
        
        print(first_name, last_name, phone, address)
        new_user = User(first_name=first_name, last_name=last_name, username=username, password=password, phone=phone, address=address)
        check_user = User.query.filter_by(username=username).first()
        if check_user is not None:
            flash('user name already in use')
            return render_template('register.html', form=form)

        db.session.add(new_user)
        db.session.commit()
        # Redirect back to the home page
        return redirect(url_for('index'))
    
    return render_template('register.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember_me = form.remember_me.data
        #login_user(user)

        #query user table for usrname
        user= db.session.execute(db.select(User).where(User.username==username)).scalar()

        if user is not None and user.check_password(password):
            login_user(user)  ###  PROBLEMATIC- old: login_user(user,remember=remember_me)
            flash(f'{user.username} has logged in')
            return redirect(url_for('index'))
        else:
            flash('Wrong usrname and/or pass')
            return redirect(url_for('login'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('You are logged out')
    return redirect(url_for('index'))

@app.route('/add-address', methods=["GET", "POST"])
@login_required
def add_address():
    form = AddressForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        phone = form.phone.data
        address = form.address.data

        # Create instance of Address
        new_address = Address(first_name=first_name, last_name=last_name, phone=phone, address=address, user_id=current_user.id)

        # upload to db
        db.session.add(new_address)
        db.session.commit()

        flash(f"{new_address.address} has been added")
        return redirect(url_for('index'))
    return render_template('add-address.html', form=form)



