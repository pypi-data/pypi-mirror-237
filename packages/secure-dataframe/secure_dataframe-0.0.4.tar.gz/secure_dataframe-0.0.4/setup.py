from distutils.core import setup

REQUIRED_PACKAGES = [
    "pandas>=1.3.5"
]


setup(
    name='secure_dataframe',  # How you named your package folder (MyLib)
    packages=['secure_dataframe'],  # Chose the same as "name"
    version='0.0.4',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='A way to secure and filter dataframe on pandas',  # Give a short description about your library
    author='Pedro Pinho',  # Type in your name
    author_email='pepeupepeo@gmail.com',  # Type in your E-Mail
    url='https://github.com/Grayfados/SecureDataframe',  # Provide either the link to your github or to your website
    download_url="https://github.com/Grayfados/SecureDataframe/archive/refs/tags/v0.0.2.tar.gz",
    install_requires=REQUIRED_PACKAGES,
    classifiers=[
        'Development Status :: 3 - Alpha',  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Environment :: Plugins',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
