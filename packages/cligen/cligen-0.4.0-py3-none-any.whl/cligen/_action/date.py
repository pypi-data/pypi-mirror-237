import argparse
import datetime
import typing

_parameters = """\
default: today
"""


class DateAction(argparse.Action):
    # argparse action for parsing dates with or without dashes
    #
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--verbose', '-v', action=DateAction)

    def __init__(
        self,
        option_strings: typing.Any,
        dest: typing.Any,
        nargs: typing.Optional[typing.Any] = None,
        **kwargs: typing.Any
    ):
        if nargs != 1 and nargs not in [None, '?', '*']:
            raise ValueError('DateAction can only have one argument')
        default = kwargs.get('default')
        if isinstance(default, str):
            kwargs['default'] = self.special(default)
        super(DateAction, self).__init__(option_strings, dest, nargs=nargs, **kwargs)

    def __call__(
        self,
        parser: typing.Any,
        namespace: argparse.Namespace,
        values: typing.Union[str, typing.Sequence[str], None],
        option_string: typing.Optional[str] = None,
    ) -> None:
        # this is only called if the option is specified
        if values is None:
            return None
        assert isinstance(values, str)
        s = values
        for c in './-_':
            s = s.replace(c, '')
        try:
            val = datetime.datetime.strptime(s, '%Y%m%d').date()
        except ValueError:
            val = self.special(values)
        #    val = self.const
        setattr(namespace, self.dest, val)

    def special(self, date_s: str) -> DefaultVal:
        if date_s in ['today', 'tomorrow', 'yesterday']:
            today = datetime.date.today()
            one_day = datetime.timedelta(days=1)
            if date_s == 'today':
                return DefaultVal(today)
            if date_s == 'yesterday':
                return DefaultVal(today - one_day)
            if date_s == 'tomorrow':
                return DefaultVal(today + one_day)
        if date_s.replace('-', '').isdigit():
            if '-' in date_s:
                return DefaultVal(datetime.date(*[int(x) for x in date_s.split('-')]))
        if date_s[0] in 'dw':
            try:
                nr = int(date_s[1:])
            except ValueError:
                nr = None
            if nr is not None:
                today = datetime.date.today()
                if date_s[0] == 'w':
                    nr *= 7
                return today + datetime.timedelta(days=nr)
        raise ValueError
