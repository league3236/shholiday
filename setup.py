import setuptools

setuptools.setup(
    name="shholiday",
    version="0.1",
    license='MIT',
    author="league3236",
    author_email="league3236@gmail.com",
    description="Check if the current date is a holiday in Korea.",
    long_description=open('README.md').read(),
    url="https://github.com/league3236/shholiday.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)