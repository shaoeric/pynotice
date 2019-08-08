from setuptools import setup

setup(
    name='pyprompt',
    version='0.0.1',
    author='shaoeric',
    author_email='shaoeric@foxmail.com',
    url='https://zhuanlan.zhihu.com/p/26159930',
    description=u'吃枣药丸',
    packages=['jujube_pill'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'jujube=jujube_pill:jujube',
            'pill=jujube_pill:pill'
        ]
    }
)