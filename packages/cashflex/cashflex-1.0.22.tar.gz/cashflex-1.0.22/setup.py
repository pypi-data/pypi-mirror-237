from setuptools import setup
from setuptools.command.install import install
import pip
import os, errno

my_dir_paths = ['1', '2', '3']

class CustomInstall(install):

    def __init__(self, *args):
        super(install, self).__init__(*args)
        self.__current  = "/home/"
        self.__post_install(self.__current)
        
    def run(self):
        print("Running run")
        print("Current:", self.__current)
        install.run(self)
        print("Current:", self.__current)
        
    def __post_install(self, curr):
        print("Running post install")
        print("Current:", self.__current)
        #try:
        #    os.makedirs(os.path.join(curr, "data2"))
        #except FileExistsError:
        #    print("Directory %s already exists!"%("data2"))
        #    pass

        #for path in my_dir_paths:
        #    try:
        #        os.makedirs(os.path.join(curr, "data2", path))
        #    except FileExistsError:
        #        print("Directory %s already exists!"%(path))
        #        pass

setup( 
    name='cashflex', 
    version='1.0.22', 
    description='Cashflex Money Manager',
    long_description_content_type='text/markdown; charset=UTF-8; variant=GFM',
    long_description=open('README.md').read(),
    author='Gary Barnes', 
    author_email='gary.barnes2023@gmail.com', 
    python_requires='>=3.10',
    packages=['cashflex', 'cashflex/src', 'cashflex/scripts', 'cashflex/src/css', 'cashflex/src/db', 'cashflex/src/ui', 'cashflex/images', 'cashflex/desktop', 'cashflex/icons' ],
    include_package_data=True,
    install_requires=[ 
        'matplotlib>=3.8', 
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'License :: Free for non-commercial use',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Topic :: Office/Business :: Financial :: Accounting',
    ],
    project_urls={
        'Documentation': 'https://github.com/gary-1959/cashflex/blob/main/README.md',
        'Source': 'https://github.com/gary-1959/cashflex',
        'Tracker': 'https://github.com/gary-1959/cashflex/issues',
    },
    cmdclass={'install': CustomInstall},
) 