from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(
    name = 'filesystempro',
    version = '0.0.0.0',
    url = 'https://github.com/hbisneto/FileSystemPro',
    license = 'MIT License',
    
    author = 'Heitor Bisneto',
    author_email = 'heitor.bardemaker@live.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    description = u'FileSystem is designed to identify the operating system (OS) on which it`s running and define the paths to various user directories based on the OS.',
    install_requires = [''],
    long_description = readme,
    long_description_content_type = "text/markdown",
    keywords = ['FileSystem', 'Linux', 'macOS', 'Windows', 'File', 'System'],
    packages = ['filesystem', 'filesystem/wrapper'],
    platforms = 'any',
    python_requires= '>=3.9',
)