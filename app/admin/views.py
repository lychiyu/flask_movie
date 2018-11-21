from app.admin import admin
from flask import render_template, redirect, url_for, session, request, flash
from app.admin.forms import LoginForm
from app.models import Admin
from functools import wraps


def admin_login_req(f):
    @wraps(f)
    def decorated_f(*args, **kwargs):
        if 'admin' not in session:
            return redirect(url_for('admin.login', next=request.url))
        return f(*args, **kwargs)

    return decorated_f


@admin.route("/")
@admin_login_req
def index():
    return render_template('admin/index.html')


@admin.route("/login/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        admin = Admin.query.filter_by(name=data['account']).first()
        if not admin.check_pwd(data['pwd']):
            flash('密码错误')
            return redirect(url_for('admin.login'))
        session['admin'] = data['account']
        return redirect(request.args.get('next') or url_for('admin.index'))
    return render_template('admin/login.html', form=form)


@admin.route("/logout/")
@admin_login_req
def logout():
    session.pop('admin', None)
    return redirect(url_for('admin.login'))


@admin.route("/pwd/")
@admin_login_req
def pwd():
    return render_template('admin/pwd.html')


@admin.route("/tag/add")
@admin_login_req
def tag_add():
    return render_template('admin/tag_add.html')


@admin.route("/tag/list")
@admin_login_req
def tag_list():
    return render_template('admin/tag_list.html')


@admin.route("/movie/add")
@admin_login_req
def movie_add():
    return render_template('admin/movie_add.html')


@admin.route("/movie/list")
def movie_list():
    return render_template('admin/movie_list.html')


@admin.route("/preview/add")
@admin_login_req
def preview_add():
    return render_template('admin/preview_add.html')


@admin.route("/preview/list")
def preview_list():
    return render_template('admin/preview_list.html')


@admin.route("/user/view")
@admin_login_req
def user_view():
    return render_template('admin/user_view.html')


@admin.route("/user/list")
@admin_login_req
def user_list():
    return render_template('admin/user_list.html')


@admin.route("/comment/list")
@admin_login_req
def comment_list():
    return render_template('admin/comment_list.html')


@admin.route("/collection/list")
@admin_login_req
def collection_list():
    return render_template('admin/collection_list.html')


@admin.route("/oplog/list")
@admin_login_req
def oplog_list():
    return render_template('admin/oplog_list.html')


@admin.route("/adminlog/list")
@admin_login_req
def adminlog_list():
    return render_template('admin/adminlog_list.html')


@admin.route("/userlog/list")
@admin_login_req
def userlog_list():
    return render_template('admin/userlog_list.html')


@admin.route("/auth/add")
@admin_login_req
def auth_add():
    return render_template('admin/auth_add.html')


@admin.route("/auth/list")
@admin_login_req
def auth_list():
    return render_template('admin/auth_list.html')


@admin.route("/role/add")
@admin_login_req
def role_add():
    return render_template('admin/role_add.html')


@admin.route("/role/list")
def role_list():
    return render_template('admin/role_list.html')


@admin.route("/admin/add")
@admin_login_req
def admin_add():
    return render_template('admin/admin_add.html')


@admin.route("/admin/list")
@admin_login_req
def admin_list():
    return render_template('admin/admin_list.html')
