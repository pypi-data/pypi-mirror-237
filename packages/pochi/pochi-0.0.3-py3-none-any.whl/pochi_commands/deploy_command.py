import os
from logs.manager import LoggingManager
from pochi_commands.pochi_util import pochi_util


class DeployCommand(object):
    def __init__(self, parser):
        # print('deploy command')
        deploy_parser = parser.add_parser(
            "deploy", help="Deploy as provider or consumer"
        )
        deploy_parser.add_argument(
            "--provider", action="store_true", help="Deploy as a provider"
        )
        deploy_parser.add_argument(
            "--consumer", action="store_true", help="Deploy as a consumer"
        )

    def get_help_text(self):
        help_text = """pochi deploy [--consumer|--provider]
    Create an application package and generate a new version/patch in the target Snowflake account specified in config/project.toml.
    This command automatically runs the build command, and then executes the deployment SQL scripts to create an Application Package,
    set up shared content, push application code into a stage, and add a version/patch.
        
    Options:
        --consumer                      Updates only the native app application code files and creates a new patch.
        --provider                      Updates only the native app package or other objects in the provider account.
"""
        return help_text

    def execute(self, options):
        has_errors = False
        LoggingManager.display_message("pochi_header", "DEPLOY")
        if options.project_config.default_connection is None:
            LoggingManager.display_message("connection_file_missing")
            has_errors = True
        else:
            has_errors = pochi_util.get_connection(options)
        if not has_errors:
            if options.deploy.consumer:
                has_errors = self.__deployment_sequence(
                    "application version code",
                    options,
                    False,
                    False,
                    True,
                    True,
                    True,
                    has_errors,
                )
            elif options.deploy.provider:
                has_errors = self.__deployment_sequence(
                    "provider side code",
                    options,
                    True,
                    True,
                    False,
                    False,
                    False,
                    has_errors,
                )
                LoggingManager.display_message(
                    "deployment_info",
                    [
                        "provider side code",
                        options.project_config.default_connection.accountname,
                        options.init.connection,
                    ],
                )
            else:
                has_errors = self.__deployment_sequence(
                    "full application package",
                    options,
                    True,
                    True,
                    True,
                    True,
                    True,
                    has_errors,
                )

        LoggingManager.display_message("closing_section")
        LoggingManager.display_message(
            "pochi_sucess", ["DEPLOY", "FAILED" if has_errors else "SUCCESS"]
        )

    def __deployment_sequence(
        self,
        deployment,
        options,
        deployment_preinstall_scripts,
        deployment_app_package_def,
        deployment_version_code,
        deployment_postinstall_scripts,
        app_package_info,
        has_errors=False,
    ):
        LoggingManager.display_message(
            "deployment_info",
            [
                deployment,
                options.project_config.default_connection.accountname,
                options.project_config.init_default_connection,
            ],
        )
        if deployment_preinstall_scripts:
            has_errors = pochi_util.execute_sql_from_file(
                "deployment_preinstall_scripts",
                os.path.join(
                    "generated", "deployment", "deploy_preinstall_objects.sql"
                ),
                has_errors,
            )
        if deployment_app_package_def:
            has_errors = pochi_util.execute_sql_from_file(
                "deployment_app_package_def",
                os.path.join(
                    "generated", "deployment", "deploy_application_package.sql"
                ),
                has_errors,
            )

        if deployment_version_code:
            has_errors = pochi_util.execute_sql_from_file(
                "deployment_version_code",
                os.path.join("generated", "deployment", "deploy_versioned_code.sql"),
                has_errors,
            )
        if deployment_postinstall_scripts:
            has_errors = pochi_util.execute_sql_from_file(
                "deployment_postinstall_scripts",
                os.path.join(
                    "generated", "deployment", "deploy_postinstall_objects.sql"
                ),
                has_errors,
            )

        if app_package_info:
            LoggingManager.display_message(
                "app_package_info",
                [
                    options.project_config.application_package_name,
                    options.project_config.application_version_name,
                    "1",
                ],
            )

        return has_errors
