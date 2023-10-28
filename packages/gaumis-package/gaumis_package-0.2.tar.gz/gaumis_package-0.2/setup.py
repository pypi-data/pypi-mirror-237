from setuptools import setup, find_packages

setup(
    name='gaumis_package',
    version='0.2',
    description='A package for doing cool things',
    author='Kumar Gaurav',
    author_email='kumargaurav1527@gmail.com',
    url='https://github.com/Gaumis/gaumis_package.git',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=[
        # Add any dependencies your package requires here
    ],
)
