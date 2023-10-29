### Разработка


```bash
pipenv install
```

#### Публикация пакета

Опубликовать пакет ermini на pypi.org:

```bash
# python manage.py publish_on_pypi <package_name>
python manage.py publish_on_pypi ermini_utils
python manage.py publish_on_pypi ermini
```

#### publish

```bash
pipenv run pip3 freeze > ./backend/ermini/requirements.txt
python3 ./backend/ermini/setup.py sdist bdist_wheel
rm -rf build ermini.egg-info dist
```