from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='maksimka',
    version='0.0.1',
    description='Very useful thing',
    long_description=open('README.txt').read()+'\n\n'+open('CHANGELOG.txt').read(),
    url='',
    author='barashek',
    author_email='ffmarkov@yandex.ru',
    classifiers=classifiers,
    license='MIT',
    keywords='kod',
    packages=find_packages(),
    install_requiers=['']

)
