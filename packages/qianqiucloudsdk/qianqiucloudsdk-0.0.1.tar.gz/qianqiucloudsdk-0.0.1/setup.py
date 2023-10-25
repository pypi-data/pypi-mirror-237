from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Qianqiu Cloud SDK'

setup(
    name="qianqiucloudsdk",
    version=VERSION,
    author="qianqiusoft",
    author_email="develop@qianqiusoft.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['PyMySQL'],
    license="MIT",
    url="https://github.com/chunleili/cut_video",
    scripts=['db/mysql/mysql.py', 'db/iot/iot.py'],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows"
    ]
)