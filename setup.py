import setuptools

with open("README.md", "r") as fh:
    complete_readme = fh.read()
    long_description = complete_readme.split("**System image")[0]
    long_description += "\n\n**Made by Help-a-Sloth org. Check us on GitHub.**"


setuptools.setup(
    name="mischief-managed", 
    packages=setuptools.find_packages(),
    version="1.0.0",
    author="Hemant Singh",
    keywords=["Quick Work" , "Productivity" , "Automation", "Cleanup"
              "Files" , "Management" , "Tidy" , "Folder Manage"],
    description=("Files outside any folder are "+
                "made tidy/managed by putting inside folder based on "+
                "their extension or date"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Help-a-Sloth/mischief-managed",
    maintainer="amifunny",
    entry_points={
        'console_scripts':[
            'mischief-managed=mischief_managed.__main__:main'
        ]
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ]

)