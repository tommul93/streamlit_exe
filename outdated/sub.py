import subprocess as sp
import shlex

sp.call(shlex.split("streamlit run pyinstaller_main.py"), shell=True)