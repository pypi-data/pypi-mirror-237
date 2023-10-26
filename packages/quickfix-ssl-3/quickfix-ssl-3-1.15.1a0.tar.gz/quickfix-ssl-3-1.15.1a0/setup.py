from distutils.core import setup
from distutils.core import Extension
from distutils.sysconfig import get_config_vars

import glob

# Remove the "-Wstrict-prototypes" compiler option, which isn't valid for C++.
import distutils.sysconfig

cfg_vars = dict(distutils.sysconfig.get_config_vars())
for key, value in cfg_vars.items():
    if isinstance(value, str):
        cfg_vars[key] = value.replace("-Wstrict-prototypes", "")

long_description = ''
with open('LICENSE') as file:
    license_file = file.read()


setup(name='quickfix-ssl-3',
      version='1.15.1a',
      python_requires='==3.9.*',
      py_modules=['quickfix', 'quickfixt11', 'quickfix40', 'quickfix41', 'quickfix42', 'quickfix43', 'quickfix44',
                  'quickfix50', 'quickfix50sp1', 'quickfix50sp2'],
      data_files=[('share/quickfix', glob.glob('spec/FIX*.xml'))],
      author='Oren Miller',
      author_email='oren@quickfixengine.org',
      maintainer='Oren Miller',
      maintainer_email='oren@quickfixengine.org',
      description="FIX (Financial Information eXchange) protocol implementation",
      url='https://www.quickfixengine.org',
      download_url='https://www.quickfixengine.org',
      license=license_file,
      include_dirs=['C++'],
      ext_modules=[Extension('_quickfix', glob.glob('C++/*.cpp'),
                             extra_compile_args=['-std=c++0x', '-Wno-deprecated', '-Wno-unused-variable',
                                                 '-Wno-deprecated-declarations', '-Wno-maybe-uninitialized'])],
      )
