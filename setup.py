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
        "PyJWT>=2.3.0",
        "Flask>=1.1.1",
        "Flask-SQLAlchemy>=2.5.1",
        "Flask-RESTful>=0.3.9",
        "Flask-JWT>=0.3.2",
        "Flask-Migrate>=3.1.0",
        "Flask-JWT-Extended>=4.3.1",
        "jwt>=1.3.1",
        "pyyaml>=6.0"
    ],
)
