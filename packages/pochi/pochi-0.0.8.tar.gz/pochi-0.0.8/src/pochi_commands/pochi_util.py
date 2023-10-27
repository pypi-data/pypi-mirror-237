import snowflake.connector
import os

from logs.manager import LoggingManager


class PochiUtil:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PochiUtil, cls).__new__(cls)
            cls._instance.init_data()
        return cls._instance

    def init_data(self):
        self.__connection = None

    def get_connection(self, options):
        has_errors = False
        try:
            if options.project_config.default_connection is None:
                LoggingManager.display_message(
                    "connection_name_issue",
                )
                has_errors = True
            else:
                if self.__connection is None:
                    self.__connection = snowflake.connector.connect(
                        user=options.project_config.default_connection.username,
                        password=options.project_config.default_connection.password,
                        account=options.project_config.default_connection.accountname,
                    )
        except snowflake.connector.Error as e:
            # raise Exception(f"Snowflake connection error: {e}")
            LoggingManager.display_message(
                "connection_issues",
                [
                    options.project_config.default_connection.accountname,
                    options.init.connection,
                ],
            )
            has_errors = True
        finally:
            return has_errors

    def execute_sql(self, sql_statement, with_output=False):
        has_errors = False
        try:
            cur = self.__connection.cursor().execute(sql_statement)
            if self.__connection.get_query_status(cur.sfqid).name != "SUCCESS":
                has_errors = True
        except Exception as e:
            LoggingManager.display_message(
                "script_issues",
                [
                    sql_statement,
                    e,
                ],
            )
            has_errors = True
        finally:
            if with_output:
                return has_errors, cur.fetchall()
            return has_errors

    def execute_sql_from_file(
        self, message_name, file_path, has_errors=False, query_logging=False
    ):
        try:
            if os.path.exists(file_path) and not has_errors:
                with open(file_path, "r") as sql_file:
                    LoggingManager.display_message(message_name, file_path)
                    for cur in self.__connection.execute_stream(
                        sql_file, remove_comments=True
                    ):
                        for ret in cur:
                            if query_logging:
                                LoggingManager.display_single_message("\n".join(ret))
                        if (
                            self.__connection.get_query_status(cur.sfqid).name
                            != "SUCCESS"
                        ):
                            has_errors = True
        except Exception as e:
            LoggingManager.display_message(
                "script_issues",
                [
                    file_path,
                    e,
                ],
            )
            has_errors = True
        finally:
            return has_errors
