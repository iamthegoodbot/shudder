# -*- coding: utf-8 -*-
import os
import subprocess


class ShutdownWorkers(object):

    def run(self):
        conf_file = os.environ.get('SV_CONF')
        subprocess.call(['supervisorctl', '--config={}'.format(conf_file), 'stop', 'all'])
        return True