from setuptools import setup, find_packages

setup(
    name="SMTinker",
    version="1.6",
    packages=find_packages(),
    package_data={'package_name': ['resources/*']},
    scripts=['SMTinker\\scripts\\smtinker.py'],
    install_requires=['easyvenv==1.8', 'twine', 'pillow']
)
