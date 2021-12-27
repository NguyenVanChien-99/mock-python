from setuptools import setup

setup(
    name='MockProhect',
    version='0.0.1',
    author='Chien Nguyen',
    author_email='nguyenvanchien309318@gmail.com',
    packages=['controller', 'database', 'entity', 'repository', 'security', 'third_party', 'utils'],
    include_package_data=True,
    description='An awesome package that does something',
    install_requires=[
        "Werkzeug",
        "SQLAlchemy",
        "PyMySQL",
        "PyJWT",
        "Flask",
        "Flask-SQLAlchemy",
        "Flask-RESTful",
        "Flask-JWT",
        "Flask-Migrate",
        "Flask-JWT-Extended",
    ],
)
