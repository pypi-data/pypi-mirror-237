from setuptools import setup
import sys, os.path, shutil

version = '1.2.1'

if sys.version_info.major < 3:
    sys.stderr.write("pysimpqr requires Python 3.2+ ")
    sys.exit(1)

if os.path.exists('docs/README.md'):
    print('Reading README.md file')
    with open( 'docs/README.md', 'r') as f:
        longdesc = f.read()
    shutil.copyfile('docs/README.md', 'README.md')
else:
    longdesc = None

setup(name='PySimpQR',
      packages=['pysimpqr'],
      version=version,
      description='pysimpqr is a module that can help you to create qr codes using only two lines',
      author='PixCap',
      url='https://github.com/ranujasanmir/pysimpqr',
      keywords=['qrcode', 'qr'],
      license='BSD',
      extras_require = {
        'PNG':  ["pypng>=0.0.13"],
      },
      classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.5',
        ],
      long_description=longdesc,
)

