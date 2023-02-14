import pluggy
from movingpandas import TrajectoryCollection

HOOK_NAMESPACE = "co-pilot-python"
hook_spec = pluggy.HookspecMarker(HOOK_NAMESPACE)
hook_impl = pluggy.HookimplMarker(HOOK_NAMESPACE)


class MoveAppsSpec(object):
    @hook_spec
    def execute(self, data: TrajectoryCollection, config: dict) -> TrajectoryCollection:
        """Invokes your main business logic

        :param data: the input data for this app. It is the output of the predecessor app in a MoveApps workflow.
        :param config: the configuration of your app. Values are set by the MoveApps workflow user.
        :return: data for any next app in the workflow
        """
        pass
