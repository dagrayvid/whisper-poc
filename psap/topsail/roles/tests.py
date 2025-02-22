import sys

from core.library.ansible_toolbox import (
    RunAnsibleRole, AnsibleRole,
    AnsibleMappedParams, AnsibleConstant,
    AnsibleSkipConfigGeneration
)

class Tests:
    """
    Commands related to the current role
    """

    @AnsibleRole("tests")
    @AnsibleMappedParams
    def main(self,
                    test_name="main",
    ):
        """
        Run the tests role
        """

        # if runtime not in ("standalone-tgis", "vllm"):
        #     raise ValueError(f"Unsupported runtime: {runtime}")

        return RunAnsibleRole(locals())

    @AnsibleRole("tests")
    @AnsibleMappedParams
    def whisper(self,
                    test_name="whisper",
    ):
        """
        Run the tests role
        """

        # if runtime not in ("standalone-tgis", "vllm"):
        #     raise ValueError(f"Unsupported runtime: {runtime}")

        return RunAnsibleRole(locals())
