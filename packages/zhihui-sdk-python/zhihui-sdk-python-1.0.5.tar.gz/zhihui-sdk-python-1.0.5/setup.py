from setuptools import setup, find_packages

setup(
    name='zhihui-sdk-python',
    version='1.0.5',
    author='samjinli',
    author_email='samjinli@tencent.com',
    description='智绘设计SDK-Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/xrdpcg/zhihui-sdk-python',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],  
    keywords='',
    install_requires=[
      'requests',
    ],
    python_requires='>=3.6',
)