from setuptools import setup, find_packages

setup(
    name="vitirover",
    version="0.1.5",
    packages=find_packages(),
    install_requires=[
        'pygame',
        'protobuf',
        'telemetry_pb2',
    ],
    author="Jorand Gallou",
    author_email="info@vitirover.com",
    description="Commande du robot Vitirover avec le clavier.",
    license="MIT",
    keywords="vitirover robot control pygame",
    url="https://github.com/votreusername/vitirover",
)
