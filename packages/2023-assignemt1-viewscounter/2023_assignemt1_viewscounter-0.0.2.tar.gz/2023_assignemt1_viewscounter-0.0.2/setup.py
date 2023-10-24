from setuptools import setup, find_packages

with open("README.md", "r") as f:
      long_description = f.read()


setup(name='2023_assignemt1_viewscounter',
      version='0.0.2',
      description='This assignment focuses on creating an application that counts and monitors user views',
      author='Team CED',
      author_email='damianoficara@gmail.com,c.ricci19@campus.unimib.it,emiliotoli21@gmail.com',
      long_description=long_description,
      license='MIT',
      packages=["application", "database"],
      package_dir={
            "": ".",
            "application": "./application",
            "database": "./database",
      },
      zip_safe=False)
