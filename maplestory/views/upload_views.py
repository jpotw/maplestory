from flask import Blueprint, request, render_template, flash, redirect, session
from maplestory.models import Button


bp = Blueprint('upload', __name__, url_prefix='/')    

@bp.route('/', methods=['GET', 'POST'])
def upload_file():
    form = Button()
    if request.method == 'POST':
        num = session.get('num', 0)
        num += 1
        session['num'] = num  # Store the updated count in the session
        flash(f"{num}번째 강화 실패")
        return render_template('upload.html', form=form)
    return render_template('upload.html', form=form)