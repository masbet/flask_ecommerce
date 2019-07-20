from flask import Flask, render_template, redirect, url_for, request, flash
from app import app, db
from app.forms.forms import FormDaftar
from app.models.models import User
from app.controllers.admin import Admin


class User:

    def index(self):
        return render_template('index.html')

    def shop(self):
        data_produk = Produk.query.all()
        return render_template('shop.html', data_produk=data_produk, title='shop')

    def cart(self):
        return render_template('cart.html')

    def contact(self):
        return render_template('contact-us.html')

    def product_detail(self):
        return render_template('product-details.html')

    def daftar_user(self):
        # data_user = User.query.all()
        form = FormDaftar()
        if form.is_submitted():
            user = User(nama=form.nama_user.data, email=form.alamat_email.data, username=form.username.data,
                        password=form.password.data, confirm=form.confirm_password.data)
            user.save()
            flash(f'Terimakasih, Pendaftaran anda berhasil', 'success')
            return redirect('shop')
        return render_template('pendaftaran.html', form=form, title='daftar user')

    def login_user(self):

        return render_template('login.html')

    def checkout_product(self):
        return render_template('checkout.html')

    def blog(self):
        return render_template('blog.html')

    def blog_single(self):
        return render_template('blog-single.html')
