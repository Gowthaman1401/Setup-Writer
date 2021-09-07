import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='setup_writer',
    packages=setuptools.find_packages(),
    version='1.2.1',
    license='Apache License, Version 2.0',
    description='To Help In Writing setup.py File And Upload Package To Pip',
    author='Gowthaman',
    author_email='rgngowthaman1@gmail.com',
    url='https://github.com/Gowthaman1401/Setup-Writer',
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.6',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.6'
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    install_requires=[
         "colorama",
    ],
    entry_points={'console_scripts': ['pip-setup=setup_writer.__main__:main', 'pip-upload=setup_writer.__main__:upload_main']}
)
