from setuptools import setup
setup(
    name='mediapart_parser',
    packages=['mediapart_parser'],
    version='1.0.0-beta.2',
    license='MIT',
    description='Provide tools to parse and download Mediapart articles as PDF.',
    author='Robin Perice',
    author_email='robin.perice@protonmail.com',
    url='https://github.com/r0perice/mediapart-parser',
    download_url='https://github.com/r0perice/mediapart-parser/archive/1.0.0-beta.2.tar.gz',
    install_requires=[
          'feedparser',
          'beautifulsoup4',
          'requests',
      ],

)