TAMI Backup Tools
=================




Install
-------


    sudo pip3 install fabric3


Make sure you have the ssh key for ``space.telavivmakers.org`` in ``~/.ssh/id_rsa_tami``.



Usage
-----


backup etc folder on router
---------------------------


    cd src
    fab backup_etc_router

backups are saved in src/backups
