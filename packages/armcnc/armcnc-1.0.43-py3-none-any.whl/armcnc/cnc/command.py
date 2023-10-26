"""
******************************************************************************
* @author  ARMCNC site:www.armcnc.net github:armcnc.github.io
******************************************************************************
"""

import linuxcnc

class Command:

    def __init__(self, framework):
        self.framework = framework
        self.linuxcnc = linuxcnc
        self.api = self.linuxcnc.command()

    def set_mode(self, m, t, *p):
        self.framework.status.api.poll()
        if self.framework.status.api.task_mode == m or self.framework.status.api.task_mode in p:
            return True
        self.api.mode(m)
        if t == 0:
            self.api.wait_complete()
        else:
            self.api.wait_complete(t)

        self.framework.status.api.poll()
        return True
