# lotteng
🦁2020 멋쟁이 사자처럼 8기 해커톤 LOTTENG🕒

## Dev Usage

1. fork repo `https://github.com/hyeoneedyou/lotteng`

2. clone your fork repo

```bash
$ git clone https://github.com/YOUR_GITHUB_USERNAME/lotteng.git
```

3. make venv & pip install
```bash
$ cd lotteng
$ python -m venv venv
$ source ./venv/bin/activate 또는 .\venv\Scripts\activate
$ pip install -r requirements.txt
```

4. migrate & runserver
```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py collectstatic
$ python manage.py runserver
```
