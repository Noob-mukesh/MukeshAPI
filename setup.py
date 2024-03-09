from setuptools import setup,find_packages
with open("README.md", encoding="utf8") as readme:
    long_desc = readme.read()
VERSION="0.0.1"

# Setting up
setup(
    name="mukeshapi",
    version=VERSION,
    author="Mukesh | noob-mukesh",
    author_email="<mail@itzcodermukesh@gamil.com>",
    description="python api hub |mukesh-api",
    long_description_content_type="text/markdown",
    long_description=long_desc,
    packages=find_packages(),
    install_requires=["pytz>=2023.3"],
    keywords=['python', "mukesh-api","flask"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    keywords="python api for telegram bot apihub telegram fastapi flask",
    project_urls={
        "Tracker": "https://github.com/noob-mukesh/API-HUB/issues",
        "Community": "https://t.me/MR_SUKKUN",
        "Source": "https://github.com/noob-mukesh/API-HUB",
    },
    python_requires="~=3.7",
)