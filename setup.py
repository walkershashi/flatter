from setuptools import setup

packages = find_packages(
    exclude=('doc', 'dist', 'build', 'fslpy.egg-info', 'tests')
)

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'requirements.txt'), 'rt') as f:
    install_requires = [l.strip() for l in f.readlines()]

setup(
    name = "flatter",
    version = "0.0.1",
    description = "Retuns the dataframe for the dictionary",
    packages = packages,
    install_requires = install_requires,
    license = "MIT",
    url = "https://github.com/walkershashi/samplePythonPackage"
)