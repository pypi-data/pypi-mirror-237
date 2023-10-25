import setuptools

def readme():
    try:
        with open('README.md') as f:
            return f.read()
    except IOError:
        return ''


setuptools.setup(
    name="uglysoup",
    version="1.2",
    author="PySimpleSoft",
    # author_email="PySimpleGUI@PySimpleGUI.org",
    # install_requires=['PySimpleGUI @ git+https://PySimpleGUI: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@github.com/PySimpleGUI/PSG5_Deploy.git#egg=PySimpleGUI&subdirectory=pip_psg', 'Pillow'],
    description="The best soup I know how to make",
    long_description=readme(),
    long_description_content_type="text/markdown",
    license='Free To Use But Restricted',
    # keywords="GUI UI PySimpleGUI tkinter psgresizer base64 resize",
    # url="https://github.com/PySimpleGUI",
    # packages=setuptools.find_packages(),
    packages=['uglysoup'],
    python_requires='>=3.6',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: Free To Use But Restricted",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Software Development :: User Interfaces",
    ],
    # package_data={"": ["*.ico", "LICENSE.txt", "README.md"]},
    entry_points={'gui_scripts': ['uglysoup=uglysoup.uglysoup:main_entry_point',],},
)