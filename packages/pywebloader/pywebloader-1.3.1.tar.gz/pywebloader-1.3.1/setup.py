from setuptools import setup


setup(
    name='pywebloader',

    packages=['pywebloader'],

    version='1.3.1',

    license='MIT',

    description='Improves work with web files downloading.',

    long_description_content_type='text/x-rst',
    long_description=open('README.rst', 'r').read(),

    author='Ivan Perzhinsky.',
    author_email='name1not1found.com@gmail.com',

    url='https://github.com/xzripper/PyLoader',
    download_url='https://github.com/xzripper/PyLoader/archive/refs/tags/v1.3.1.tar.gz',

    keywords=['utility'],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ]
)
