from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.6.9'
DESCRIPTION = 'Connecting Music to Real Time Emotions'
LONG_DESCRIPTION = 'Recommend Users Songs on the Basis of their Mood by detecting Facial Expressions'

# Setting up
setup(
    name="emomusic",
    version=VERSION,
    author="SUKH",
    author_email="<frsukhh@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['opencv-python', 'cv2','numpy','matplotlib','urllib.request','DeepFace','HTTPHandler',],
    keywords=['python', 'music', 'stream', 'music stream', 'camera', 'emotions'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
