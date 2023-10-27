import setuptools
import os
import re

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            tem=os.path.join(path, filename)
            tem=re.sub('GDmicro/','',tem)
            paths.append(tem)
    return paths

path=package_files("GDmicro/higra")
path.append("feature_select_model_nodirect.R")
path.append("feature_select_model.R")
path.append("norm_features.R")
path.append("parameters.yaml")
path.append("allmeta.tsv")
path.append("higra.libs/libtbb-d697f7e9.so.2")
#print(path)
#exit()


setuptools.setup(
    name="gdmicro",
    version="1.0.9",
    author="Liao Herui",
    author_email="heruiliao2-c@my.cityu.edu.hk",
    description="GDmicro - Use GCN and Deep adaptation network to classify host disease status based on human gut microbiome data",
    long_description="GDmicro takes microbial compositional abundance data as input, then it can classify disease status for your test samples, return disease-related microbes (potential biomarkers), and return the microbes' contribution to the hosts' disease status.",
    long_description_content_type="text/markdown",
    url="https://github.com/liaoherui/GDmicro",
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=True,
    #package_data={"GDmicro":["feature_select_model_nodirect.R","feature_select_model.R","norm_features.R","parameters.yaml","higra.libs/libtbb-d697f7e9.so.2"]},
    package_data={"GDmicro":path},
    install_requires=[
    "numpy==1.17.3",
    "pandas==1.0.1",
    "scipy==1.5.2",
    "scikit-learn==1.0.2",
    "torch==1.12.0",
    "networkx==2.4",
    "matplotlib==3.1.2",
    "ipython"
    ],
    entry_points={
        'console_scripts':[
        "gdmicro = GDmicro.GDmicro:main",
        ]
    },
    python_requires='~=3.7',
    classifiers=[
    'Programming Language :: Python :: 3.7',
    ],
)
