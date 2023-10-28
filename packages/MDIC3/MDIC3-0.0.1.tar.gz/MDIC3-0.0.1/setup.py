import setuptools
import os





setuptools.setup(
    # 包的分发名称，使用字母、数字、_、-
    name="MDIC3",
     # 版本号, 版本号规范：https://www.python.org/dev/peps/pep-0440/
    version="0.0.1",
    # 作者名
    author="Lyxiaotai",
     # 作者邮箱
    author_email="liuyi54894xiaotai@163.com",  
    # 包的简介描述,将传到网页上
    description="First lucky python package",   
    # 假如你的这个包有个介绍网站或者github之类的，就可以写上
    url='https://github.com/LYxiaotai/MDIC3',
     # 如果项目由多个文件组成，我们可以使用find_packages()自动发现所有包和子包，而不是手动列出每个包，在这种情况下，包列表将是example_pkg
    packages=setuptools.find_packages(),

)
