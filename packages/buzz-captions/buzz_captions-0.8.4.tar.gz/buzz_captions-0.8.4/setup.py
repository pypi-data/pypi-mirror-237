# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['buzz',
 'buzz.settings',
 'buzz.store',
 'buzz.widgets',
 'buzz.widgets.preferences_dialog',
 'buzz.widgets.transcriber',
 'buzz.widgets.transcription_viewer']

package_data = \
{'': ['*'], 'buzz': ['assets/*']}

install_requires = \
['PyQt6==6.4.0',
 'appdirs>=1.4.4,<2.0.0',
 'dataclasses-json>=0.5.9,<0.6.0',
 'faster-whisper>=0.4.1,<0.5.0',
 'humanize>=4.4.0,<5.0.0',
 'keyring>=23.13.1,<24.0.0',
 'openai-whisper==v20230124',
 'openai>=0.27.1,<0.28.0',
 'platformdirs>=3.5.3,<4.0.0',
 'sounddevice>=0.4.5,<0.5.0',
 'stable-ts==1.0.2',
 'torch==1.12.1',
 'transformers>=4.24.0,<4.25.0']

setup_kwargs = {
    'name': 'buzz-captions',
    'version': '0.8.4',
    'description': '',
    'long_description': '# Buzz\n\n[Documentation](https://chidiwilliams.github.io/buzz/) | [Buzz Captions on the App Store](https://apps.apple.com/us/app/buzz-captions/id6446018936?mt=12&itsct=apps_box_badge&itscg=30200)\n\nTranscribe and translate audio offline on your personal computer. Powered by\nOpenAI\'s [Whisper](https://github.com/openai/whisper).\n\n![MIT License](https://img.shields.io/badge/license-MIT-green)\n[![CI](https://github.com/chidiwilliams/buzz/actions/workflows/ci.yml/badge.svg)](https://github.com/chidiwilliams/buzz/actions/workflows/ci.yml)\n[![codecov](https://codecov.io/github/chidiwilliams/buzz/branch/main/graph/badge.svg?token=YJSB8S2VEP)](https://codecov.io/github/chidiwilliams/buzz)\n![GitHub release (latest by date)](https://img.shields.io/github/v/release/chidiwilliams/buzz)\n[![Github all releases](https://img.shields.io/github/downloads/chidiwilliams/buzz/total.svg)](https://GitHub.com/chidiwilliams/buzz/releases/)\n\n<blockquote>\n<p>Buzz is better on the App Store. Get a Mac-native version of Buzz with a cleaner look, audio playback, drag-and-drop import, transcript editing, search, and much more.</p>\n<a href="https://apps.apple.com/us/app/buzz-captions/id6446018936?mt=12&amp;itsct=apps_box_badge&amp;itscg=30200"><img src="https://tools.applemediaservices.com/api/badges/download-on-the-mac-app-store/black/en-us?size=250x83&amp;releaseDate=1679529600" alt="Download on the Mac App Store" /></a>\n</blockquote>\n\n![Buzz](./buzz/assets/buzz-banner.jpg)\n\n## Installation\n\n**macOS**:\n\n```shell\nbrew install --cask buzz\n```\n\n**Windows**:\n\nDownload and run the `.exe` file in the [releases page](https://github.com/chidiwilliams/buzz/releases/latest).\n\n**Linux**:\n\n```shell\nsudo apt-get install libportaudio2\nsudo snap install buzz\n```\n',
    'author': 'Chidi Williams',
    'author_email': 'williamschidi1@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/chidiwilliams/buzz',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9.13,<3.11',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
