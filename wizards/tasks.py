
from django.template import loader, Context

class Task(object):

    def render():
        raise NotImplementedError


class CompositeTask(Task):
    pass


class SimpleTask(Task):
    pass


class TestTask(CompositeTask):

    template = 'test_task.html'
    actions = {'previous', 'next'}

    def __init__(self, length, prefix = "", state = None, data = None, posted = None):
        self._subtasks = [NumberedFormTask(i) for i in range(length)]
        self._prefix = prefix
        self.restore_state(state)
        self.process_action(self.extract_action(posted or {}))


    def extract_action(self, posted):
        _actions = [action for action in self.actions if self.prefixed(action) in posted]
        if len(_actions) > 1:
            raise ValueError('Cannot process more than one action.')
        elif len(_actions) == 0:
            return None
        else:
            return _actions[0]


    def process_action(self, action):
        if action == 'previous':
            self._current_subtask = max(0, self._current_subtask - 1)
        elif action == 'next':
            self._current_subtask = min(len(self._subtasks) - 1, self._current_subtask + 1)


    def save_state(self, storage):
        storage[self.prefixed('current_subtask')] = self._current_subtask


    def restore_state(self, state):
        if state is None:
            self._current_subtask = 0
        else:
            self._current_subtask = state.get(self.prefixed('current_subtask'), 0)


    def prefixed(self, key):
        return self._prefix + key


    def render(self):
        _template = loader.get_template(self.template)
        return _template.render(Context(self.get_context()))


    def get_context(self):
        context = {'subtask':  self._subtasks[self._current_subtask] }
        context.update(self.get_actions_for_context())
        context.update(self.get_labels())
        return context


    def get_actions_for_context(self):
        return dict((action, self.prefixed(action)) for action in self.actions)


    def get_labels(self):
        labels = []
        for subtask in self._subtasks:
            labels += subtask.get_labels()


class NumberedFormTask(SimpleTask):

    def __init__(self, number):
        self._number = number


    def render(self):
        return "<p>Task: <b>" + str(self._number) + "</b></p>"

