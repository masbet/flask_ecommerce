from app import db
from datetime import datetime


class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nama_supplier = db.Column(db.String(50), nullable=False)
    alamat = db.Column(db.String(150), nullable=False)
    telpon = db.Column(db.String(20), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def getAll(self):
        return Supplier.query.all()

    def getOne(self, id):
        return Supplier.query.filter_by(id=id).first()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return '<id:{}>'.format(self.id)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nama_user = db.Column(db.String(50), nullable=False)
    alamat_email = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    Confirm_password = db.Column(db.String(50), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        return db.session.commit()


class Produk(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    nama_produk = db.Column(db.String(50), nullable=False)
    harga = db.Column(db.Integer, nullable=False)
    stok = db.Column(db.Integer, nullable=False)
    image_produk = db.Column(db.String(50), nullable=False)
    deskripsi = db.Column(db.String(200), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def getAll(self):
        return Produk.query.all()

    def getOne(self, id):
        return Produk.query.filter_by(id=id).first()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return '<id:{}>'.format(self.id)


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    judul = db.Column(db.String(200), nullable=False)
    artikel = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(20), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def getAll(self):
        return Blog.query.all()

    def getOne(self, id):
        return Blog.query.filter_by(id=id).first()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return '<id:{}>'.format(self.id)
