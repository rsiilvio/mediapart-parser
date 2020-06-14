from distutils.core import setup
setup(
    name='mediapart_bot_core',
    packages=['mediapart_bot_core'],
    version='1.0.0-beta.1',
    license='MIT',
    description='Provide tools to parser and download Mediapart articles as PDF.',
    author='Robin Perice',
    author_email='robin.perice@protonmail.com',
    url='https://github.com/r0perice/mediapart-bot-core',

    install_requires=[
          'feedparser',
          'beautifulsoup4',
          'requests',
      ],

    classifiers=[
    'Development Status :: 1.0.0-beta.1',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Website Parser',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],
    )