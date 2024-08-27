from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='TransformerSum',
    version="0.0.1",
    description='Models to perform neural summarization (extractive and abstractive) using machine learning transformers and a tool to convert abstractive summarization datasets to the extractive task.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Hayden Housen',
    author_email='contact@haydenhousen.com',
    packages=find_packages(include=['TransformerSum']),
    install_requires=[
        'torch>=2.0.0',
        'scikit-learn>=1.2.0',
        'tensorboard',
        'spacy',
        'sphinx',
        'pyarrow',
        'pre-commit>=3.2.0',
        'pytorch_lightning==1.6.5',
        'transformers>=4.0.0',
        'torch_optimizer>=0.3.0',
        'wandb>=0.14.0',
        'rouge-score>=0.1.0',
        'packaging',
        'datasets>=2.0.0',
        'gradio>=3.0.0'
    ],
    entry_points={
        'console_scripts': ['transformersum = TransformerSum.main:main']
    },
    python_requires='>=3.10',
    license='GNU General Public License v3.0',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3.0",
        "Operating System :: OS Independent",
    ]
)