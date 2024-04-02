from setuptools import setup, find_packages

setup(
    name='ghutils',
    version='0.4.1',
    description="Collection of various GitHub-related git remote repository server helper utilities",
    author='Thanatisia',
    author_email='55834101+Thanatisia@users.noreply.github.com',
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        # List your dependencies here
        "requests",
    ],
    url='https://github.com/Thanatisia/gh-utils',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    entry_points = {
        # Program Entry Point(s) and scripts
        'console_scripts' : [
            'gh-clone = ghutils.ghclone:main',
            'gh-retrieve = ghutils.ghretrieve:main',
        ],
    },
)

