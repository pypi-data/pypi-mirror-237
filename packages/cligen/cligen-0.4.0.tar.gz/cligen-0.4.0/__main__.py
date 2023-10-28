# coding: utf-8
# flake8: noqa
# cligen: 0.3.2, dd: 2023-10-27, args: gen


import argparse
import importlib
import os
import pathlib
import ruamel.yaml
import sys
import typing

from . import __version__


class HelpFormatter(argparse.RawDescriptionHelpFormatter):
    def __init__(self, *args: typing.Any, **kw: typing.Any):
        kw['max_help_position'] = 40
        super().__init__(*args, **kw)

    def _fill_text(self, text: str, width: int, indent: str) -> str:
        import textwrap

        paragraphs = []
        for paragraph in text.splitlines():
            paragraphs.append(textwrap.fill(paragraph, width,
                             initial_indent=indent,
                             subsequent_indent=indent))
        return '\n'.join(paragraphs)


class ArgumentParser(argparse.ArgumentParser):
    def __init__(self, *args: typing.Any, **kw: typing.Any):
        kw['formatter_class'] = HelpFormatter
        super().__init__(*args, **kw)


class DefaultVal(str):
    def __init__(self, val: typing.Any):
        self.val = val

    def __str__(self) -> str:
        return str(self.val)


class ConfigBase:
    suffix = ""

    def __init__(self, path: typing.Optional[typing.Union[pathlib.Path, str]]=None):
        self._data = None
        tmp_path = self.get_config_parm()
        if tmp_path:
            self._path = tmp_path
        elif isinstance(path, pathlib.Path):
            self._path = path
        elif path is not None:
            if path[0] in '~/':
                self._path = pathlib.Path(path).expanduser()
            elif '/' in path:  # assume '!Config config_dir/config_name'
                self._path = self.config_dir / path
            else:
                self._path = self.config_dir / path / (path.rsplit('.')[-1] + self.suffix)
        else:
            raise NotImplementedError

    @property
    def data(self) -> typing.Any:
        if self._data is None:
            self._data = self.load()  # NOQA
        return self._data

    def get(self, *args: typing.Any, pd: typing.Optional[typing.Any]=None) -> typing.Any:
        data = self.data
        try:
            for arg in args:
                if arg in data:
                    data = data[arg]
                else:
                    break
            else:
                return data
        except Exception as e:
            print(f'exception getting "{arg}" from "{args}" ({self.data})') 
            return {}
        if args[0] != 'global':
            return self.get(*(['global'] + list(args[1:])), pd=pd)
        return pd

    def get_config_parm(self) -> typing.Union[pathlib.Path, None]:
        for idx, arg in enumerate(sys.argv[1:]):
            if arg.startswith('--config'):
                if len(arg) > 8 and arg[8] == '=':
                    return pathlib.Path(arg[9:])
                else:
                    try:
                        return pathlib.Path(sys.argv[idx + 2])
                    except IndexError:
                        print('--config needs an argument')
                        sys.exit(1)
        return None

    @property
    def config_dir(self) -> pathlib.Path:
        attr = '_' + sys._getframe().f_code.co_name
        if not hasattr(self, attr):
            if sys.platform.startswith('win32'):
                d = os.environ['APPDATA']
            else:
                d = os.environ.get(
                    'XDG_CONFIG_HOME', os.path.join(os.environ['HOME'], '.config')
                )
            pd = pathlib.Path(d)
            setattr(self, attr, pd)
            return pd
        return getattr(self, attr)  # type: ignore

    def load(self) -> typing.Any:
        raise NotImplementedError


class ConfigYAML(ConfigBase):
    suffix = '.yaml'

    def load(self) -> typing.Any:
        yaml = ruamel.yaml.YAML(typ='safe')
        try:
            data = yaml.load(self._path)
        except (FileNotFoundError, TypeError, KeyError):
            return {}
        return data

    def __repr__(self) -> str:
        return f'ConfigYAML(path="{self._path}")'


class CountAction(argparse.Action):

    def __call__(
        self,
        parser: typing.Any,
        namespace: argparse.Namespace,
        values: typing.Union[str, typing.Sequence[str], None],
        option_string: typing.Optional[str] = None,
    ) -> None:
        if self.const is None:
            self.const = 1
        try:
            val = getattr(namespace, self.dest) + self.const
        except TypeError:  # probably None
            val = self.const
        setattr(namespace, self.dest, val)


def main(cmdarg: typing.Optional[typing.List[str]]=None) -> int:
    cmdarg = sys.argv if cmdarg is None else cmdarg
    parsers = []
    config = ConfigYAML(path='cligen')
    parsers.append(ArgumentParser())
    parsers[-1].add_argument('--verbose', '-v', default=DefaultVal(config.get('global', 'verbose', pd=0)), dest='_gl_verbose', metavar='VERBOSE', nargs=0, help='increase verbosity level', action=CountAction)
    parsers[-1].add_argument('--comment', default=DefaultVal(config.get('global', 'comment', pd=None)), dest='_gl_comment', action='store_true', help="don't strip comments from included code (config)")
    parsers[-1].add_argument('--debug', default=DefaultVal(config.get('global', 'debug', pd=None)), dest='_gl_debug', action='store_true', help='insert debug statements in generated code')
    parsers[-1].add_argument('--version', action='store_true', help='show program\'s version number and exit')
    subp = parsers[-1].add_subparsers()
    px = subp.add_parser('gen', description='execute show related commands', help='execute show related commands')
    px.set_defaults(subparser_func='gen')
    parsers.append(px)
    parsers[-1].add_argument('--meld', default=config.get('gen', 'meld', pd=False), action='store_true', help='present output as diff for inspection')
    parsers[-1].add_argument('--verbose', '-v', default=DefaultVal(config.get('gen', 'verbose', pd=0)), nargs=0, help='increase verbosity level', action=CountAction)
    parsers[-1].add_argument('--comment', default=DefaultVal(config.get('gen', 'comment', pd=False)), action='store_true', help="don't strip comments from included code (config)")
    parsers[-1].add_argument('--debug', default=DefaultVal(config.get('gen', 'debug', pd=False)), action='store_true', help='insert debug statements in generated code')
    px = subp.add_parser('replace', description='replace a string in the _cligen_data/cli.yaml', help='replace a string in the _cligen_data/cli.yaml')
    px.set_defaults(subparser_func='replace')
    parsers.append(px)
    parsers[-1].add_argument('--from', default=config.get('replace', 'from', pd=None), dest='frm', help='original string to match (default: %(default)s)', required=True)
    parsers[-1].add_argument('--to', default=config.get('replace', 'to', pd=None), help='replacement string (default: %(default)s)', required=True)
    parsers[-1].add_argument('--backup', default=config.get('replace', 'backup', pd=False), action='store_true', help='make a timestamped backup of the file (.YYYYMMDD-HHMMSS)')
    parsers[-1].add_argument('path', default=config.get('replace', 'path', pd=['**/__init__.py', '**/cli.yaml']), nargs='*', help='path pattern to scan for replacement (default: %(default)s)')
    parsers[-1].add_argument('--verbose', '-v', default=DefaultVal(config.get('replace', 'verbose', pd=0)), nargs=0, help='increase verbosity level', action=CountAction)
    parsers[-1].add_argument('--comment', default=DefaultVal(config.get('replace', 'comment', pd=False)), action='store_true', help="don't strip comments from included code (config)")
    parsers[-1].add_argument('--debug', default=DefaultVal(config.get('replace', 'debug', pd=False)), action='store_true', help='insert debug statements in generated code')
    px = subp.add_parser('update', description='common updates to _cligen_data/cli.yaml\n- remove explicit default adding on !Help if !AddDefaults is set\n', help='common updates to _cligen_data/cli.yaml\n- remove explicit default adding on !Help if !AddDefaults is set\n')
    px.set_defaults(subparser_func='update')
    parsers.append(px)
    parsers[-1].add_argument('--test', default=config.get('update', 'test', pd=False), action='store_true', help="don't save")
    parsers[-1].add_argument('path', default=config.get('update', 'path', pd=['**/__init__.py', '**/cli.yaml']), nargs='*', help='path pattern to scan for replacement (default: %(default)s)')
    parsers[-1].add_argument('--verbose', '-v', default=DefaultVal(config.get('update', 'verbose', pd=0)), nargs=0, help='increase verbosity level', action=CountAction)
    parsers[-1].add_argument('--comment', default=DefaultVal(config.get('update', 'comment', pd=False)), action='store_true', help="don't strip comments from included code (config)")
    parsers[-1].add_argument('--debug', default=DefaultVal(config.get('update', 'debug', pd=False)), action='store_true', help='insert debug statements in generated code')
    px = subp.add_parser('convert', description='analyse argument file that uses ruamel.std.argparse and generate cligen data\n- commands currently cannot have a different name (using set first @subparser argument)\n', help='analyse argument file that uses ruamel.std.argparse and generate cligen data\n- commands currently cannot have a different name (using set first @subparser argument)\n')
    px.set_defaults(subparser_func='convert')
    parsers.append(px)
    parsers[-1].add_argument('--append', default=config.get('convert', 'append', pd=False), action='store_true', help='append _cligen_data to __init__.py')
    parsers[-1].add_argument('path')
    parsers[-1].add_argument('--verbose', '-v', default=DefaultVal(config.get('convert', 'verbose', pd=0)), nargs=0, help='increase verbosity level', action=CountAction)
    parsers[-1].add_argument('--comment', default=DefaultVal(config.get('convert', 'comment', pd=False)), action='store_true', help="don't strip comments from included code (config)")
    parsers[-1].add_argument('--debug', default=DefaultVal(config.get('convert', 'debug', pd=False)), action='store_true', help='insert debug statements in generated code')
    px = subp.add_parser('comment', description='show cligen_data comments (from cligen.__init__.py)', help='show cligen_data comments (from cligen.__init__.py)')
    px.set_defaults(subparser_func='comment')
    parsers.append(px)
    parsers[-1].add_argument('--update', default=config.get('comment', 'update', pd=None), help='update cligen_data comments in __init__.py (argument can be directory or file) (default: %(default)s)')
    parsers[-1].add_argument('--verbose', '-v', default=DefaultVal(config.get('comment', 'verbose', pd=0)), nargs=0, help='increase verbosity level', action=CountAction)
    parsers[-1].add_argument('--comment', default=DefaultVal(config.get('comment', 'comment', pd=False)), action='store_true', help="don't strip comments from included code (config)")
    parsers[-1].add_argument('--debug', default=DefaultVal(config.get('comment', 'debug', pd=False)), action='store_true', help='insert debug statements in generated code')
    px = subp.add_parser('snippet', description='work on snippets (site-packages/cligen/_snippet, ~/.config/cligen/snippet), by default insert\nbased on matching arguments\n', help='work on snippets (site-packages/cligen/_snippet, ~/.config/cligen/snippet), by default insert\nbased on matching arguments\n')
    px.set_defaults(subparser_func='snippet')
    parsers.append(px)
    parsers[-1].add_argument('--list', default=config.get('snippet', 'list', pd=False), action='store_true', help='list available snippets for current environment')
    parsers[-1].add_argument('--log', default=config.get('snippet', 'log', pd='/var/tmp/snippet.log'), help='file to log output to (default: %(default)s)')
    parsers[-1].add_argument('arg', default=config.get('snippet', 'arg', pd=None), nargs='*')
    parsers[-1].add_argument('arg', default=config.get('snippet', 'arg', pd=None), nargs='*')
    parsers[-1].add_argument('--verbose', '-v', default=DefaultVal(config.get('snippet', 'verbose', pd=0)), nargs=0, help='increase verbosity level', action=CountAction)
    parsers[-1].add_argument('--comment', default=DefaultVal(config.get('snippet', 'comment', pd=False)), action='store_true', help="don't strip comments from included code (config)")
    parsers[-1].add_argument('--debug', default=DefaultVal(config.get('snippet', 'debug', pd=False)), action='store_true', help='insert debug statements in generated code')
    parsers.pop()
    # sp: gen
    _subparser_found = False
    for arg in cmdarg[1:]:
        if arg in ['-h', '--help', '--version']:  # global help if no subparser
            break
    else:
        end_pos = None if '--' not in cmdarg else cmdarg.index('--')
        for sp_name in ['gen', 'replace', 'update', 'convert', 'comment', 'snippet']:
            if sp_name in cmdarg[1:end_pos]:
                break
        else:
            # insert default in first position, this implies no
            # global options without a sub_parsers specified
            cmdarg.insert(1, 'gen')
    if '--version' in cmdarg[1:]:
        if '-v' in cmdarg[1:] or '--verbose' in cmdarg[1:]:
            return list_versions(pkg_name='cligen', version=None, pkgs=['ruamel.yaml'])
        print(__version__)
        return 0
    if '--help-all' in cmdarg[1:]:
        try:
            parsers[0].parse_args(['--help'])
        except SystemExit:
            pass
        for sc in parsers[1:]:
            print('-' * 72)
            try:
                parsers[0].parse_args([sc.prog.split()[1], '--help'])
            except SystemExit:
                pass
        sys.exit(0)
    args = parsers[0].parse_args(args=cmdarg[1:])
    for gl in ['verbose', 'comment', 'debug']:
        glv = getattr(args, '_gl_' + gl, None)
        if isinstance(getattr(args, gl, None), (DefaultVal, type(None))) and glv is not None:
            setattr(args, gl, glv)
        delattr(args, '_gl_' + gl)
        if isinstance(getattr(args, gl, None), DefaultVal):
            setattr(args, gl, getattr(args, gl).val)
    cls = getattr(importlib.import_module('cligen.cligen'), 'CligenLoader')
    obj = cls(args, config=config)
    funcname = getattr(args, 'subparser_func', None)
    if funcname is None:
        parsers[0].parse_args(['--help'])
    fun = getattr(obj, funcname + '_subcommand', None)  # type: ignore
    if fun is None:
        fun = getattr(obj, funcname)  # type: ignore
    ret_val = fun()
    if ret_val is None:
        return 0
    if isinstance(ret_val, int):
        return ret_val
    return -1

def list_versions(pkg_name: str, version: typing.Union[str, None], pkgs: typing.Sequence[str]) -> int:
    version_data = [
        ('Python', '{v.major}.{v.minor}.{v.micro}'.format(v=sys.version_info)),
        (pkg_name, __version__ if version is None else version),
    ]
    for pkg in pkgs:
        try:
            version_data.append(
                (pkg,  getattr(importlib.import_module(pkg), '__version__', '--'))
            )
        except ModuleNotFoundError:
            version_data.append((pkg, 'NA'))
        except KeyError:
            pass
    longest = max([len(x[0]) for x in version_data]) + 1
    for pkg, ver in version_data:
        print('{:{}s} {}'.format(pkg + ':', longest, ver))
    return 0


if __name__ == '__main__':
    sys.exit(main())
