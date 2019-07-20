from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField, SelectField, DateField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, EqualTo


class FormSupplier(FlaskForm):
    message = 'data tidak boleh kosong'
    nama_supplier = StringField('Nama Supplier', validators=[
                                DataRequired(message=message)])
    alamat = StringField('Alamat', validators=[DataRequired(message=message)])
    telpon = StringField('Telpon', validators=[DataRequired(message=message)])
    simpan = SubmitField('Simpan')


class FormDaftar(FlaskForm):
    message = 'data tidak boleh kosong'
    nama_user = StringField('Nama User', validators=[
                            DataRequired(message=message)])
    alamat_email = StringField('Alamat Email', validators=[
                               DataRequired(message=message)])
    username = StringField('Username', validators=[
                           DataRequired(message=message)])
    password = PasswordField('Password', validators=[
                             DataRequired(message=message)])
    confirm_password = PasswordField('Confirmasi Password', validators=[
                                     DataRequired(message=message), EqualTo('password')])
    daftar = SubmitField('Daftar')


class FormProduk(FlaskForm):
    message = 'data tidak boleh kosong'
    nama_produk = StringField('Nama Produk', validators=[
                              DataRequired(message=message)])
    harga = IntegerField('Harga', validators=[DataRequired(message=message)])
    stok = IntegerField('Stok', validators=[DataRequired(message=message)])
    image = StringField('Image', validators=[DataRequired(message=message)])
    deskripsi = StringField('Deskripsi', validators=[
                            DataRequired(message=message)])
    tambah = SubmitField('Tambah')


class FormBlog(FlaskForm):
    message = 'data tidak boleh kosong'
    judul_blog = StringField('Judul', validators=[
                             DataRequired(message=message)])
    artikel = TextAreaField('Artikel', validators=[
        DataRequired(message=message)])
    image = StringField('Image', validators=[DataRequired(message=message)])
    tambah = SubmitField('Tambah')


class FormLoginAdmin(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    login = SubmitField('Login')
