import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

PLN_DBSCHEMA = os.environ.get("PLN_DBSCHEMA")
PLN_DBNM = os.environ.get("PLN_DBNM")
PLN_DBUSERNM = os.environ.get("PLN_DBUSERNM")
PLN_DBPASSWD = os.environ.get("PLN_DBPASSWD")

IF_DBSCHEMA = os.environ.get("IF_DBSCHEMA")
IF_DBNM = os.environ.get("IF_DBNM")
IF_DBUSERNM = os.environ.get("IF_DBUSERNM")
IF_DBPASSWD = os.environ.get("IF_DBPASSWD")