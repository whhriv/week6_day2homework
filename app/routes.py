from app import app
from flask import render_template, redirect, url_for
from app.forms import SignUpForm
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hoth', methods=['GET', 'POST'])
def hoth():
    form = SignUpForm()
    if form.validate_on_submit():
        print(form.first_name.data)
        print(form.last_name.data)
        print(form.phone.data)
        print(form.address.data)
        #get data from each of the fields
        first_name = form.first_name.data
        last_name = form.last_name.data
        phone= form.phone.data
        address = form.address.data
        
        print(first_name, last_name, phone, address)


        # Redirect back to the home page
        return redirect(url_for('index'))
    
    return render_template('hoth.html', form=form)


