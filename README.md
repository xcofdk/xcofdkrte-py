<!-- ---------------------------------------------------------------------------
File        : README.md
Copyright(c) 2023-2026 Farzad Safa (farzad.safa@xcofdk.com)

This file is distributed under the same license provided through the SOFTWARE it is part of.
A copy of the license file can also be obtained following the link below:
    https://github.com/xcofdk/xcofdkrte-py/blob/master/LICENSE.txt
------------------------------------------------------------------------------->


# Project Description

**XCOFDK** is the architecture of an e**X**tensible, **C**ustomizable and **O**bject-oriented **F**ramework 
**D**evelopment **K**it.

This project presents an implementation of the <u>backend package</u> of XCOFDK for Python through the PyPI package 
[xcofdk-rte](https://pypi.org/project/xcofdk-rte/). <br> 
The backend is responsible for providing both the public API and the (default) functional scope of the runtime 
environment (RTE) of the framework to authorized frontend packages of XCOFDK, so the RTE is available to user programs 
which use a frontend of the framework.

For more information refer to the default frontend package [xcofdk](https://pypi.org/project/xcofdk/).

<br>


# Installation

XCOFDK is available for **Python versions 3.11+** on both POSIX and Windows platfroms.

> **NOTE:** <br>
> - By installing you agree to the terms and conditions of use of the software (see section [Licensing](#licensing) below). 

<br> 

By default, [xcofdk-rte](https://pypi.org/project/xcofdk-rte/) is auto-installed, whenever 
[xcofdk](https://pypi.org/project/xcofdk/) is installed:
```bash
$> python3 -m pip install xcofdk
```

Or, it may also be installed separately:
```bash
$> python3 -m pip install xcofdk-rte
```

<br>

# Licensing

Unless used by a frontend package other than the default frontend package [xcofdk](https://pypi.org/project/xcofdk/), 
use of the backend package [xcofdk-rte](https://pypi.org/project/xcofdk-rte/) is free of charge and granted under terms 
and conditions stated in the [License](https://github.com/xcofdk/xcofdkrte-py/blob/master/LICENSE.txt) file. 
