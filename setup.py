from setuptools import setup, find_packages
import subprocess

version = subprocess.check_output(["dpkg-parsechangelog", "--show-field", "Version"]).decode()

setup(
    name="vpngate-client",
    version=version,
    description="A client for discovering and connecting to vpngate.net OpenVPN servers.",


    author='Sami Jaktholm',
    author_email='sjakthol@outlook.com',

    keywords='vpn openvpn client',
    packages=find_packages(),
    scripts=["vpngate-client"]
)
