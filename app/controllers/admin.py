from flask import Flask, render_template, redirect, url_for
from app import app, db
from app.forms.forms import FormSupplier, FormProduk, FormBlog, FormLoginAdmin
from app.models.models import Supplier, User, Produk, Blog


class Admin:

    # admin

    def admin(self):
        return render_template('dashboard.html')

    def loginAdmin(self):
        form = FormLoginAdmin()
        if form.is_submitted():
            if form.username.data == 'admin' and form.password.data == 'admin':
                return redirect(url_for('admin'))

            else:
                flash('Username dan password salah', 'danger')
        return render_template('login-adm.html', form=form)

    def dataSupplier(self):
        data_supplier = Supplier.query.all()
        # forms = FormSupplier()
        # if forms.is_submitted():
        #     supplier = Supplier(nama_supplier=forms.nama_supplier.data,
        #     alamat=forms.alamat.data,
        #     telpon=forms.telpon.data)
        #     supplier.save()
        #     return redirect('data_supplier')
        return render_template('data-supplier.html', title='DataSupplier', data_supplier=data_supplier)

    def dataKonsumen(self):
        data_konsumen = User.query.all()
        return render_template('data-konsumen.html', data_konsumen=data_konsumen)

    def dataPesanan(self):
        return render_template('data-pesanan.html')

    def barangMasuk(self):
        data_produk = Produk.query.all()
        return render_template('barang-masuk.html', title='DataProduk', data_produk=data_produk)

    def inputProduk(self):
        data_produk = Produk.query.all()
        forms = FormProduk()
        if forms.is_submitted():
            produk = Produk(nama_produk=forms.nama_produk.data, harga=forms.harga.data,
                            stok=forms.stok.data, image_produk=forms.image.data, deskripsi=forms.deskripsi.data)
            produk.save()
            return redirect(url_for('barangMasuk'))
        return render_template('input-produk.html', title='InputProduk', data_produk=data_produk, forms=forms)

    def editProduk(self, id):
        forms = FormProduk()
        data_produk = Produk().query.filter_by(id=id).first()
        if forms.is_submitted():
            data_produk.nama_produk = forms.nama_produk.data
            data_produk.harga = forms.harga.data
            data_produk.stok = forms.stok.data
            data_produk.image = forms.image.data
            data_produk.deskripsi = forms.deskripsi.data
            db.session.commit()
            return redirect(url_for('barangMasuk'))

        return render_template('edit-produk.html', title='edit produk', forms=forms, data_produk=data_produk)

    def deleteProduk(self, id):
        data_produk = Produk().query.filter_by(id=id).first()
        data_produk.delete()

        return redirect(url_for('barangMasuk'))

    def barangKeluar(self):
        return render_template('barang-keluar.html')

    def laporanPenjualan(self):
        return render_template('laporan-penjualan.html')

    def laporanPembelian(self):
        return render_template('laporan-pembelian.html')

    def inputSupplier(self):
        data_supplier = Supplier.query.all()
        forms = FormSupplier()
        if forms.is_submitted():
            supplier = Supplier(nama_supplier=forms.nama_supplier.data,
                                alamat=forms.alamat.data,
                                telpon=forms.telpon.data)
            supplier.save()
            return redirect(url_for('dataSupplier'))

        return render_template('input-supplier.html', title='Tambah supplier', forms=forms, data_supplier=data_supplier)

    def editSupplier(self, id):
        forms = FormSupplier()
        data_supplier = Supplier().query.filter_by(id=id).first()
        if forms.is_submitted():
            data_supplier.nama_supplier = forms.nama_supplier.data
            data_supplier.alamat = forms.alamat.data
            data_supplier.telpon = forms.telpon.data
            db.session.commit()
            return redirect(url_for('dataSupplier'))
        return render_template('edit-supplier.html', title='Edit Supplier', forms=forms, data_supplier=data_supplier)

    def deleteSupplier(self, id):
        data_supplier = Supplier().query.filter_by(id=id).first()
        data_supplier.delete()

        return redirect(url_for('dataSupplier'))

    def inputBlog(self):
        data_blog = Blog.query.all()
        forms = FormBlog()
        if forms.is_submitted():
            blog = Blog(judul=forms.judul_blog.data,
                        artikel=forms.artikel.data,
                        image=forms.image.data)
            blog.save()
            return redirect(url_for('dataBlog'))
        return render_template('input-blog.html', forms=forms, data_blog=data_blog, title='input Blog')

    def dataBlog(self):
        return render_template('data-blog.html')
