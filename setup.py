from setuptools import setup, find_packages
 
setup(
    name='bigvgan',
    version='0.1',
    description='Nvidia BigVGAN',
    packages=find_packages(),  # 自动发现和包含项目中的所有Python包
    install_requires=[
        'torch',
        'numpy',
        'scipy',
        'tensorboard',
        'soundfile',
        'pesq',
        'auraloss',
        'tqdm',
    ],
)