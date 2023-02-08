import pluggy
from sdk.moveapps_spec import MoveAppsSpec, HOOK_NAMESPACE
from sdk.moveapps_io import MoveAppsIo
from sdk.moveapps_execution import MoveAppsExecutor

PROJECT_NAME = "co-pilot-python"


class MoveAppsSdk:

    def __init__(self, active_hooks=None) -> None:
        """
        Setup the plugin manager and register all the hooks.
        """
        self._pm = pluggy.PluginManager(HOOK_NAMESPACE)
        self._pm.add_hookspecs(MoveAppsSpec)
        self.hooks = active_hooks
        if self.hooks:
            for hook in self.hooks:
                self._pm.register(hook)

        executor = MoveAppsExecutor(plugin_manager=self._pm)
        executor.execute()


if __name__ == "__main__":
    from app.app import App
    # LIFO
    hooks = [App(moveapps_io=MoveAppsIo())]
    sdk = MoveAppsSdk(active_hooks=hooks)
