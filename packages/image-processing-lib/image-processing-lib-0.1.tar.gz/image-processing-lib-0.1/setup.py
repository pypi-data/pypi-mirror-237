from setuptools import setup, find_packages

setup(
    name='image-processing-lib',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'opencv-python',
        'matplotlib'
    ],
    author='Elliot Cole',
    author_email='coleelliot2001@gmail.com',
    description='This Python module provides utility functions for various image processing tasks, such as image conversion, display, normalization, and enhancement. It leverages the power of libraries like cv2 and numpy to handle and manipulate image data.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/votre_nom_utilisateur/image-processing-lib',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)