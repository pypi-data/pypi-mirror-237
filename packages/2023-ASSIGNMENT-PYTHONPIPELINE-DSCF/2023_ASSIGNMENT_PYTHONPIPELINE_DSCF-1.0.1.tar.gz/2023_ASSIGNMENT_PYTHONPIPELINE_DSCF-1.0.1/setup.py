from setuptools import setup, find_packages

setup(
    name = '2023_ASSIGNMENT_PYTHONPIPELINE_DSCF',
    version = '1.0.1',
    packages=find_packages(),
    install_requires=[
        # Lista delle dipendenze del tuo progetto
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'nome-comando=modulo:funzione',
        ],
    },
    author=['Daniel Satriano','Francesco Cavallini'],
    description='Progetto pipeline GitLab',
    url='https://gitlab.com/processo-e-sviluppo-software/2023_assignment1_PythonPipeline.git',
)