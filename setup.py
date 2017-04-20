from setuptools import setup

setup(
  name = 'interanasdk',
  packages = ['interanasdk'],
  version = '0.1.1',
  description = 'Interana SDK',
  scripts=['bin/ia_query_client'],
  author = 'Sachin Holla',
  author_email = 'sachin@interana.com',
  url = 'https://github.com/Interana/interana-sdk',
  download_url = 'https://github.com/Interana/interana-sdk/archive/0.1.1.tar.gz',
  keywords = [
                 'interana',
                 'sdk',
                 'query-api'
             ],
  classifiers = [],
  install_requires=[
   'requests>=2.9.1'
  ]
)
