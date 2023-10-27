import os
import logging

from ..kore import App
from .. import krypt
from ..krypt import krypt_functions
from ._kust import KustApp
from ._kube import KubeKonfig

logger = logging.getLogger(__name__)


class KubeCli(krypt.KryptCli):
    def __init__(self, *, app_class=KustApp):
        super().__init__()
        self._app_class = app_class
        self.add_subcommand(files, [], aliases=["f"])
        self.add_subcommand(build, [], aliases=["b"])
        self.add_subcommand(diff, [], aliases=["d"])
        self.add_subcommand(apply, [], aliases=["a"])
        cmd = self.add_subcommand(test, [], aliases=["t"])
        cmd.add_argument(
            "-e",
            "--expected-output",
            help="file with expected output of build",
            action="store",
            default=None,
        )
        cmd = self.add_subcommand(testupdate, [], aliases=["tu"])
        cmd.add_argument(
            "-e",
            "--expected-output",
            help="file with expected output of build",
            action="store",
            default=None,
        )

    def get_packages(self):
        return ["kreate-kube"]

    def kreate_konfig(self, filename: str) -> KubeKonfig:
        return KubeKonfig(filename, dict_=self.calc_dict(), inkludes=self.args.inklude)

    def kreate_app(self) -> KustApp:
        return self._app_class(self.konfig())

    def default_command(self):
        files(self)


def kreate_files(cli: KubeCli) -> KustApp:
    app: App = cli.app()
    app.kreate_komponents()
    app.kreate_files()
    return app


def files(cli: KubeCli) -> None:
    """kreate all the files (default command)"""
    kreate_files(cli)


def build(cli: KubeCli) -> None:
    """output all the resources"""
    app = kreate_files(cli)
    cmd = f"kustomize build {app.target_path}"
    logger.info(f"running: {cmd}")
    os.system(cmd)


def diff(cli: KubeCli) -> None:
    """diff with current existing resources"""
    app = kreate_files(cli)
    cmd = (
        f"kustomize build {app.target_path} "
        f"| kubectl --context={app.env} -n {app.namespace} diff -f - "
    )
    logger.info(f"running: {cmd}")
    os.system(cmd)


def apply(cli: KubeCli) -> None:
    """apply the output to kubernetes"""
    app = kreate_files(cli)
    cmd = f"kustomize build {app.target_path} " "| kubectl apply --dry-run -f - "
    logger.info(f"running: {cmd}")
    os.system(cmd)


def test(cli: KubeCli) -> None:
    """test output against expected-output-<app>-<env>.out file"""
    # Do not dekrypt secrets for testing
    krypt_functions._dekrypt_testdummy = True
    app = kreate_files(cli)
    expected = (
        cli.args.expected_output
        or f"{app.konfig.dir}/expected-output-{app.appname}-{app.env}.out"
    )
    cmd = f"kustomize build {app.target_path} | diff {expected} -"
    logger.info(f"running: {cmd}")
    os.system(cmd)


def testupdate(cli: KubeCli) -> None:
    """update expected-output-<app>-<env>.out file"""
    # Do not dekrypt secrets for testing
    krypt_functions._dekrypt_testdummy = True
    app = kreate_files(cli)
    expected = (
        cli.args.expected_output
        or f"{app.konfig.dir}/expected-output-{app.appname}-{app.env}.out"
    )
    cmd = f"kustomize build {app.target_path} >{expected}"
    logger.info(f"running: {cmd}")
    os.system(cmd)
