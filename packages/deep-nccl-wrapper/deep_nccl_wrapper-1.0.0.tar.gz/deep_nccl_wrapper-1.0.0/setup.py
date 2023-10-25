#
# Copyright (C) Alibaba Cloud Ltd. 2021-2022.  ALL RIGHTS RESERVED.
#
import sys
import os
import shutil
import time
import platform
import atexit

#import torch
#from torch.utils import cpp_extension
#from Cython.Build import cythonize
from setuptools import setup, Extension, find_packages
from wheel.bdist_wheel import bdist_wheel
from setuptools.command.build_ext import build_ext
from setuptools.command.install import install

deep_nccl_version = "1.0.0"

package_name = "deep_nccl_wrapper"
total_packages = [
    "deep_nccl_wrapper"
]

def _post_install():
    os.system('ldconfig')

class post_install(install):
    def run(self):
        install.run(self)
        atexit.register(_post_install)

setup(
    name=package_name,
    version=f"{deep_nccl_version}",
    description=("Deep-NCCL is an AI-Accelerator communication framework for NVIDIA-NCCL. "\
                 "It implements optimized all-reduce, all-gather, reduce, broadcast, reduce-scatter, all-to-all," \
                 "as well as any send/receive based communication pattern." \
                 "It has been optimized to achieve high bandwidth on aliyun machines using PCIe, NVLink, NVswitch," \
                 "as well as networking using InfiniBand Verbs, eRDMA or TCP/IP sockets."),
    author="Alibaba Cloud",
    author_email="ziqi.yzq@alibaba-inc.com",
    license="Copyright (C) Alibaba Group Holding Limited",
    keywords="Distributed, Deep Learning, Communication, NCCL, AIACC, DEEPNCCL",
    url="https://help.aliyun.com/document_detail/462422.html?spm=a2c4g.462031.0.0.c5f96b4drcx52F",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    packages=total_packages,
    #package_data={package_name: ['aiacc/']},
    #include_package_data=True,
    #data_files=[("aiacc/nccl/", ["aiacc/aiacc.so"])],
    # ext_modules=aiacc_ext_modules,
    # scripts=['aiacc_bind'],
    cmdclass={
      'install': post_install
    },
    install_requires=[
      'deepnccl',
    ],
    python_requires=">=3.0",
)
