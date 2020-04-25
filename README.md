# ayudaPy

Platform to help people help people

#### URL

https://ayudaec.org

## Requirements

- Python 3.6+
- Django 2.2+
- PostGIS 3.0+
- PostgreSQL 11+

## Install

GeoDjango https://kitcharoenp.github.io/gis/2018/06/12/geodjango_installation.html

```
git clone https://github.com/AngelNavarroR/ayudaec.git
cd ayudapy
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cp conf/.env.example conf/.env # you should edit this file with your configuration
./manage.py migrate
./manage.py runserver
```

We use `django-pipeline` to handle CSS/JS assests, and this library requires `yuglify`. To install `yuglify`, issue the following:

```
npm -g install yuglify
```

The above command assumes that [NPM](https://www.npmjs.com/get-npm) is available.

## Install using docker-compose

```
git clone git@github.com:melizeche/ayudapy.git && cd ayudapy
cp conf/.env.example conf/.env # you should edit this file with your configuration
docker-compose up -d --build
docker-compose exec app ./manage.py migrate
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Add your name and git account to the Contributors section in this `Readme.MD` :D
6. Submit a pull request to `dev` branch

## Author

- Marcelo Elizeche Landó https://github.com/melizeche

## Contributors / Thanks

- 

## TODO

- Documentation
- Support geolocation
- Captcha
- ~~Create models~~
- Users(?)
- Test

More in [TODO.md](TODO.md)

## License

This project is licensed under the terms of the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details
