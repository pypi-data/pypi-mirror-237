import logging

from naludaq.controllers import get_board_controller
from naludaq.helpers.exceptions import RegisterNameError

from .udc16 import PedestalsGeneratorUdc16

LOGGER = logging.getLogger("naludaq.pedestals_generator_upac96")


def disable_trigger_monitor_signal(func):
    """Decorator to disable the trigger monitor signal during the execution of a function.

    Args:
        func (function): function to decorate

    Returns:
        function: decorated function
    """

    def wrapper(self, *args, **kwargs):
        try:
            previous = self.board.registers["control_registers"][
                "trigger_monitor_disable"
            ]["value"]
        except KeyError:
            raise RegisterNameError("trigger_monitor_disable")
        bc = get_board_controller(self.board)
        bc.set_trigger_monitoring_disabled(disabled=True)
        try:
            result = func(self, *args, **kwargs)
        finally:
            bc.set_trigger_monitoring_disabled(previous)
        return result

    return wrapper


class PedestalsGeneratorUpac96(PedestalsGeneratorUdc16):
    """Pedestals generator for UPAC96."""

    @disable_trigger_monitor_signal
    def _capture_data_for_pedestals(self) -> list[list[dict]]:
        return super()._capture_data_for_pedestals()

    def _validate_event(self, event):
        """Check if the event has a data field, which means it's parsed"""
        if "data" not in event:
            LOGGER.warning("Got an invalid event")
            return False
        chans_with_data = [i for i, x in enumerate(event.get("data", [])) if len(x) > 0]
        is_superset = set(chans_with_data).issuperset(self._channels)
        if not is_superset:
            LOGGER.warning(
                "Got a parseable event, but the channels are incorrect: %s",
                chans_with_data,
            )
        return is_superset
