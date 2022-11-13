import setuptools


with open("requirements.txt", "r", encoding="utf-8") as r:
    requires = [i.strip() for i in r]  # Зависимости

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()


setuptools.setup(
    name="aiogram_cache",
    version="0.1",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="alteralt",
    packages=setuptools.find_packages(),
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=requires,
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: Russian",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    project_urls={"Source": "https://github.com/alteralt/aiogram_cache"},
)