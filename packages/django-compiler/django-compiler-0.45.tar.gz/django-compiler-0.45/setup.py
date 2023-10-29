from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name='django-compiler',
    version='0.45',
    packages=find_packages(),
    python_requires='>=3.10',
    install_requires=[
        'Django>=4.1.4',
    ],
    license='MIT',
    description='A Django app for compiling Python files',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/S-Amine/django-compiler',
    author='S-Amine',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 4.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
