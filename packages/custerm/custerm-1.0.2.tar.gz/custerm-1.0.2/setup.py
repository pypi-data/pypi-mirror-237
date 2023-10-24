from setuptools import setup, find_packages

setup(
    name='custerm',
    version='1.0.2',
    description='A custom terminal library with rich markdown support.',
    author='cxstles',
    author_email='bio@fbi.ac',
    url='https://github.com/cxstles/custerm',
    packages=find_packages(include=['custerm*']),
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    long_description=open('docs.md').read(),
    long_description_content_type='text/markdown',
)
