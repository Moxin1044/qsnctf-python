from setuptools import setup
import io

with io.open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='qsnctf',
    version='0.0.2',
    install_requires=['PyExecJS'],
    packages=['qsnctf'],
    url='https://github.com/Moxin1044/qsnctf-python',
    license='MIT License',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Moxin',
    author_email='1044631097@qq.com',
    description='青少年CTF训练平台提供的Python软件包'
)
