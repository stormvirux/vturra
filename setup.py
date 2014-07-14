from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import vturra
import sys
import codecs
try:
	codecs.lookup('mbcs')
except LookupError:
	ascii = codecs.lookup('ascii')
	func = lambda name, enc=ascii: {True: enc}.get(name=='mbcs')
	codecs.register(func) 

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(name="vturra",
    version=vturra.__version__,
    license='MIT Software License',
    tests_require=['pytest'],
    install_requires=[
                      'mechanize',
                      'patsy',
                      'BeautifulSoup4',
                      'numpy',
                      'scipy',
                      'matplotlib>=1.2.1',
                      'pandas<0.13'
                     ],
    cmdclass={'test': PyTest},
    description="Downloads results from VTU website and analyzes the result",
    long_description=open('README.md').read(),
    author="Muhammed Thaha",
    author_email='mthaha1989@gmail.com',
    download_url='https://github.com/stormvirux/vturra',
    packages=find_packages(exclude='tests'),
    package_data={'vturra': ['data/*.xml']},
    include_package_data=True,
    platforms='any',
    test_suite='vturra.test.test_vturra',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: English',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Information Analysis'
        ],
    extras_require={
        'testing': ['pytest'],
    },
    entry_points={
        "console_scripts": [
            "vturra=vturra.rra:main"
            #"pip%s=pip:main" % sys.version[:1],
            #"pip%s=pip:main" % sys.version[:3],
        ],
    }
)

