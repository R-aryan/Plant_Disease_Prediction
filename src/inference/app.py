from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

# Define a flask app
app = Flask(__name__)