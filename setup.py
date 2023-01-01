from setuptools import setup, find_packages
import io

with io.open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='qsnctf',
    version='0.0.6',
    install_requires=['PyExecJS', 'python3base92', 'pybase62'],
    packages=find_packages(),
    include_package_data=True,
    package_data={'qsnctf': ['plugin/*']},
    url='https://github.com/Moxin1044/qsnctf-python',
    license='MIT License',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Moxin',
    author_email='1044631097@qq.com',
    description='青少年CTF训练平台提供的Python软件包'
)
