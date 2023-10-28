from setuptools import setup, find_packages

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
    name="xiaohuohumax-test",
    version="1.0.0",
    author="xiaohuohumax",
    description="no description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    license="MIT",
    keywords=[
        'xiaohuohumax',
        'test'
    ],
)
