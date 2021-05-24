import setuptools

setuptools.setup(
    name="mulgyeol-bot-framework",
    version="0.0.1",
    author="Mycroft Kang",
    author_email="thkang0629@gmail.com",
    description="Mulgyeol Bot Framework",
    packages=["MGBotBuilder"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.7",
)
