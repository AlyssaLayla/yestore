# YESTORE
**Situs Deployment:** http://alyssa-layla-yestore.pbp.cs.ui.ac.id/

Nama    : Alyssa Layla Sasti

Kelas   : PBP D

NPM     : 2306152052

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
            category = models.CharField(max_length=255, 
            name="category")

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

## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![Bagan](/yestore/bagan.png)

- Alur keseluruhan: 
    - Client/user melakukan request -> Internet melanjutkan request -> urls.py melanjutkan request -> views.py melanjutkan ke models.py dan template (main.html)
    - views.py ke models.py
    views.py melakukan transaksi data modification ke models.py -> models.py mengakses database untuk melakukan modifikasi data. Lalu setelah dimodifikasi sesuai request akan dikembalikan ke models.py dan dilanjutkan memberi data yang lengkap ke views.py
    - views.py ke template (main.html)
    views.py melakukan display data ke template (main.html) -> Kemudian dikembalikan data input input by user ke views.py
    - Setelah dari models.py dan main.html sudah lengkap tergabung semua di views.py -> Dikembalikan responnya ke internet berdasarkan request klien -> Kemudian dari internet akan diberkan ke klien berupa web page sesuai request

- Kaitan antara urls.py, views.py, models.py, dan berkas html
Kaitan antara urls.py, views.py, models.py, dan berkas html dapat dilihat di alur yang sudah saya jelaskan sebelumnya. `urls.py` dilakukan untuk konfigurasi routing dan dilanjutkan ke `views.py`. File ini sebagai logika aplikasi untuk data organization/preparation layer yang akan meneruskan ke models.py (Database layer) dan berkas .`html` (Tampilan pengguna). Ketika models.py dan berkas html sudah melakukan request pengguna, kedua bagian tersebut dikembalikan lagi ke views.py. Pada kondisi ini, views.py sudah berisi html merged dengan database yang dibutuhkan dari model. Setelah itu views.py akan meneruskan ke internet dan diteruskan kembali ke klien sebagai web page.

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