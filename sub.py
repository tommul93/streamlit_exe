import subprocess as sp
import shlex

sp.call(shlex.split("streamlit run main.py"), shell=True)