from setuptools import setup, find_packages

setup(
    name="wildfire_evac",
    version="0.0.9",
    author='Celtics Big 3',
    author_email='clpondoc@stanford.edu',
    description='An RL OpenAI Gym Environment for Wildfire Evacuation',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires = ["numpy==1.21.6", "pytest==7.4.0", "scipy==1.11.3", "torch==2.1.0", "gymnasium==0.29.1", "pygame==2.5.2"]
)
