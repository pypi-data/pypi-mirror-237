from setuptools import setup, find_packages

setup(
    name             = 'imagestogif_js',
    version          = '1.0.0',
    description      = 'Test package for distribution',
    author           = 'Jadejung',
    author_email     = 'jungjade06@gmail.com',
    url              = 'https://github.com/jadejung06-sk/',
    download_url     = '',
    install_requires = ['pillow'],
	include_package_data=True,
	packages=find_packages(),
    keywords         = ['GIFCONVERTER', 'gifconverter', 'imagestogif', 'gif'],
    python_requires  = '>=3',
    zip_safe=False,
    classifiers      = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
) 