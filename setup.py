from distutils.core import setup, Extension

module = Extension('alephzero',
                   include_dirs = ['/usr/local/include'],
                   library_dirs = ['/usr/local/lib'],
                   libraries = ['alephzero'],
                   sources = ['alephzero.cc'])

setup (name = 'AlephZero',
       version = '0.1',
       description = 'TODO: description',
       author = 'Leonid Shamis',
       author_email = 'leonid.shamis@gmail.com',
       url = 'https://github.com/alephzero/py',
       long_description = '''TODO: long description''',
       ext_modules = [module])

