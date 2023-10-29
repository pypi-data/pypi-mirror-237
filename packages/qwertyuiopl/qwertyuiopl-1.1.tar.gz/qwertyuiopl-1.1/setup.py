from setuptools import setup, find_packages


with open('README.md', encoding="utf-8") as f:
  long_description = f.read()


setup(
  name='qwertyuiopl',
  version='1.1',
  author='tosterLIKE',
  author_email='090504opo@gmail.com',
  description='Тест',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/xllebbSQ/aiopayAPI',
  packages=find_packages(),
  install_requires=['aiohttp>=3.8.5',
                    "asyncio>=3.4.3",
                    "typing>=3.7.4",
                    "pydantic>=1.8.2"],
  classifiers=[
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  python_requires='>=3.8'
)