# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kosmosg']

package_data = \
{'': ['*']}

install_requires = \
['einops', 'torch', 'torchscale', 'zetascale']

setup_kwargs = {
    'name': 'kosmosg',
    'version': '0.0.4',
    'description': 'kosmosg - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n# KosmosG\nMy implementation of the model KosmosG from "KOSMOS-G: Generating Images in Context with Multimodal Large Language Models"\n\n## Installation\n`pip install kosmosg`\n\n## Usage\n```python\nimport torch\nfrom kosmosg.main import KosmosG\n\n# usage\nimg = torch.randn(1, 3, 256, 256)\ntext = torch.randint(0, 20000, (1, 1024))\n\nmodel = KosmosG()\noutput = model(img, text)\nprint(output)\n```\n\n## Architecture\n`text, image => KosmosG => text tokens with multi modality understanding`\n\n## License\nMIT\n\n## Todo\n- Create Aligner in pytorch\n- Create Diffusion module\n- Integrate these pieces\n- Create a training script',
    'author': 'Kye Gomez',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/KosmosG',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
