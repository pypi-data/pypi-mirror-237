import os
import easyvenv as ev

project_dir = os.path.dirname(__file__)
publish = True

if not publish:
    ev.easyvenv(project_dir)
else:
    package_dir = ev.create_package("SMTinker", "1.3", project_dir)
    ev.publish_package(package_dir, "pypi-AgEIcHlwaS5vcmcCJDJmZTBjOWNmLWE5NzAtNGM2ZS1hMjg2LTVmNjFhMGZmZjRhYgACKlszLCI0YjgwNzdmYi04ZGU5LTQyZGItOGZjZC1mZTcwYmJlMDUyNDkiXQAABiD2yesyTn5-IoDMGWrQNNL47K97CGHGhjz_3p5NNc6KSA")
