from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='offical_django_tutorial',
    version='0.1.0',
    author="Kevin Beirne",
    description='Django Tutorial from offical Django website',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['mysite'],
    url='https://github.com/kevinbeirne1/django_tutorial',
    license='MIT',
    author_email='####@example.com',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
