from setuptools import setup, find_packages
with open('./README.md', 'r') as f:
    long_description = f.read()

setup(
    name='modulairy-redirect-app',
    version='0.0.7',
    packages=['modulairy_redirect_app'],
    install_requires=[
        'Flask',
        'gunicorn'
    ],
    author='Fatih Mehmet ARSLAN',
    author_email='contact@fmarslan.com',
    description='Modulairy Redirect App is a flexible Flask-based redirection application that dynamically redirects incoming HTTP requests based on environment variables prefixed with TARGET_.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/modulairy/modulairy-redirect-app',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
