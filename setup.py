from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='mkdocs-word-filter',
    version='0.1.1',
    description='A MkDocs plugin to filter extra content that was to markdown documents for e.g. formatting docx files.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='mkdocs markdown word filter',
    url='https://github.com/miikama/mkdocs-word-filter',
    author='Miika Mäkelä',
    author_email='makelanmiika@gmail.com',
    license='MIT',
    python_requires='>=3.5',
    install_requires=[
        'mkdocs',
    ],
    classifiers=[                
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',        
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'mkdocs-word-filter=mkdocs_word_filter.plugin:ContentFilterPlugin',
        ]
    }
)