from setuptools import setup, find_namespace_packages
import io

with io.open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='qsnctf',
    version='0.0.10',
    python_requires='>=3.9',
    install_requires=['base58', 'requests', 'bs4', 'urllib3', 'rarfile', 'sympy'],
    extras_require={
        'js': ['exejs'],  # 可选: jsfuck_decode 等需要 JS eval 的少数功能
    },
    packages=find_namespace_packages(include=['qsnctf', 'qsnctf.*']),
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
