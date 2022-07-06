from crypt import methods
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key="123456"
@app.route('/')
def form_page():
    return render_template('form.html')


@app.route('/result', methods=['POST'])
def display_info():
    session['first_name'] = request.form.get("first_name")
    session['last_name'] = request.form.get("last_name")
    session['email'] = request.form.get("email")
    if request.form.get("flexRadioDefault") == 'add_to_letter':
        session['newsletter'] = "Added to newsletter"
    else:
        session['newsletter'] = "Not added to newsletter"
    session['address'] = request.form.get('address_line')
    session['city'] = request.form.get('city')
    session['state'] = request.form.get('state')
    session['zip_code'] = request.form.get('zip_code')
    return render_template('display_info.html', first_name=session['first_name'], last_name=session['last_name'], email=session['email'], newsletter=session['newsletter'], address=session['address'], city=session['city'], state=session['state'], zip_code=str(session['zip_code']))

if __name__ == '__main__':
    app.run(debug=True)