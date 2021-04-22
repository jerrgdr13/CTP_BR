from pptx import Presentation  
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Emu, Inches, Cm
from urlparse import urljoin, urlparse
from urllib import quote
#from urllib.parse import quote
# import numpy
#from bitmath import *
import yaml
import string
from datetime import datetime
from wand.image import Image
from io import BytesIO
import matplotlib
matplotlib.use('Agg')
from matplotlib import dates
from google.cloud import bigquery
from google.oauth2 import service_account
from datetime import datetime
import json, re, time, boto3
import statistics
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_gbq
import requests, xmltodict, shutil, cv2, os, hashlib
import matplotlib.ticker as ticker
import socket
import time
import boto3
from botocore.exceptions import ClientError
import psycopg2
# import datetime
from iso3166 import countries
#import pycountry
import uuid
import tldextract
import glob
import collections
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from collections import OrderedDict
from hurry.filesize import size
import argparse
import sys
sys.path.append('.')
from classes.wpt_processing import WptProcessing
from classes.utilities import Utilities