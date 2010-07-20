import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages

setup(
    name = "django-searchapi",
    version = "0.1.0",
    packages = ['searchapi',
               ],
    zip_safe = False,
    author = "Agiliq Solutions",
    author_email = "info@agiliq.com",
    description = "Api over a number of search engines.", 
    url = "http://agiliq.com/",
)
