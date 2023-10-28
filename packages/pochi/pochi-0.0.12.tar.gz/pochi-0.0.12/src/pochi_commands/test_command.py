import os
import sys
from logs.manager import LoggingManager
from pochi_commands.pochi_util import PochiUtil
from templates.manager import TemplateManager


class TestCommand(object):
    def __init__(self, parser):
        # print('test command')
        parser.add_parser("test", help="Run tests")
        self.pochi_util = PochiUtil()

    def get_help_text(self):
        help_text = """pochi test
    Run the all of the test suites defined in the test directory.
"""
        return help_text

    def __get_footer(self, has_errors):
        LoggingManager.display_message("closing_section")
        LoggingManager.display_message(
            "pochi_sucess", ["TEST", "FAILED" if has_errors else "SUCCESS"]
        )

    def execute(self, options):
        has_errors = False
        LoggingManager.display_message("pochi_header", "TEST")
        has_errors = self.pochi_util.get_connection(options)

        if has_errors:
            self.__get_footer(has_errors=has_errors)
            sys.exit()

        dict_project_config = vars(options.project_config)
        template_manager = TemplateManager(dict_project_config)

        os.makedirs(os.path.join("generated", "test"), exist_ok=True)

        list_test_suites = sorted(os.listdir("test"))
        last_list_test_suites = len(list_test_suites) - 1
        for index, testsuite in enumerate(list_test_suites):
            if os.path.isdir(os.path.join("test", testsuite)):
                # this is the test suite.
                test_setup_sql = ""
                test_teardown_sql = ""
                test_code_sql = ""

                for file in sorted(os.listdir(os.path.join("test", testsuite))):
                    with open(os.path.join("test", testsuite, file), "r") as sql_input:
                        if file == "setup.sql":
                            test_setup_sql = sql_input.read() + "\n"
                            test_setup_sql = test_setup_sql
                        elif file == "teardown.sql":
                            test_teardown_sql = sql_input.read() + "\n"
                            test_teardown_sql = test_teardown_sql
                        elif file.startswith("test"):
                            test_code_sql += sql_input.read() + "\n"
                            test_code_sql = test_code_sql

                test_suite_file = os.path.join("generated", "test", testsuite + ".sql")
                with open(test_suite_file, "w") as sql_output:
                    sql_output.write(
                        template_manager.render_template(
                            test_setup_sql + test_code_sql + test_teardown_sql
                        )
                    )

                LoggingManager.display_message("running_test", testsuite)
                test_suite_has_errors = self.pochi_util.execute_sql_from_file(
                    test_suite_file, query_logging=True
                )

                has_errors = test_suite_has_errors or has_errors

                LoggingManager.display_message(
                    "test_suite_status",
                    [testsuite, "FAILED" if test_suite_has_errors else "SUCCESS"],
                )
                if index != last_list_test_suites:
                    LoggingManager.display_single_message("")

        self.__get_footer(has_errors=has_errors)
