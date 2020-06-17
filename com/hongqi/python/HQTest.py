import os, sys
sys.path.insert(0, '..')
codePath = os.path.abspath(os.path.join(__file__, "../..", "json"))
if os.path.exists(codePath):
    sys.path.append(codePath)
sys.path.insert(0, '..')
sys.path.append("../")

from com.hongqi.python.json import HQJsonUtils
#from .excel import HQBotRelation2
