from flask import (
    Blueprint,
    flash,
    redirect,
    request,
    url_for,
    render_template)

from siapp.blueprints.signup.forms import SignupForm

signup = Blueprint('signup', __name__, template_folder='templates')

@signup.route('/signup', methods=['GET', 'POST'])
def index():
    form = SignupForm()

    if form.validate_on_submit():
        # This prevents circular imports.
        from siapp.blueprints.signup.tasks import deliver_signup_email

        deliver_signup_email.delay(request.form.get('first'), 
                                    request.form.get('last'),
                                    request.form.get('email'))

        flash('Thanks, expect a response shortly.', 'success')
        return redirect(url_for('signup.index'))

    return render_template('signup/index.html', form=form)
