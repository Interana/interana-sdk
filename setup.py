from setuptools import setup

setup(
  name = 'interanasdk',
  packages = ['interanasdk'],
  version = '0.0.2',
  description = 'Interana SDK',
  scripts=['bin/ia_query_client'],
  author = 'Sachin Holla',
  author_email = 'sachin@interana.com',
  url = 'https://github.com/Interana/interana-sdk',
  download_url = 'https://github.com/Interana/interana-sdk/archive/0.0.2.tar.gz',
  keywords = [
                 'interana',
                 'sdk',
                 'query-api'
             ],
  classifiers = [],
  install_requires=[
   'requests'
  ]
)
