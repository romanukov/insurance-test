from setuptools import setup, find_packages


setup(
    name='insurance-test',
    version='1.0.0',
    description='Test work',
    long_description='Test work for python team on FastAPI and Tortoise',
    long_description_content_type='text/plain',
    packages=find_packages(),
    python_requires='>=3.7.0<3.8',
    install_requires=[
        'fastapi>=0.61<0.62',
        'pydantic>=1.6.1<1.7',
        'tortoise-orm>=0.16.14<0.17',
        'uvicorn>=0.11.8<0.12',
        'python-dotenv>=0.14.0<0.15',
    ],
    extras_require=dict(
        dev=[
            'invoke>=1.3,<1.4',
        ],
    ),
)
