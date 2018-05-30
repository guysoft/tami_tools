from fabric.api import *
from fabric.context_managers import cd
from fabric.contrib import files
import os
import datetime

env.hosts = ["space.telavivmakers.org"]
env.user = "root"
env.key_filename = os.path.expanduser("~/.ssh/id_rsa_tami")
env.shell = ""


def backup_etc_router():
    BACKUP_DIR = os.path.join(os.path.dirname(__file__), "backups")
    #run("/bin/ls")
    if files.exists("/tmp/config.tar.gz"):
        run("/bin/rm /tmp/config.tar.gz")
    run("/bin/tar czf /tmp/config.tar.gz /etc", shell_escape=False, shell=False)
    #get("/tmp/config.tar.gz", "/tmp/config.tar.gz")
    os.system("scp space.telavivmakers.org:/tmp/config.tar.gz " + os.path.join(BACKUP_DIR, "config_" + datetime.datetime.now().strftime("%Y-%m-%d")  + ".tar.gz"))
