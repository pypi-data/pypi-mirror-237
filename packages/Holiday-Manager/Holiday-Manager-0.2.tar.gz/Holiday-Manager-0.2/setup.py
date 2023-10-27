from setuptools import setup, find_packages

setup(
    name='Holiday-Manager',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'requests',
        # Add other dependencies here
    ],
    author='Fluffik3666',
    author_email='sasha@fluffik.co.uk',
    description='A package for planning holidays',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
