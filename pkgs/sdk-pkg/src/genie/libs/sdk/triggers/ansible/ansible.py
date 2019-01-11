# import ats
from ats import aetest
from pyats.log.utils import banner
import logging
from genie.harness.base import Trigger
import ansible_runner

log = logging.getLogger()


class RunAnsiblePlaybook(Trigger):

    @aetest.test
    def run_playbook(self, uut, playbook, inventory):
        log.info(banner("Running Ansible Playbook {}".format(playbook)))
        r = ansible_runner.run(private_data_dir='.',
                               inventory=inventory,
                               playbook=playbook)

        log.info("Playbook status: {}".format(r.stats))
