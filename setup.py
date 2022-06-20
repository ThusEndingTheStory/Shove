from setuptools import setup

setup(
    name='shove',
    version='1.0.0',    
    description='A database for python',
    url='https://github.com/ThusEndingTheStory/Shove',
    author='ThusEndingTheStory',
    author_email='',
    license='MIT License',
    packages=['shove'],
    install_requires=['sqlitedict', 'os'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: *',
    ],
)
