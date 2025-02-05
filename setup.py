from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    description = fh.read()

setup(
    name="dotplotter",
    version="1.0.1",
    author="Thomas J. Booth",
    author_email="thoboo@biosustain.dtu.dk",
    packages=find_packages(),
    description="A python for plotting dot plots from blast results.",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/DrBoothTJ/dotplotter",
    license='GNU General Public License v3.0',
    python_requires='>=3.7',
    install_requires=['matplotlib'],
    entry_points={'console_scripts': ["dotplotter=dotplotter.main:main"]}
)
