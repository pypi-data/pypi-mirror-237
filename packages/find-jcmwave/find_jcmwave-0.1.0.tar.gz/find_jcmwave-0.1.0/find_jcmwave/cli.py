import argparse
import os
import sys
import site
from . import module_path

parser = argparse.ArgumentParser(
                    prog='Find JCMWAVE CLI',
                    description='Link JCMWAVE and your python environment',
                    epilog="That's all. Have fun.")

parser.add_argument('-l', '--lib',
                    action='store_true', 
                    help='link the third party support library into your ' 
                        'current python environment')
parser.add_argument('-i', '--interpreter',
                    action='store_true',
                    help='replace the jcm built in python interpreter '
                        'with the one from your environment')

def cli():
    args = parser.parse_args()
    if args.lib:
        link_lib()
    if args.interpreter:
        link_interpreter()
    if not (args.lib or args.interpreter):
        parser.print_help()

def link_lib():
    os.symlink(f"{module_path}/jcmwave", f"{site.getsitepackages()[0]}/jcmwave")
    print("linked jcmwave module")

def link_interpreter():
    os.rename(f"{module_path}/bin/python", f"{module_path}/bin/old_python")
    os.symlink(sys.executable, f"{module_path}/bin/python")