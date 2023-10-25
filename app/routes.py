from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm 
from app.models import User
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hoth', methods=['GET', 'POST'])
def hoth():
    form = SignUpForm()
    if form.validate_on_submit():
        print('First Name: ',form.first_name.data)
        print('Last Name: ',form.last_name.data)
        print('Phone Number: ',form.phone.data)
        print('Address: ',form.address.data)
        
        first_name = form.first_name.data
        last_name = form.last_name.data
        phone= form.phone.data
        address = form.address.data
        
        print(first_name, last_name, phone, address)

        new_user = User(first_name=first_name, last_name=last_name, phone=phone, address=address)
        
        
        db.session.add(new_user)
        db.session.commit()
        # Redirect back to the home page
        return redirect(url_for('index'))
    
    return render_template('hoth.html', form=form)


