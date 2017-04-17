from distutils.core import setup
setup(
  name = 'foobar',
  packages = ['foobar'], # this must be the same as the name above
  version = '0.1',
  description = 'A foobar lib',
  author = 'Sachin Holla',
  author_email = 'sachin@interana.com',
  url = 'https://github.com/Interana/interana-sdk', # use the URL to the github repo
  download_url = 'https://github.com/Interana/interana-sdk/archive/0.2.tar.gz', # I'll explain this in a second
  keywords = ['testing', 'foobar', 'example'], # arbitrary keywords
  classifiers = [],
)
