from setuptools import setup

setup(
    name="DTLhelpTool_Python",
    version="1.313.0",
    packages=["DTLhelper"],
install_requires = [
    'requests>=2.0.0',  # requests 라이브러리, 최소 버전 2.0.0 이상
    'pycryptodome>=3.0.0',  # Cryptodome 라이브러리, 최소 버전 3.0.0 이상
    'pywin32>=300',
    'pycryptodomex',  # pywin32 라이브러리, 최소 버전 300 이상
],
)