from setuptools import setup, find_packages

setup(
    name='InstantlyEscrow',
    packages=find_packages(),
    version='0.0.7',
    url='https://github.com/clockwrks/Instantly-Escrow-Crypto',
    author='aruseni',
    author_email='aruseni.magiku@gmail.com',
    description='Simple Python package that can generate wallets for several cryptocurrencies',
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    install_requires=[
        'ecdsa==0.13',
    ],
    dependency_links=[
        'https://github.com/IsThisThePayneResidence/pyethereum/tarball/master',
    ],
)
