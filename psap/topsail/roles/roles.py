import sys

from projects.core.library.ansible_toolbox import (
    RunAnsibleRole, AnsibleRole,
    AnsibleMappedParams, AnsibleConstant,
    AnsibleSkipConfigGeneration
)

class TopsailRoles:
    """
    Commands related to the current role
    """

    @AnsibleRole("plotter")
    @AnsibleMappedParams
    def main(self,
                     namespace,
                     delete_others=True,
                     ):
        """
        Run the plotter role

        Args:
          namespace: the namespace in which the model should be deployed
          delete_others: if True, deletes the other serving runtime/inference services of the namespace
        """

        # if runtime not in ("standalone-tgis", "vllm"):
        #     raise ValueError(f"Unsupported runtime: {runtime}")

        return RunAnsibleRole(locals())

    @AnsibleRole("smi_gather")
    @AnsibleMappedParams
    def main(self,
                     namespace,
                     delete_others=True,
                     ):
        """
        Run the plotter role

        Args:
          namespace: the namespace in which the model should be deployed
          delete_others: if True, deletes the other serving runtime/inference services of the namespace
        """

        # if runtime not in ("standalone-tgis", "vllm"):
        #     raise ValueError(f"Unsupported runtime: {runtime}")

        return RunAnsibleRole(locals())

    @AnsibleRole("whisper")
    @AnsibleMappedParams
    def main(self,
                     namespace,
                     delete_others=True,
                     ):
        """
        Run the plotter role

        Args:
          namespace: the namespace in which the model should be deployed
          delete_others: if True, deletes the other serving runtime/inference services of the namespace
        """

        # if runtime not in ("standalone-tgis", "vllm"):
        #     raise ValueError(f"Unsupported runtime: {runtime}")

        return RunAnsibleRole(locals())
