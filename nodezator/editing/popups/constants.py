
### local imports

from contextlib import suppress

from config import APP_REFS

from loopman.exception import ContinueLoopException

from ourstdlibs.behaviour import get_suppressing_callable


class GeneralPopupCommands:

    def __init__(self):

        cls = self.__class__

        if not hasattr(cls, 'GENERAL_COLLECTIVE_COMMANDS'):

            cls.GENERAL_SINGLE_COMMANDS = [

              {
                 'label': "Move",
                 'icon': 'moving',
                 'command': self.move_obj,
              },

              {
                 'label': "Duplicate",
                 'icon': 'duplication',
                 'command': self.duplicate_obj,
              },

              {
                 'label'   : "Delete",
                 'icon'    : 'delete',
                 'command' : self.delete_obj,
              },

            ]

            cls.GENERAL_COLLECTIVE_COMMANDS = [

              {'label' : "---"},

              {
                'label'   : "Move selected",
                'icon'    : 'moving',
                'command' : get_suppressing_callable(
                              APP_REFS.ea.start_moving,
                              ContinueLoopException,
                            ),
              },

              {
                'label'   : "Duplicate selected",
                'icon'    : 'duplication',
                'command' : get_suppressing_callable(
                              APP_REFS.ea.duplicate_selected,
                              ContinueLoopException,
                            ),
              },

              {
                'label'   : "Delete selected",
                'icon'    : 'delete',
                'command' : APP_REFS.ea.remove_selected,
              },

            ]

    def move_obj(self):

        APP_REFS.ea.deselect_all()

        APP_REFS.ea.add_obj_to_selection(
          self.obj_under_mouse
        )

        with suppress(ContinueLoopException):
            APP_REFS.ea.start_moving()

    def duplicate_obj(self):

        APP_REFS.ea.deselect_all()

        APP_REFS.ea.add_obj_to_selection(
          self.obj_under_mouse
        )

        with suppress(ContinueLoopException):
            APP_REFS.ea.duplicate_selected()

    def delete_obj(self):

        APP_REFS.ea.deselect_all()

        APP_REFS.ea.add_obj_to_selection(
          self.obj_under_mouse
        )

        APP_REFS.ea.remove_selected()


## function for injection

def get_node_info(self):
    APP_REFS.ea.view_info(self.obj_under_mouse)
