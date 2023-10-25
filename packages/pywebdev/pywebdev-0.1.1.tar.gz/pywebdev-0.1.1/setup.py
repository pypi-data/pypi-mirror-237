from setuptools import setup, find_packages

# Informações sobre o projeto
NAME = "pywebdev"
DESCRIPTION = "Biblioteca de Desenvolvimento Web Python - Um kit abrangente para criar aplicativos da web de alto desempenho."
AUTHOR = "icarogamer2001"

# Versão do projeto
VERSION = "0.1.1"

# Configuração do setup
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires='>=3.1',  # Requer Python 3.1 ou superior
)
