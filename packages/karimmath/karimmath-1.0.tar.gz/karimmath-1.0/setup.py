from setuptools import setup

setup(
    name='karimmath',
    version='1.0',
    py_modules=['karimmath'],
    install_requires=[
        'pyinputplus',
	'math',
    ],
    entry_points={
        'console_scripts': [
            'karimmath = karimmath:main'
        ]
    },
    description='Mathematical operations package',
    author='karimjaballah',
    author_email='shellcloud18@gmail.com',    
)
