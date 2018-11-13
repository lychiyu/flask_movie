from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@127.0.0.1:3306/flask_movie'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class User(db.Model):
    """用户"""
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    mobile = db.Column(db.String(11), unique=True)
    info = db.Column(db.Text)
    face = db.Column(db.String(255), unique=True)
    uuid = db.Column(db.String(255), unique=True)
    created = db.Column(db.DateTime, index=True, default=datetime.now)
    user_logs = db.relationship('UserLog', backref='user')  # 处理关系关联
    comments = db.relationship('Comment', backref='user')
    collections = db.relationship('Collection', backref='user')

    def __repr__(self):
        return self.name


class UserLog(db.Model):
    """用户登录日志"""
    __tablename__ = 'user_log'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ip = db.Column(db.String(100))
    created = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return str(self.id)


class Tag(db.Model):
    """电影标签"""
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    created = db.Column(db.DateTime, index=True, default=datetime.now)
    movie = db.relationship('Movie', backref='tag')

    def __repr__(self):
        return self.name


class Movie(db.Model):
    """电影"""
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    url = db.Column(db.String(255), unique=True)
    info = db.Column(db.Text)
    logo = db.Column(db.String(255), unique=True)
    star_num = db.Column(db.SmallInteger)
    play_num = db.Column(db.BigInteger)
    comment_num = db.Column(db.BigInteger)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
    area = db.Column(db.String(100))
    release_time = db.Column(db.Date)
    length = db.Column(db.String(100))
    created = db.Column(db.DateTime, index=True, default=datetime.now)
    comments = db.relationship('Comment', backref='movie')
    collections = db.relationship('Collection', backref='movie')

    def __repr__(self):
        return self.title


class Preview(db.Model):
    """电影预告"""
    __tablename__ = 'preview'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    logo = db.Column(db.String(255), unique=True)
    created = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return self.title


class Comment(db.Model):
    """评论"""
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    created = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return str(self.id)


class Collection(db.Model):
    """用户收藏"""
    __tablename__ = 'collection'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    created = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return str(self.id)


class Auth(db.Model):
    """权限"""
    __tablename__ = 'auth'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    url = db.Column(db.String(100), unique=True)
    created = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return self.name


class Role(db.Model):
    """角色"""
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    auths = db.Column(db.String(600))
    created = db.Column(db.DateTime, index=True, default=datetime.now)
    admins = db.relationship('Admin', backref='role')

    def __repr__(self):
        return self.name


class Admin(db.Model):
    """管理员"""
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    is_super = db.Column(db.SmallInteger)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    created = db.Column(db.DateTime, index=True, default=datetime.now)
    admin_logs = db.relationship('AdminLog', backref='admin')
    admin_op_logs = db.relationship('AdminOpLog', backref='admin')

    def __repr__(self):
        return self.name


class AdminLog(db.Model):
    """管理员登录日志"""
    __tablename__ = 'admin_log'
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    ip = db.Column(db.String(100))
    created = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return str(self.id)


class AdminOpLog(db.Model):
    """管理员操作日志"""
    __tablename__ = 'admin_op_log'
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    ip = db.Column(db.String(100))
    op_detail = db.Column(db.String(600))  # 操作详情
    created = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return str(self.id)


if __name__ == '__main__':
    db.create_all()
