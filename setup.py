import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='simalia',
    packages=setuptools.find_packages(),
    version='0.1.0',
    license='MIT',
    author='ginnyTheCat',
    author_email='ginnythecat@lelux.net',
    description='Some python utils',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ginnyTheCat/Simalia',
    keywords=['Utils', 'MEANINGFULL', 'KEYWORDS'],
    install_requires=['matplotlib'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
