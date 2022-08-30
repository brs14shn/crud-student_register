<h1 style="color: green">Githuba push nasıl edilir!!!<h1>

(1)-pip install python-decouple >> import et
gitignore ile aynı konumda env dosyası oluştur

(2) setting.py içerisindeki SECRET KEY'i >>>>> env file taşı

setting.py file içerisine aşağıdaki komutları çalıştır.
```
from decouple import config
SECRET_KEY = config('SECRET_KEY')
```
!!!! env file SECRET KEY TIRNAKLARINI KALDIR.!!!

<h1 style="color: red">Githubtan veri çekerken;aşağıdaki adımları uygula;<h1>

```
python -m venv env
source env/Scripts/Activate (windows)
source env/bin/activate(macos)
pip install -r requirements.txt

```