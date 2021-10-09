from setuptools import setup

with open("README.md", "r") as f:
    readmetext = f.read()

if __name__ == "__main__":
    setup(
        long_description=readmetext,
        long_description_content_type="text/markdown"
    )