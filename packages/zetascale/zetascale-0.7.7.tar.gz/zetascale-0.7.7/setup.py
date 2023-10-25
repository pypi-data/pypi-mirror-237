# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zeta',
 'zeta.models',
 'zeta.nn',
 'zeta.nn.architecture',
 'zeta.nn.attention',
 'zeta.nn.biases',
 'zeta.nn.embeddings',
 'zeta.nn.modules',
 'zeta.nn.modules.xmoe',
 'zeta.ops',
 'zeta.optim',
 'zeta.quant',
 'zeta.rl',
 'zeta.tokenizers',
 'zeta.training',
 'zeta.utils']

package_data = \
{'': ['*']}

install_requires = \
['accelerate',
 'beartype',
 'bitsandbytes',
 'colt5-attention==0.10.14',
 'datasets',
 'einops',
 'einops-exts',
 'fairscale',
 'lion-pytorch',
 'pytest',
 'scipy',
 'sentencepiece',
 'tiktoken',
 'timm',
 'tokenmonster',
 'torch',
 'torchvision',
 'transformers',
 'typing',
 'vector-quantize-pytorch==1.9.14']

setup_kwargs = {
    'name': 'zetascale',
    'version': '0.7.7',
    'description': 'Transformers at zeta scales',
    'long_description': '[![Multi-Modality](images/agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n![Zeta banner](images/zeta.png)\n\n[![Docs](https://readthedocs.org/projects/zeta/badge/)](https://zeta.readthedocs.io)\n\n<p>\n  <a href="https://github.com/kyegomez/zeta/blob/main/LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-blue.svg" /></a>\n  <a href="https://pypi.org/project/zetascale"><img alt="MIT License" src="https://badge.fury.io/py/zetascale.svg" /></a>\n</p>\n\nBuild High-performance, agile, and scalable AI models with modular and re-useable building blocks!\n\n# 🤝 Schedule a 1-on-1 Session\nBook a [1-on-1 Session with Kye](https://calendly.com/apacai/agora), the Creator, to discuss any issues, provide feedback, or explore how we can improve Zeta for you.\n\n\n## Installation\n\n`pip install zetascale`\n\n## Initiating Your Journey\n\nCreating a model empowered with the aforementioned breakthrough research features is a breeze. Here\'s how to quickly materialize the renowned Flash Attention\n\n```python\nimport torch\nfrom zeta import FlashAttention\n\nq = torch.randn(2, 4, 6, 8)\nk = torch.randn(2, 4, 10, 8)\nv = torch.randn(2, 4, 10, 8)\n\nattention = FlashAttention(causal=False, dropout=0.1, flash=True)\noutput = attention(q, k, v)\n\nprint(output.shape) \n\n```\n\n# Documentation\n[Click here for the documentation, it\'s at zeta.apac.ai](https://zeta.apac.ai)\n\n# Vision\nZeta hopes to be the leading framework and library to effortlessly enable you to create the most capable and reliable foundation models out there with infinite scalability in as minmal amounts of code as possible\n\n\n## Contributing\nWe\'re dependent on you for contributions, it\'s only Kye maintaining this repository and it\'s very difficult and with that said any contribution is infinitely appreciated by not just me but by Zeta\'s users who dependen on this repository to build the world\'s\nbest AI models\n\n* Head over to the project board to look at open features to implement or bugs to tackle\n\n## Project Board\n[This weeks iteration is here](https://github.com/users/kyegomez/projects/7/views/2)\n',
    'author': 'Zeta Team',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/zeta',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
