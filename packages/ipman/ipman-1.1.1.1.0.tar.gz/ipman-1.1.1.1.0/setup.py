#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
  name = 'ipman',  
  package_dir={'ipman': 'ipman'},
  package_data={'ipman': ['ipman.py','errors.py', 'iptoolz.py']},
              version = '1.1.1.1.0',
  license='MIT',    
  description = 'ipman is a high-level core python package for Internet Protocol(IP) manipulations.',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Mobolaji Abdulsalam',                   
  author_email = 'ibraheemabdulsalam@gmail.com',
  url = 'https://github.com/moriire/ipman',  
  download_url = 'https://github.com/moriire/ipman/archive/v_110.tar.gz',
  keywords = ['IPMan is a high-level core python package for Internet Protocol(IP) manipulations.'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3.10',
  ],
   python_requires='>=3.10',
)
