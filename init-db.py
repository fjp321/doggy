import sys
import numpy as np
import scipy as sp
import pandas as pd
from lxml import etree as et
root=et.Element("recipes")
db=open('recipes.xml','w')
db.write(et.tostring(root, pretty_print=True, encoding='utf-8').decode('utf-8'))
db.close()