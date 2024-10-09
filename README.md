# YESTORE
**Situs Deployment:** http://alyssa-layla-yestore.pbp.cs.ui.ac.id/

Nama    : Alyssa Layla Sasti

Kelas   : PBP D

NPM     : 2306152052

<details>
<summary> <b> Tugas 6: JavaScript dan AJAX </b> </summary>

# Pertanyaan

## Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!

## Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?

##  Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?

## Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

</details>

<details>
<summary> <b> Tugas 5: Desain Web menggunakan HTML, CSS, dan Framework CSS </b> </summary>

# Pertanyaan

##  Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
1. Inline Style: Ini adalah prioritas tertinggi. Style yang didefinisikan langsung di baris tersebut. Contoh:
```css
    <p style="color : red;">
```
Notes: Semua teks yang ada di dalam div tersebut akan berwarna merah

2. ID Selector: Style dengan ID selector juga memiliki prioritas tinggi (walauapun tidak setinggi inline style). Contoh:
```css
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            #main { color: blue; }      
        </style>
    </head>
    <body>
        <p id="main">Hello World!</p>
    </body>
    </html>
```
3. Class, Attribute, dan Pseudo-class Selector. Contoh:
```css
    <style>
        .menu { color: green; }            /* Class selector */
        [type="text"] { color: blue; }     /* Attribute selector */
        a:hover { color: red; }            /* Pseudo-class selector*/
    </style>

    <p class="menu">Paragraf pakai kelas 'menu'.</p>
    <input type="text" value="Text input field">
    <a href="#">Hover over this link</a>
```

4. Element Selector (Tag Selector): Pakai elemen seperti h1, p, div, dll. Contoh: 
```css
    <style>
        p { color: red; }  
    </style>

    <p>Halo semuanya.</p>
```
5. Universal Selector *: Memiliki prioritas paling rendah
```css
    <style>
    * { margin: 0; }  /* Universal selector */
    </style>

    <div>
    <p>Ini bagian paragraf.</p>
    <h1>Ini heading.</h1>
    </div>  
```
Referensi: https://revou.co/panduan-teknis/css-selectors

## Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design dalam pengembangan web menjadi hal yang penting dan krusial. Hal ini dikarenakan, dari sisi pengguna, dalam menggunakan website akan digunakan dalam berbagai ukuran layar. Tidak selalu full page. Dan pengguna tentu mengharapkan kemudahan apabila website dibuka dengan berbagai ukuran di mobile dan dekstop harus dapat berfungsi dan menunjang kebutuhan pengguna dengan baik. Jika tidak, maka pengguna akan kesulitan dan merasa tidak efektif dalam menggunakan website tersebut

Contoh aplikasi yang sudah responsive: Website Netflix, App Store versi website
Contoh aplikasi yang belum responsive: SIAKNG


## Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
- Margin: Ruang di luar elemen border. Margin mengatur jarak elemen dari elemen-elemen di luar batasnya. Margin ini transparan, tidak mempengaruhi konten. Contoh: `margin: 40px;`
- Border: Garis tepi yang mengelilingi elemen, berada di antara margin dan padding. Biasanya digunakan untuk batas visual elemen. Contoh: `border: 5px solid red`
- Padding: Padding adalah batas yang paling dekat dengan konten. Ia dalah ruang di dalam elemen, antara konten elemen dengan tepi elemen (border). Padding menambah jarak di dalam elemen sehingga tidak langsung bersinggungan dengan border. Padding ini transparan, hanya menggeser saja. Contoh: `padding: 20px`
    
## Jelaskan konsep flex box dan grid layout beserta kegunaannya!
- Flexbox: Digunakan sebagai container dan items untuk mengatur elemen secara horizontal dan vertikal dalam satu arah utama. Memberikan fleksibilitas tinggi dalam menyusun elemen, terutama jika dinamis.
- Grid Layout: Bentuknya dua dimensi dan lebih kompleks dari flexbox. Baris dan kolom yang diatur tidak bergantung pada satu arah. Memungkinkan design yang lebih tersttruktur dan presisis dengan  penempatan gridnya

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
- Pertama saya mengimplementasikan fungsi hapus dan edit dengan menambahkan di `views.py`
```python
    def edit_product(request, id):
        product = Product.objects.get(pk = id)
        form = ProductEntryForm(request.POST or None, instance=product)

        if form.is_valid() and request.method == "POST":
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))

        context = {'form': form}
        return render(request, "edit_product.html", context)

    def delete_product(request, id):
        product = Product.objects.get(pk = id)
        product.delete()
        return HttpResponseRedirect(reverse('main:show_main'))
```

- Import fungsi dan menambahkan path ke `urls.py`
    ```python
    from django.urls import path
    from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_product, delete_product

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
        path('create-product-entry', create_product_entry, name='create_product_entry'),
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
        path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
        path('register/', register, name='register'),
        path('login/', login_user, name='login'),
        path('logout/', logout_user, name='logout'),
        path('edit-product/<uuid:id>', edit_product, name='edit_product'),
        path('delete/<uuid:id>', delete_product, name='delete_product'),
    ]
    ```
- Ke `main.html` dan menambah fungsionalitas `main:edit_product` dan `main:delete_product` untuk hyperlink di buttonnya

- Membuat folder static css dan image. css untuk membuat global.css dengan isi sebagai berikut:
```css
.form-style form input, 
.form-style form textarea, 
.form-style form select {
    width: 100%;
    padding: 0.5rem;
    border: 2px solid #bcbcbc; 
    border-radius: 0.375rem; 
    font-size: 1rem; 
    transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.form-style form input:focus, 
.form-style form textarea:focus, 
.form-style form select:focus {
    outline: none; 
    border-color: red; 
    box-shadow: 0 0  3px red; 
}

@keyframes shine {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
}

.animate-shine {
    background: linear-gradient(120deg, rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.1) 50%, rgba(255, 255, 255, 0.3));
    background-size: 200% 100%;
    animation: shine 3s infinite;
}

```
- Tambahkkan tailwind di `base.html`
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
  </head>
  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```
- Membuat file create_product.html, edit_product.html, card_product.html dan card_info.html dan kustomisasi dengan design yang diinginkan
</details>

<details>
<summary> <b> Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django </b> </summary>

# Pertanyaan

## Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`
`HttpResponseRedirect()` dan `redirect()` keduanya sama akan melakukan *redirect* mengalihkan ke URL yang diinginkan. Namun perbedaannya adalah
- Untuk `HttpResponseRedirect()` diimport dari `django.http` sedangkan `redirect()` diimport dari `django.shortcuts`. Sehingga dapat dikatakan bahwa `redirect()` merupakan versi shortcut dari `HttpResponseRedirect()`
- `redirect()` lebih fleksibel dibanding `HttpResponseRedirect()` karena `redirect()` bisa handle lebih beragam input, yaitu model instance, view names, atau URL. Sedangkan jika di `HttpResponseRedirect()` hanya bisa URL saja

## Jelaskan cara kerja penghubungan model `Product` dan `User!`!
Penghubungan model `Product` dan `User` dilakukan dengan menambahkan `ForeignKey` di model `Product` dengan meng-import `User` dari django
```python
from django.db import models
from django.contrib.auth.models import User
import uuid 

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```
Pada kode saya, `Product` dan `User` terhubung melalui `user`. Sehingga saat kita membuat product, akan otomatis menempel dengan user yang sedang login. Sehingga peoduct yang dibuat berkepemilikan oleh kita. Ini mengakibatkan apabila berbeda user yang login, maka productnya juga beda

## Apa perbedaan antara *authentication* dan *authorization*, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut
- Authentication adalah proses verifikasi identitas pengguna. Kemudian saat pengguna login, Django akan memeriksa data-data yang diinput dan memvalidasi apakah sesuai dengan yang ada di database. Django juga menyimpan informasi sesi pengguna untuk setiap dilakukan login
- Authorization adalah proses memberikan izin pengguna untuk mengakses fitur. Pada Django, digunakan `login_required` untuk melakukan authorization. Pada saat pengguna login, Django akan melihat apakah authenticationnya valid, setelah itu authorization menyesuaikan `login_required` diperlukan untuk mendapat hak akses apa saja. Baru setelah itu pengguna dapat mengakses page sesuai dengan data yang diberikan 
- Django mengimplementasikan kedua konsep ini dengan:
```python
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
```
Baris pertama ditujukan untuk penerapan authentication dan sebagai contoh diimplementasikan untuk login. Kemudian baris kedua ditujukan untuk penerapan authorization. Pada fungsi yang ingin dilakukan Authorization harus diberikan permission check seperti ini:
```python
@login_required(login_url='/login')
def show_main(request):
    #isi dari fungsinya
```

## Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
- Django mengingat pengguna yang telah login dengan *session Framework*. Setelah pengguna login, datanya disimpan di session yang terakit dengan cookie di browser. Session ID disimpan di cookie pengguna dan setiap pengguna melakukan permintaan baru, session ID digunakan untuk mengidentifikasi pengguna yang sedang login.
- Kegunaan lain dari cookies adalah cookies dapat digunakan untuk menyimpan data sementara di browser pengguna (seperti last login). Sebagai gambaran untuk memudahkan, cookies adalah data kecil yang disimpan di browser pengguna dengan disesuaikan per-penggunannya. Alias tiap pengguna memiliki cookies yang berbeda.
- Tidak semua cookies aman, terutama apabila menyimpan data-data kredensial seperti password. Maka dari itu, untuk keamanan, Django memiliki beberapa proteksi, salah satunya yaitu dengan `SESSION_COOKIE_SECURE`

## Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial)

### Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
- Membuat Fungsi dan Form Registrasi
    1. Buka CMD dan aktifkan virtual environment dengan perintah `env\Scripts\activate`
    2. Membuka file `views.py`, kemudian saya menambahkan import `UserCreationForm` dan `messages` untuk menambah fitur pengisian formulir di website. Import yang saya lakukan seperti ini:
        ```python
        from django.contrib.auth.forms import UserCreationForm
        from django.contrib import messages
        ```
    3. Saya menambahkan fungsi `register`dengan parameter `request` ke file yang sama seperti step sebelumnya, yaitu file `views.py`. Di dalam fungsi ini saya membuat instance form kosong menggunakan `UserCreationForm` dan menggunakan `request.POST`untuk mengurim data pengguna ke dalam instance baru dari `UserCreationForm`. Kemudian saya mengecek apakah form valid dan save ke database kemudian redirect ke halaman login kembali apabila sudah di save ke database.
        ```python
        def register(request):
            form = UserCreationForm()

            if request.method == "POST":
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Your account has been successfully created!')
                    return redirect('main:login')
            context = {'form':form}
            return render(request, 'register.html', context)
        ```
    4. Pergi `ke main/templates` kemudian membuat berkas `.html` baru dengan nama `register.html`
        ```html
        {% extends 'base.html' %}

        {%` block meta %}
        <title>Register</title>
        {% endblock meta %}

        {% block content %}

        <div class="login">
        <h1>Register</h1>

        <form method="POST">
            {% csrf_token %}
            <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td><input type="submit" name="submit" value="Daftar" /></td>
            </tr>
            </table>
        </form>

        {% if messages %}
        <ul>
            {% for message in messages %}
            <li>{{ message }}</li>
            {% endfor %}
        </ul>
        {% endif %}
        </div>

        {% endblock content %}
        ```
        Notes: file ini digunakan untuk menampilkan halaman register. `{{ form.as_table }}` digunakan untuk men-display formnya dengan bentuk tabel
    5. Saya membuka `urls.py` pada subdirektori `main` untuk mengimpor fungsi yang baru tadi dibuat di `views.py` kemudian menambahkan path ke `urlpatters`
        ```python
        from main.views import register

        ...

         urlpatterns = [
            ...
            path('register/', register, name='register'),
        ]
        ```

- Membuat Fungsi Login
    1. Saya membuka `views.py` kemudian tambahkan import `authenticate`, `login`, dan `AutenticationForm` dan menambahkan fungsi `login_user` ke `views.py`. Fungsi inidigunakan untuk mengautentikasi pengguna yang ingin login, kemudian jika valid, fungsi akan membuat *session* untuk pengguna yang sudah berhasil login.
        ```python
        from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
        from django.contrib.auth import authenticate, login

        ...

        def login_user(request):
            if request.method == 'POST':
                form = AuthenticationForm(data=request.POST)

                if form.is_valid():
                        user = form.get_user()
                        login(request, user)
                        return redirect('main:show_main')

            else:
                form = AuthenticationForm(request)
            context = {'form': form}
            return render(request, 'login.html', context)
        ```
    2. Buat berkas `.html` di direktori `main/templates` dengan nama `login.html`. Saya mengisi dengan kode berikut:
        ```html
        {% extends 'base.html' %}

        {% block meta %}
        <title>Login</title>
        {% endblock meta %}

        {% block content %}
        <div class="login">
        <h1>Login</h1>

        <form method="POST" action="">
            {% csrf_token %}
            <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login" /></td>
            </tr>
            </table>
        </form>

        {% if messages %}
        <ul>
            {% for message in messages %}
            <li>{{ message }}</li>
            {% endfor %}
        </ul>
        {% endif %} Don't have an account yet?
        <a href="{% url 'main:register' %}">Register Now</a>
        </div>

        {% endblock content %}
        ```
    3. Saya membuka kembali `urls.py` yang ada di `main` untuk import fungsi `login_user` dan menambahkan `urlpatterns`
        ```python
        from main.views import login_user
        urlpatterns = [
        ...
        path('login/', login_user, name='login'),
        ]
        ```

- Membuat Fungsi Logout
    1. Saya kembali ke `views.py` di `main` untuk menambahkan import `logout` dan menambahkan fungsi `logout_user` dengan parameter `request` kemudian redirect pengguna ke halaman login jika sudah menghapus sesi pengguna yang saat ini sedang masuk
        ```python
        from django.contrib.auth import logout
        def logout_user(request):
        logout(request)
        return redirect('main:login')
        ```
    2. Menambahkan button Logout disertai redirect ke halaman main yang diletakkan di bagian bawah page
        ```html
        ...
        <a href="{% url 'main:logout' %}">
        <button>Logout</button>
        </a>
        ...
        ```
    3. Saya menambahkan import fungsi `logout_user` yang baru dibuat dan menambahkan *path* ke `urlpatterns` pada file `urls.py`
        ```python
        from main.views import logout_user
        urlpatterns = [
        ...
        path('logout/', logout_user, name='logout'),
        ]
        ```
- Merestriksi Akses Halaman Main
    1. Saya membuka lagi `views.py` pada `main` dan menambahkan *import* `login_required` dan menambahkan `@login_required(login_url='/login')` di atas fungsi `show_main`
        ```python
        from django.contrib.auth.decorators import login_required
        ...
        @login_required(login_url='/login')
        def show_main(request):
        ...
        ```
    2. Saya menjalankan proyek di localhost kemudian muncul halaman login.

###  Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
- Saya membuka localhost kemudian register untuk dua akun pengguna
- Setelah itu saya login dengan masing-masing akun tersebut dan saya menambahkan product minimal 3 pada akun tersebut
- Kemudian saya cek apakah data yang saya masukkan sudah dapat dilihat di  halaman akun tersebut
- Saya memastikan apakah data yang ada di akun pertama berbeda dengan data yang ada di akun kedua

### Menghubungkan model `Product` dengan `User`.
- Menghubungkan Model `Product` dengan `User`
    1. Saya membuka file `models.py` pada `main` kemudian menambahkan import `user` dan menambahkan `models.ForeignKey` ke potongan `Product` saya
        ```python
        from django.db import models
        from django.contrib.auth.models import User
        import uuid 

        class Product(models.Model):
            user = models.ForeignKey(User, on_delete=models.CASCADE)
            id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
            name = models.CharField(max_length=255, name="name")
            price = models.IntegerField(name="price")
            quantity = models.IntegerField(name="quantity", default=0)
            description = models.TextField(name="description")
            category = models.CharField(max_length=255, name="category", default="Uncategorized")
        ```
    2. Saya membuka `views.py` pada `main` dan memodifikasi fungsi `create_product_entry` sebagai berikut:
        ```python
        def create_product_entry(request):
            form = ProductEntryForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('main:show_main')
        
            context = {'form': form}
            return render(request, "create_product_entry.html", context)
        ```
    3. Pada `show_main` saya memodifikasi `show_main` menjadi:
        ```python
        def show_main(request):
            products = Product.objects.filter(user=request.user)
            context = {
                'nama': request.user.username,
                ...
            }
        ```
        Notes: Hal ini dilakukan agar objek `Product` tersambung dengan pengguna yang sedang login. Kemudian agar username pengguna yang sedang login muncul di field nama
    4. Saya melakukan perintah `python manage.py makemigrations` dan `python manage.py migrate`
    5. Buka `settings.py` kemudian import `os` dan mengganti `DEBUG` menjadi kode di bawah ini
        ```python
        import os
        ...
        PRODUCTION = os.getenv("PRODUCTION", False)
        DEBUG = not PRODUCTION
        ```
    6. Jalankan projeknya di localhost. Kemudian apabila kita login dengan akun berbeda, maka data yang muncul per akun akan sesuai dengan data masing-masing akun tersebut. Data yang sudah ada di akun sebelumnya tidak akan muncul lagi di akun yang lain.

###  Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan `cookies` seperti `last login` pada halaman utama aplikasi.
- Menggunakan Data Dari Cookies
    1. Saya membuka kembali `views.py` yang ada di `main` kemudian melakukan *import* sebagai berikut
        ```python
        import datetime
        from django.http import HttpResponseRedirect
        from django.urls import reverse
        ```
    2. Saya memodifikasi fungsi `login_user` dengan menambahkan cookies yaitu `last_login` agar pengguna dapat melihat kapan ia terakhir login. Saya mengganti `if form.is_valid()` dengan kode:
        ```python
        ...
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        ...
        ```
    3. Pada fungsi `show_main` saya menambahkan context `last_login` dengan `request.COOKIES` dan mengubah fungsi `logout_user` menjadi seperti:
        ```python
        @login_required(login_url='/login')
        def show_main(request):
            products = Product.objects.filter(user=request.user)
            context = {
                'nama': request.user.username,
                'kelas': 'PBP D',
                'npm': 2306152052,
                'products': products,
                'last_login': request.COOKIES['last_login'],
            }

        return render(request, "main.html", context)

        ...

        def logout_user(request):
            logout(request)
            response = HttpResponseRedirect(reverse('main:login'))
            response.delete_cookie('last_login')
            return response
        ```

    4. Menambahkan kode button logout yang menampilkan data `last_login` pada berkas `main.html`
        ```html
        ...
        <h5>Sesi terakhir login: {{ last_login }}</h5>
        ...
        ```

    5. Menjalankan di localhost, kemudian saya register dan login. Kemudian data last login saya muncul di halaman main

</details>

<details>
<summary> <b> Tugas 3: Implementasi Form dan Data Delivery pada Django </b> </summary>

# Pertanyaan

## Jelaskan mengapa kita memerlukan *data delivery* dalam pengimplementasian sebuah platform?
Dalam mengimplementasikan sebuah platform, diperlukan pengiriman data dari satu komponen ke komponen lainnya. Sebagai contoh: dari database menuju ke-user agar dapat mengakses dan menampilkan data yang diminta user. *Data delivery* dibutuhkan untuk mengoptimalkan dan mengefisiensikan proses pengiriman data, apalagi untuk platform beskala besar. Dengan *data delivery*, dapat membuat proses pengiriman data tepat waktu, sehingga memberikan pengalaman pengguna yang lebih baik, juga keamanan data yang terjamin. Format yang populer digunakan (dan sekarang sedang dipelajari) adalah HTML, XML, dan JSON. 

## Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
PERBEDAAN XML dan JSON:
1. XML menyimpan data dalam struktur pohon dengan *namespace* untuk kategori data yang berbeda. Sedangkan JSON menggunakan struktur mapping dengan pasangan key-value.
2. XML memiliki sintaks yang lebih kompleks. Sebagai contoh penggunaan tag pembuka dan penutup `<tag></tag>`. Sedangkan JSON hanya menggunakan kurung kurawal `{}`, kurung siku `[]`, dan titik dua `:` antara nama dan nilai, sehingga lebih ringkas.
3. XML membutuhkan waktu lebih lama untuk parsing, dikarenakan formatnya yang lebih kompleks. Sedangkan JSON lebih cepat diparsing, dikarenakan strukturnya yang lebih sederhana.
4. XML tidak dapat diintegrasikan langsung oleh JavaScript tanpa dilakukannya parsing tambahan. Sedangkan JSON didesain agar dapat langsung digunakan oleh JavaScript tanpa memerlukan konversi tambahan.
5. XML cenderung lebih sulit dibaca, terutama apabila data dan platform yang digunakan besar. Hal ini dikarenakan XML melibatkan lebih banyak tag. Sedangkan JSON lebih mudah dibaca karena struktur lebih ringkas dan sederhana.

Dengan perbedaan yang saya paparkan, dapat kita lihat bahwa JSON lebih sederhana, ringkas, dan efisien. Penggunaan JSON memudahkan *developer* dalam membuat platform dan mengolah datanya. Sehingga dapat dilihat JSON lebih populer daripada XML.

## Jelaskan fungsi dari method `is_valid()` pada form Djangoo dan mengapa kita membutuhkan method tersebut?
Method is_valid() digunakan untuk melakukan validasi untuk setiap kolom formulir, mengembalikan true jika data valid. Dalam konteks tugas 3, Method is_valid() berfungsi untuk memeriksa apakah data yang dikirimkan oleh pengguna sesuai dengan kebutuhan yang ada di form `ProductEntryForm`(Memastikan fields yanga da pada `forms.py` sesuai dengan yang ada pada `models.py`). Kita membutuhkan method is_valid() untuk memastikan agar tidak ada data yang tidak sesuai yang masuk ke database sistem. Sehingga kita menjaga konsistensi data dan memungkinkan pemberian feedback yang jelas kepada user apabila ada kesalahan.

## Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
- `csrf_token` atau yang disebut *Cross-Site Request Forgery* token untuk melindungi platform dari serangan *Cross-Site Request Forgery*(CSRF). Serangan CSRF adalah ketika penyerang melakukan eksploitasi platform yang membuat pengguna tanpa sadar mengirim sebuah permintaan POST yang tidak diinginkan. Sistem kerjanya adalah penyerang menggunakan/membajak sesi pengguna yang sudah diautentifikasi tanpa sepengetahuan pengguna. Kita membutuhkan `csrf_token` saat membuat form di Django agar mencegah serangan saat sedang pembuatan form dengan adanya permintaan POST palsu.
- Jika kita tidak menambahkan `csrf_token` maka platform rentan terhadap serangan CSRF. Platform tidak dapat memverifikasi apakah permintaan berasal dari pengguna yang sah atau bukan. Sehingga dapat keamanan pengguna tercancam.
- Hal ini dapat dimanfaatkan oleh penyerang dengan mengirimkan permintaan yang berbahaya kepada user (misal melakukan transaksi keuangan yang tidak diinginkan dan mengubah kata sandi).


## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekedar mengikuti tutorial).

- Implemetasi Skeleton sebagai Kerangka Views
    1. Saya membuat direktor baru bernama `templates` di folder utama. Kemudian saya membuat berkas HTML baru yang bernama `base.html`. File `base.html` tersebut diisi dengan kode:
        ```html
        {% load static %}
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta charset="UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                {% block meta %} {% endblock meta %}
            </head>

            <body>
            {% block content %} {% endblock content %}
            </body>
        </html>
        ```
        Notes: `{% load static %}` digunakan sebagai template tag dalam Django. `<!DOCTYPE html>` digunakan sebagao pendefinisian jenis dokumen HTML5. 

    2. Kemudian saya menambahkan `[BASE_DIR / 'templates']` pada subbagian `DIRS` dalam bagian `TEMPLATES` yang ada di dalam file `settings.py`. Penambahan yang saya lakukan adalah sebagai berikut:
        ```python
        TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    ],
                },
            },
        ]
        ```
        Notes: Penambahan yang saya lakukan bertujuan agar file `base.html` pada `templates` dijadikan sebagai template tujuan.

    3. Saya mengubah `main.html` yang ada di direktori `main/templates` dengan menambahkan ` {% extends 'base.html' %}` dan `{% block content %}` di awal kode. Kemudian juga menambahkan `{% endblock content %}` di akhir kode. Hal ini mengindikasikan bahwa kita menggunakan `base.html` sebagai template utama dan menginisiasikan dimana *block content* di mulai dan di mana berhenti.

- Menambahkan UUID
    1. Menambahkan `import uuid` dan `id=` di dalam `main/models.py`. Guna dari menambahkan import UUID ini adalah untuk mengimport modul UUID yang akan memberikan string unik untuk ID sebagai *identifier*. Perubahan yang saya lakukan seperti ini: 
        ```python
        from django.db import models
        import uuid 

        class Product(models.Model):
            id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
            name = models.CharField(max_length=255, name="name")
            price = models.IntegerField(name="price")
            quantity = models.IntegerField(name="quantity", default=0)
            description = models.TextField(name="description")
            category = models.CharField(max_length=255, name="category", default="Uncategorized")
        ```
        Notes: Pada fields `quantity` dan `category` saya menetapkan default valuenya.

    2. Karena dilakukan perubahan pada models. Maka saya melakukan migrasi model dengan perintah:
        ```bash
        python manage.py makemigrations
        python manage.py migrate
        ```

- Membuat Form Input Data dan Menampilkannya pada HTML
    1. Pada direktori `main`, buat file baru bernama `forms.py`. Saya memasukkan kode sebagai berikut:
        ```python
        from django.forms import ModelForm
        from main.models import Product
    
        class ProductEntryForm(ModelForm):
            class Meta:
            model = Product
            fields = ["name", "price", "quantity", "description", "category"]
        ````
        Notes: Saya mengisi fields sesuai dengan yang ada di `models.py` saya.
    2. Pada direktori `main`, saya membuka `views.py` dan menambahkan `import redirect` dan membuat fungsi baru bernama `create_product_entry` yang menerima parameter `request`. Fungsi ini bertujuan untuk menambahkan input form ke dalam permintaan POST untuk database. Saya juga mengubah fungsi `show_main`. Penambahan kode yang saya lakukan ke `views.py` adalah sebagai berikut:
        
        ```python
        from django.shortcuts import render, redirect
        from main.models import Product
        from main.forms import ProductEntryForm

        def show_main(request):
            products = Product.objects.all()
            context = {
                'nama': 'Alyssa Layla Sasti',
                'kelas': 'PBP D',
                'npm': 2306152052,
                'products': products,
            }

        return render(request, "main.html", context)

        def create_product_entry(request):
            form = ProductEntryForm(request.POST or None)

            if form.is_valid() and request.method == "POST":
                form.save()
                return redirect('main:show_main')

            context = {'form': form}
        return render(request, "create_product_entry.html", context)
        ```
        Notes: Redirect digunakan untuk mengarahkan pengguna ke url tertentu, dalam konteks tugas ini adalah menuju `main:show_main`

    3. Saya menambahkan import fungsi `create_product_entry` ke dalam `urls.py` yang ada di `main` dan menambahlan *path* URL ke dalam *urlpatterns*

        ```python
        from main.views import show_main, create_product_entry

        urlpatterns = [
            path('', show_main, name='show_main'),
            path('create-product-entry', create_product_entry, name='create_product_entry'),
        ]
        ````
    4. Saya membuat file HTML baru dengan nama `create_product_entry.html` pada direktori `main/templates`. Kemudian saya mengisi dengan kode sebagai berikut:
        ```html
        {% extends 'base.html' %} 
        {% block content %}
        <h1>Add New Product Entry</h1>

        <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Product" />
            </td>
            </tr>
        </table>
        </form>

        {% endblock %}
        ```
    5. Menambahkan kode di `main.html` untuk menampilkan data *product* dan button *Add New Product*. Perubahan kode yang saya lakukan adalah sebagai berikut:
        ```html
        {% extends 'base.html' %}
        {% block content %}
        <h1>Welcome to YESTORE!</h1>

        <h2>Nama Mahasiswa: </h2>
        <p>{{ nama }}</p>
        <h2>Kelas: </h2>
        <p>{{ kelas }}</p>
        <h2>NPM: </h2>
        <p>{{ npm }}</p>

        {% if not products %}
        <p>Belum ada data product pada YESTORE.</p>
        {% else %}
        <table>
        <tr>
            <th>Name</th>
            <th>Price</th>
            <th>Quantity</th>
            <th>Description</th>
            <th>Category</th>
        </tr>

        {% comment %} 
        {% endcomment %} 
        {% for product in products %}
        <tr>
            <td>{{product.name}}</td>
            <td>{{product.price}}</td>
            <td>{{product.quantity}}</td>
            <td>{{product.description}}</td>
            <td>{{product.category}}</td>
        </tr>
        {% endfor %}
        </table>
        {% endif %}

        <br />

        <a href="{% url 'main:create_product_entry' %}">
        <button>Add New Product</button>
        </a>
        {% endblock content %}
        ```
    6. Jalankan `python manage.py runserver` kemudian buka  http://localhost:8000/, seharusnya web sudah dapat dibuka dan digunakan

- Mengembalikan Data dalam Bentuk XML
    1. Menambahkan `import HttpResponse` dan `Serializer` di file `views.py` pada `main`
        ```python
        from django.shortcuts import render, redirect
        from main.models import Product
        from main.forms import ProductEntryForm
        from django.http import HttpResponse
        from django.core import serializers
        ```
    2. Membuat fungsi `show_xml` yang menerima parameter `request` disertai *return function* berupa `HttpResponse` masih di file `views.py` pada `main`
        ```python
        def show_xml(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
        ```
    3. Menambahkan  import `show_xml` dan *path url* ke `urlpatterns` di dalam `urls.py` pada `main` 
        ```python
        from main.views import show_main, create_product_entry, show_xml
        
        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
            path('create-product-entry', create_product_entry, name='create_product_entry'),
            path('xml/', show_xml, name='show_xml'),
        ]
        ```
    4.  Jalankan `python manage.py runserver` kemudian buka  http://localhost:8000/xml/, seharusnya web sudah dapat dibuka dan digunakan

- Mengembalikan Data dalam Bentuk JSON
    1. Membuat fungsi `show_json` yang menerima parameter `request` disertai *return function* berupa `HttpResponse` di file `views.py` pada `main`
        ```python
        def show_json(request):
            data = Product.objects.all()
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")
        ```
    2. Menambahkan  import `show_json` dan *path url* ke `urlpatterns` di dalam `urls.py` pada `main`
        ```python
        from django.urls import path
        from main.views import show_main, create_product_entry, show_xml, show_json

        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
            path('create-product-entry', create_product_entry, name='create_product_entry'),
            path('xml/', show_xml, name='show_xml'),
            path('json/', show_json, name='show_json'),
        ]
        ``` 
    3. Jalankan `python manage.py runserver` kemudian buka  http://localhost:8000/json/, seharusnya web sudah dapat dibuka dan digunakan


- Mengembalikan Data Berdasarkan ID dalam Bentuk XML dan JSON
    1. Membuat fungsi `show_xml_by_id` yang menerima parameter `request` dan `id` disertai *return function* berupa `HttpResponse` di file `views.py` pada `main`
        ```python
        def show_xml_by_id(request, id):
            data = Product.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
        ```
    2.  Membuat fungsi `show_json_by_id` yang menerima parameter `request` dan `id` disertai *return function* berupa `HttpResponse` di file `views.py` pada `main`
        ```python
        def show_json_by_id(request, id):
            data = Product.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")
        ```
    3. Menambahkan  import `show_xml_by_id`, `show_json_by_id` dan *path url* ke `urlpatterns` di dalam `urls.py` pada `main`
        ```python
        from django.urls import path
        from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id

        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
            path('create-product-entry', create_product_entry, name='create_product_entry'),
            path('xml/', show_xml, name='show_xml'),
            path('json/', show_json, name='show_json'),
            path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
            path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
        ]
        ```
    4. Jalankan `python manage.py runserver` kemudian buka  http://localhost:8000/xml/(masukkan id) dan http://localhost:8000/json/(masukkan id) sesuai dengan id input product yang diberikan. 

- Push ke git hasil Tugas 3
    ```bash
    git add .
    git commit -m
    git push -u origin main
    git push pws main:master
    ```

# Bukti Screenshot hasil akses URL pada Postman
1. Localhost
![Localhost](/images/localhost.png)

2. Localhost XML
![Localhost XML](/images/localhost_xml.png)

3. Localhost JSON
![Localhost JSON](/images/localhost_json.png)

4. Localhost XML ID
![Localhost XML ID](/images/localhost_xml_id.png)

5. Localhost JSON ID
![Localhost JSON ID](/images/localhost_json_id.png)
</details>

<details>
<summary> <b> Tugas 2: Implementasi Model-View-Template (MVT) pada Django </b> </summary>

# Pertanyaan

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekedar mengikuti tutorial)!

- Membuat sebuah proyek Django baru. <br>
    1. Menginsiasi Git pada Directory Baru
        -  Melakukan konfigurasi awal git dengan membuat directory baru di lokal bernama `yestore`.
        - Membuka terminal, kemudian melakukan cd ke directory path yestore yang baru saya buat. Kemudian melakukan perintah `git init`, `git config --global user.name "AlyssaLayla"`, dan `git config --global user.email "alyssasasti@gmail.com"`
        -  membuat repositori baru di GitHub dengan nama yestore dan mengatur visibilitasnya sebagai public
        -  Membuat `README.md`, `git status`, `git add README.md`. Kemudian saya mengecek kembali status README.md dengan `git status`. Lalu jalankan `git commit -m "Make README.md"`
        - Membuat branch utama dengan menjalankan perintah `git branch -M main`. Dengan menjalankan perintah ini, branch utamanya akan bernama "main".
        - Menjalankan perintah `git remote add origin https://github.com/AlyssaLayla/yestore.git`
        - Menjalankan `git push -u origin main`

    2. Mengaktifkan Virtual Environment
        -  Menjalankan perintah `python -m venv env` dan `env\Scripts\activate`
        - Notes: Ditandai dengan adanya (env) pada awal baris di terminal

    3. Install Dependencies
        - Membuat file baru bernama `requirements.txt` dan mengeditnya melalui IDE dengan isi:
        ```bash
        django
        gunicorn
        whitenoise
        psycopg2-binary
        requests
        urllib3
        ```
        - Instalasi dependencies yang ada di file `requirements.txt` dengan perintah `pip install -r requirements.txt`
    
    4. Membuat Proyek Django
        - Menjalankan perintah `django-admin startproject yestore` untuk membuat proyek Django bernama "yestore"

    5. Mempersiapkan untuk Menjalankan Server
        - Mengedit file `settings.py` kemudian menambahkan `"localhost"` dan `"127.0.0.1"` pada `ALLOWED-HOSTS`
        - Membuat file baru bernama `.gitignore` dan mengeditnya melalui iDE dengan isi:

        ```bash
        # Django
        *.log
        *.pot
        *.pyc
        __pycache__
        db.sqlite3
        media

        # Backup files
        *.bak

        # If you are using PyCharm
        # User-specific stuff
        .idea/**/workspace.xml
        .idea/**/tasks.xml
        .idea/**/usage.statistics.xml
        .idea/**/dictionaries
        .idea/**/shelf

        # AWS User-specific
        .idea/**/aws.xml

        # Generated files
        .idea/**/contentModel.xml
        .DS_Store

        # Sensitive or high-churn files
        .idea/**/dataSources/
        .idea/**/dataSources.ids
        .idea/**/dataSources.local.xml
        .idea/**/sqlDataSources.xml
        .idea/**/dynamic.xml
        .idea/**/uiDesigner.xml
        .idea/**/dbnavigator.xml

        # Gradle
        .idea/**/gradle.xml
        .idea/**/libraries

        # File-based project format
        *.iws

        # IntelliJ
        out/

        # JIRA plugin
        atlassian-ide-plugin.xml

        # Python
        *.py[cod]
        *$py.class

        # Distribution / packaging
        .Python build/
        develop-eggs/
        dist/
        downloads/
        eggs/
        .eggs/
        lib/
        lib64/
        parts/
        sdist/
        var/
        wheels/
        *.egg-info/
        .installed.cfg
        *.egg
        *.manifest
        *.spec

        # Installer logs
        pip-log.txt
        pip-delete-this-directory.txt

        # Unit test / coverage reports
        htmlcov/
        .tox/
        .coverage
        .coverage.*
        .cache
        .pytest_cache/
        nosetests.xml
        coverage.xml
        *.cover
        .hypothesis/

        # Jupyter Notebook
        .ipynb_checkpoints

        # pyenv
        .python-version

        # celery
        celerybeat-schedule.*

        # SageMath parsed files
        *.sage.py

        # Environments
        .env
        .venv
        env/
        venv/
        ENV/
        env.bak/
        venv.bak/

        # mkdocs documentation
        /site

        # mypy
        .mypy_cache/

        # Sublime Text
        *.tmlanguage.cache
        *.tmPreferences.cache
        *.stTheme.cache
        *.sublime-workspace
        *.sublime-project

        # sftp configuration file
        sftp-config.json

        # Package control specific files Package
        Control.last-run
        Control.ca-list
        Control.ca-bundle
        Control.system-ca-bundle
        GitHub.sublime-settings

        # Visual Studio Code
        .vscode/*
        !.vscode/settings.json
        !.vscode/tasks.json
        !.vscode/launch.json
        !.vscode/extensions.json
        .history
        ```
    <hr>

- Membuat aplikasi dengan nama `main` pada proyek tersebut. <br>
    - Menjalankan perintah `python manage.py startapp main`
    - Mengedit file `settings.py` dan menambahkan `main` pada `INSTALLED_APPS`
    - Membuat directory (folder) baru bernama `templates` di dalam directory `main`. Kemudian di dalam folder ini, buat file baru bernama `main.html` untuk menyimpan file `.html` yang ingin digunakan. File ini berisi konten yang ingin ditampilkan di web. Bagian yang wajib ada adalah nama e-commerce, nama mahasiswa, dan kelas.
    <hr>

- Melakukan routing pada proyek agar dapat menjalankan aplikasi main. <br>
    - Mengonfigurasi routing URL pada proyek yestore. Buka file `urls.py` di dalam directory proyek `yestore`
    - Menambahkan import `include` pada `from django.urls import path, include`
    - Menambahkan route url dengan mengarahkan ke tampilan `main` di dalam variabel `urlpatterns` menjadi
        ```python
        urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
        ]
        ```
    <hr>

- Membuat model pada aplikasi main dengannama Product dan memiliki atribut wajib (`name` (CharField), `price` (IntegerField), dan `description` (TextField)) <br>
    - Mengedit file `models.py` pada directory `main` dengan:
        ```python
        
        from django.db import models

        class Product(models.Model):
            name = models.CharField(max_length=255, name="name")
            price = models.IntegerField(name="price")
            quantity = models.IntegerField(name="quantity")
            description = models.TextField(name="description")
            category = models.CharField(max_length=255, name="category")
        ```
    - Notes: Saya mengisi `models.py` dengan 5 atributes yaitu `name` (CharField), `price` (IntegerField), `quantity` (IntegerFIeld), `description` (TextField), dan `category`(CharField)

    - Menjalankan perintah `python manage.py makemigrations` dan `python manage.py migrate` setiap kita membuat perubahan pada model
    <hr>

-  Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas mahasiswa. <br>
    - Mengedit `views.py` pada `main` dengan kode: 
        ```python
        from django.shortcuts import render

        def show_main(request):
            context = {
                'nama': 'Alyssa Layla Sasti',
                'kelas': 'PBP D',
                'npm': 2306152052,
                'products': [ 
                    {'name': 'Dimsum Mozarella', 'price': 20000, 'quantity': 5, 'description': 'Dimsum dengan keju Mozarella meleleh di atasnya wow enak', 'category': 'Makanan'},
                    {'name': 'Charger HP', 'price': 100000, 'quantity': 8, 'description': 'Charge HP dijamin Original!', 'category': 'Elektronik'},
                    {'name': 'Hoodie', 'price': 50000, 'quantity': 3, 'description': 'Hoodie Oversize paling keren se-UI', 'category': 'Pakaian'},
                    ],
            }

            return render(request, "main.html", context)
        ```
    - Notes: Selain ingin menampilkan nama aplikasi, nama mahasiswa, dan kelasnya, saya ingin menampilkan atribut-atribut lain. Maka dari itu di `views.py`, saya menampilkan nama, kelas, npm, dan Product yang saya jual dengan detail (product name, price, quantity, description, dan category)

    - Saya menambahkan tampilan yang saya inginkan di `main.html` agar dapat menampilkan data yang telah diambil dari model sebagai berikut
        ```html
        <h1>Welcome to YESTORE!</h1>

        <h2>Nama Mahasiswa: </h2>
        <p>{{ nama }}</p>
        <h2>Kelas: </h2>
        <p>{{ kelas }}</p>
        <h2>NPM: </h2>
        <p>{{ npm }}</p>

        <h3>Apa yang Kami Jual?</h3>
        <ol>
            {% for product in products %}
            <li> 
                <h4>{{product.name}}</h4>
                <h5>Rp{{product.price}}</h5>
                <h5>Quantity: {{product.quantity}}</h5>
                <p>{{product.description}}</p>
                <h5>Category: {{product.category}}</h5>
                {% endfor %}
            </li>
        </ol>
        ```
    <hr>

- Membuat sebuah routing pada `urls.py` aplikasi main untuk memetakan fungsi yang telah dibuat pada `views.py` <br>
    - Buka file `urls.py` di `main`, kemudian saya isi dengan kode ini
        ```python
        from django.urls import path
        from main.views import show_main

        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
        ]
        ```
    <hr>

- Membuat deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses di internet <br>
    - Sebelum ke PWS, saya melakukan `git add .`, `git commit -m "<message>"`, dan `git push -u origin main` untuk mengupdate perubahan ke GitHub
    - Saya mencoba run di local host terlebih dahulu. Jalankan perintah `python manage.py runserver` kemudian saya cek di `http://localhost:8000/`. Jika halaman yang saya buat sudah muncul, saya lanjut deploy ke PWS
    - Login di PWS, lalu menambahkan projek baru dengan nama `yestore`
    - Buka kembali `settings.py` kemudian tambahkan `alyssa-layla-yestore.pbp.cs.ui.ac.id` di `ALLOWED_HOSTS`
    - Melakukan kembali `git add .`, `git commit -m"<message>"`, dan `git push -u origin main`
    - Menjalankan perintah `git remote add pws http://pbp.cs.ui.ac.id/alyssa.layla/yestore` agar terhubung antara pws dengan lokal
    - Menjalankan perintah `git branch -M master` dan `git push pws master` agar kode di lokal bisa diupdate ke pws dan dilihat web nya di internet
    - Menjalankan `git branch -M main` agar branch utama kembali lagi menjadi `main`
    - Untuk kedepannya ketika saya melakukan perubahan, setelah push di GitHub, saya hanya perlu melakukan perintah `git push pws main:master` untuk push di PWS.
    - Deployment selesai. Tampilan web di local host dan di PWS seharusnya sama.
    <hr>

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `.html`.

![Bagan](/images/bagan.png)

- Alur keseluruhan: 
    - Client/user melakukan request -> Internet melanjutkan request -> `urls.py` melanjutkan request berupa route -> `views.py` melanjutkan ke `models.py` dan template `main.html`
    - `views.py` ke `models.py`
    `views.py` melakukan transaksi data modification ke `models.py` -> `models.py` mengakses database untuk melakukan modifikasi data. Lalu setelah dimodifikasi sesuai request akan dikembalikan ke `models.py` dan dilanjutkan memberi data yang lengkap ke `views.py`
    - `views.py` ke template `main.html`
    `views.py` melakukan display data ke template `main.html` -> Kemudian dikembalikan data input by user ke `views.py`
    - Setelah dari `models.py` dan `main.html` sudah lengkap tergabung semua di `views.py` -> Dikembalikan responnya ke internet berdasarkan request klien -> Kemudian dari internet akan diberkan ke klien berupa web page sesuai request

- Kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `.html`
Kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `.html `dapat dilihat di alur yang sudah saya jelaskan sebelumnya. `urls.py` dilakukan untuk konfigurasi routing dan dilanjutkan ke `views.py`. File ini sebagai logika aplikasi untuk data organization/preparation layer yang akan meneruskan ke `models.py` (Database layer) dan berkas .`html` (Tampilan pengguna). Ketika `models.py` dan berkas `.html` sudah melakukan request pengguna, kedua bagian tersebut dikembalikan lagi ke `views.py`. Pada kondisi ini, `views.py` sudah berisi html merged dengan database yang dibutuhkan dari model. Setelah itu `views.py` akan meneruskan ke internet dan diteruskan kembali ke klien sebagai web page.

## Jelaskan fungsi git dalam pengembangan perangkat lunak!
- Versi Kontrol
Git memungkinkan developer untuk melacak perubahan kode. Siapa yang melakukan perubahan, apa yang diubah, dan kapan diubah. Semua itu dapat kita lihat di riwayat pada Git
- Kolaborasi
Git memudahkan apabila ingin ada kolaborasi antar-developer dalam suatu proyek. Adanya fitur pull, branching, dan merging dapat memudahkan tiap developer untuk mengerjakan proyek kolaborasi secara paralel di waktu yang sama. 
- Branching dan Merging
Dengan branching, kita dapat push kode tanpa mengubah branch utama. Kemudian apabila diperlukan, kita bisa merging branch tersebut menjadi satu. Hal ini dibutuhkan apabila ingin ada pengembangan fitur baru atau debugging di branch terpisah. Baru setelah selesai, perubahan tersebut dapat di merge ke branch utama
- Backup
Git menyimpan riwayat perubahan kode di setiap commit yang kita lakukan. Jika kita ingin melihat riwayat perubahan yang kita lakukan, dapat dilakukan dengan melihat riwayat backup kode yang sudah kita commit sebelumnya

## Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
- Django menggunakan bahasa python yang cenderung lebih literal dan lebih mudah dipahami
- Django memiliki struktur MVT (Model-View-Template) sehingga memudahkan pemahaman alur pengembangan perangkat lunak. Model untuk interaksi dengan database, View untuk logika aplikasi dan respon terhadap permintaan user, dan Template untuk fokus ke tampilan pengguna (User Interface)
- Adanya keamanan yang terintegrasi secara default.
- Adanya ORM (Object-Relational Mapping) bawaan. Hal ini mempermudah developer dalam akses database. Developer tidak perlu menulis kode SQL secara langsung. Melainkan, dapat menggunakan python untuk membuat, membaca, dan memodifikasi data.

## Mengapa model pada Django disebut sebagai ORM?
Django disebut ORM atau Object-Relational-Mapping karena ORM menghubungkan objek dalam kode dengan tabel dalam database relasional. Hal ini dikarenakan adanya otomasi query SQL sehingga developer tidak perlu menulis query SQL manual untuk akses ke database. Cukup dengan python saja sudah bisa mengakses dan memanipulasi data di database.
</details>