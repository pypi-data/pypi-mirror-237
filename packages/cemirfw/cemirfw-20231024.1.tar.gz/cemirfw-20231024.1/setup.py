from setuptools import setup
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cemirfw',
    version='20231024.1',
    description='AllInOne Framework for Python/PyPy',
    author='MusluY.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author_email='musluyuksektepe@gmail.com',
    url='https://github.com/muslu/cemirfw',
    packages=['cemirfw'],
    install_requires=['tornado'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
