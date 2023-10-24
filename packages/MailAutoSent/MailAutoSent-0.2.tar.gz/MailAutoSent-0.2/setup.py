from setuptools import setup

setup(
    name='MailAutoSent',
    version='0.2',
    packages=['MailAutoSent'],
    author='Wanggsh',
    author_email='wanggsh98@qq.com',
    description='Auto sent Mail',
    url='https://github.com/GuangShuaiWang/MailAutoSent',
    install_requires=[
        'yagmail==0.15.293',
    ],
)