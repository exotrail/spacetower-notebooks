from setuptools import setup, find_packages

setup(
    name="spacetower-notebooks",
    version="1.2.0",
    description="Python Notebooks for FDS workflows",
    author="Exotrail",
    author_email="",
    url="https://github.com/exotrail/spacetower-notebooks",
    license="MIT",
    keywords=["FDS", "API", "Exotrail"],
    packages=find_packages(),
    install_requires=[
        "pandas>=2.2.2",
        "matplotlib>=3.9.0",
        "plotly>=5.22.0",
        "spacetrack>=1.3.0",
        "notebook>=7.2.0",
        "spacetower-fds-sdk>=1.2.0"
    ],
    extras_require={
        "dev": [
            "pytest>=7.2.1"
        ]
    },
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
