from app import app
from app.controllers.konsumen import User
from app.controllers.admin import Admin


@app.route('/')
def index():
    return User().index()


@app.route('/shop')
def shop():
    return User().shop()


@app.route('/cart')
def cart():
    return User().cart()


@app.route('/contact')
def contact():
    return User().contact()


@app.route('/detail-product')
def detail_product():
    return User().product_detail()


@app.route('/daftar-user', methods=['POST', 'GET'])
def daftar_user():
    return User().daftar_user()


@app.route('/login-user')
def login_user():
    return User().login_user()


@app.route('/checkout')
def checkout_product():
    return User().checkout_product()


@app.route('/input-blog')
def input_blog():
    return Admin().inputBlog()


@app.route('/blog')
def blog():
    return User().blog()


@app.route('/single-blog')
def blog_single():
    return User().blog_single()


@app.route('/data-konsumen', methods=['POST', 'GET'])
def data_konsumen():
    return Admin().dataKonsumen()

    # admin


@app.route('/admin')
def admin():
    return Admin().admin()


@app.route('/login-admin', methods=['GET', 'POST'])
def loginAdmin():
    return Admin().loginAdmin()


@app.route('/data-supplier', methods=['POST', 'GET'])
def dataSupplier():
    return Admin().dataSupplier()


@app.route('/input-supplier', methods=['POST', 'GET'])
def inputSupplier():
    return Admin().inputSupplier()


@app.route('/edit-supplier/<id>', methods=['POST', 'GET'])
def editSupplier(id):
    return Admin().editSupplier(id)


@app.route('/delete-supplier/<id>')
def deleteSupplier(id):
    return Admin().deleteSupplier(id)


@app.route('/data-konsumen', methods=['POST', 'GET'])
def dataKonsumen():
    return Admin().dataKonsumen()


@app.route('/data-pesanan', methods=['POST', 'GET'])
def dataPesanan():
    return Admin().dataPesanan()


@app.route('/input-produk', methods=['POST', 'GET'])
def inputProduk():
    return Admin().inputProduk()


@app.route('/edit-produk/<id>', methods=['POST', 'GET'])
def editProduk(id):
    return Admin().editProduk(id)


@app.route('/hapus-produk/<id>', methods=['POST', 'GET'])
def deleteProduk(id):
    return Admin().deleteProduk(id)


@app.route('/barang-masuk', methods=['POST', 'GET'])
def barangMasuk():
    return Admin().barangMasuk()


@app.route('/barang-keluar')
def barangKeluar():
    return Admin().barangKeluar()


@app.route('/laporan-penjualan')
def laporanPenjualan():
    return Admin().laporanPenjualan()


@app.route('/laporan-pembelian')
def laporanPembelian():
    return Admin().laporanPembelian()


@app.route('/data-blog')
def dataBlog():
    return Admin().dataBlog()
