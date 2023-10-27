from setuptools import setup

setup(
    name='yav',
    version='1.0.1',
    description='yav- yet another venv management tool',
    author='niuguy',
    author_email='tf.wang.seu@gmail.com',
    packages=['yav'],
    entry_points={
        'console_scripts': ['yav=yav.main:main']
    },
)