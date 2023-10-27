from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='service-Rabbit-thread',
    version='0.0.5.post3',
    license='MIT License',
    author='Eliézer Schwartz',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='eliezer.mail090@gmail.com',
    keywords='rabbit',
    description=u'Wrapper não oficial do Rabbit',
    packages=['service-Rabbit-thread'],
    install_requires=['pika'],)