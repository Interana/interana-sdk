from distutils.core import setup
setup(
  name = 'interanasdk',
  packages = ['interanasdk'], # this must be the same as the name above
  version = '0.2',
  description = 'Interana SDK',
  scripts=['bin/ia_query_client'],
  author = 'Sachin Holla',
  author_email = 'sachin@interana.com',
  url = 'https://github.com/Interana/interana-sdk', # use the URL to the github repo
  download_url = 'https://github.com/Interana/interana-sdk/archive/0.2.tar.gz', # I'll explain this in a second
  keywords = ['interana','sdk','query-api'], # arbitrary keywords
  classifiers = [],
  install_requires=[
   'requests>=2.9.1'
  ]
)
