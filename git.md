## Githuba push nasıl edilir!!!
pip install python-decouple >> import et
gitignore ile aynı konumda env dosyası oluştur

setting.py içerisindeki SECRET KEY'i >>>>> env file taşı

setting.py file içerisine aşağıdaki komutları çalıştır.

from decouple import config

SECRET_KEY = config('SECRET_KEY')
!!!! env file SECRET KEY TIRNAKLARINI KALDIR.!!!