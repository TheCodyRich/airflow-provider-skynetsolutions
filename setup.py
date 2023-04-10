from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

__version__ = "1.0.0"

setuptools.setup(
    name="airflow-provider-thecodyrich",
    version=thecodyrich_provider.__version__,
    author="TheCodyRich",
    license="Apache License 2.0",
    description="An Apache Airflow provider for using unofficial APIS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points="""
        [apache_airflow_provider]
        provider_info=thecodyrich_provider.__init__:get_provider_info
    """,
    url="https://github.com/TheCodyRich/airflow-provider-thecodyrich",
    install_requires=[
        "apache-airflow>=2.0",
        "openai>=0.27.4"
    ],
    packages=find_packages(exclude=["*tests.*", "*tests"]),
    python_requires=">=3.8",
)
