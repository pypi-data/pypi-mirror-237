from setuptools import setup, find_packages

setup(
    name="user_MTM",
    version="1.0.0",
    description="Modulo di test utente per l'accesso al database mysql",
    author="MTM_group",
    packages=find_packages(),
    install_requires=[
        "mysql-connector-python",
    ],
)
