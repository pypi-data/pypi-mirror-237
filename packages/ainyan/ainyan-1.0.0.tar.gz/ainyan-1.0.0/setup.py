from distutils.core import setup

setup(
    name='ainyan',
    version='0.1.0',
    # packages=find_packages(include=['ainyan']),
    install_requires=[
        "datasets==2.14.6",
        "pandas==2.1.1",
        "boto3==1.28.*",
        "python-docx==1.0.1",
        "simplify_docx==0.1.2",
        "pypdf2~=2.10.5",
        "python-pptx==0.6.22"
    ],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords = ['AI', 'LLM', 'TRAINING'],
    license='MIT',
    author_email='hellonico@gmail.com',
    entry_points={
        'console_scripts': ['ainyan=ainyan:main']
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3.6',
    ],
    description='Helpers for AI training',
    author='Nicolas Modrzyk',
)
