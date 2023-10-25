from setuptools import setup, find_packages

setup(
    name='automagicio',
    version='1.0.0',
    description='A versatile plugin module for streamlining input/output operations in Python projects.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Ishan Oshada',
    author_email='ic31908@gamil.com',
    url='https://github.com/ishanoshada/automagicio',
    packages=find_packages(),
    keywords=['auto', 'magic', 'io', 'file handling', 'data transformation'],  
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
