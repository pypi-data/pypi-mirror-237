# Django Compiler

**django-compiler** is a Django package that provides a custom management command to compile Python files within a directory while allowing you to exclude specific directories from the compilation process.

## Features

- Easily compile Python files in your Django project.
- Exclude specific directories from compilation.
- Simple and user-friendly command-line interface.


## Solution
Django Client Whitelist provides a solution to this problem by allowing you to create a predefined list of client hosts that are allowed to access the API. With this middleware in place, you can be sure that only authorized hosts can request your API endpoints, making your application more secure.

## Installation
You can install **django-compiler** via pip:

```bash
pip install django-compiler
```
add `django_compiler` to your `INSTALLED_APPS`:

```python
# settings.py
INSTALLED_APPS = [
    # ...
    'django_compiler',
    # ...
]
```

## Usage

After installing the package, you can use the provided `compile` management command to compile Python files within your Django project. Here's how to use it:

```bash
python manage.py compile
```

## Options

`--exclude-dirs`: Specify one or more directories to exclude from the compilation. Use space-separated directory names. For example:

```bash
python manage.py compile --exclude-dirs dir1 dir2
```

This command will compile Python files within your Django project while excluding the specified directories.

## Contributing

If you'd like to contribute to this project, please follow these guidelines:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and ensure they are well-tested.
- Create a pull request to merge your changes into the main repository.

## License

[MIT](https://choosealicense.com/licenses/mit/)
