from setuptools import setup, find_packages

setup(
    name="ara-tools",
    version="0.1.4.7", # published is 0.1.4.6, local is 0.1.4.7
    packages=find_packages(),
    include_package_data=True,  # Add this line
    entry_points={
        "console_scripts": [
            "ara = ara_tools.__main__:cli",
        ],
    },
    install_requires=[
        # Add your package dependencies here
    ],
)
