from setuptools import setup, find_packages

setup(
    name="strada",
    version="0.1.24",
    packages=find_packages(),
    install_requires=[
        "jsonschema",
        "openai",
        "google-api-python-client",
        "google-auth",
        "oauth2client",
        "google-auth-oauthlib",
        "google-auth-httplib2",
        "requests",
    ],
    author="Strada",
    description="Strada SDK",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
