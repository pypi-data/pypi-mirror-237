from setuptools import setup, find_packages


setup(
    name='ubicoders-vrobots-bridge',
    version='0.0.6',
    license='GPLv3',
    author="Elliot Lee",
    author_email='info@airnh.ca',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    url='https://github.com/ubicoders0/vrobots_bridge',
    keywords='ubicoders virtual robots',
    install_requires=[
          'asyncio',
          'websockets',
          'websocket-client',
          'flatbuffers',
          'flet',
          'pyperclip'
      ],
)