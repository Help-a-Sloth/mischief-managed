import setuptools

setuptools.setup(
    name="mischeif-managed", 
    version="1.0.0",
    author="Hemant Singh",
    keywords=["Quick Work" , "Productivity" , "Automation", "Cleanup"
              "Files" , "Management" , "Tidy" , "Folder Manage"],
    description=("Files outside any folder are "+
                "made tidy/managed by putting inside folder based on "+
                "their extension or date"),
    long_description_content_type="text/markdown",
    url="https://github.com/amifunny/mischeif-managed/",
    maintainer="amifunny",
    entry_points={
        'console_scripts':[
            'mischeif-managed=mischeif_managed.__main__:main'
        ]
    },
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]

)