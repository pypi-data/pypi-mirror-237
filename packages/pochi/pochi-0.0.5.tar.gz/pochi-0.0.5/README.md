# Pochi - a Snowflake Native App Build Automation Tool

## Important
This application is not part of the Snowflake Service and is governed by the terms in LICENSE, unless expressly agreed to in writing.  You use this application at your own risk, and Snowflake has no obligation to support your use of this application.

## Overview
Pochi is a Command-Line Interface (CLI) tool that allows a user to create, build, deploy, and test Snowflake native applications with simple commands. Pochi is built using the Snowflake Connector for Python.

## Install Pochi
To use Pochi, you need the following:
1. Python (>= 3.10)
2. SnowCLI or SnowSQL

To install Pochi, run this command in a terminal:
```
% pip install pochi
```

## Pochi CLI Commands

### Initialize a Pochi Native App Project Directory
```
pochi init [--name=<application_package_name>][--version=<application_version_name>] 
           [--connection=<default_connection>][--force]
```
|Options|Description|
|-------|-----------|
|`--name=<application_package_name>`|Create a new directory with the specified name in the current directory, and create the project in it|
|`--version=<application_version_name>`|Set the application_version_name in config/project.toml|
|`--connection=<default_connection>`|Set the default_connection name in config/project.toml; the name should exist in a connection file for SnowCLI or SnowSQL|
|`--force`|Replace an existing project directory with default templates|

This command creates a template native app project with default directory structure in the current directory.

### Add or Update Project Configuration
```
pochi config [--name=<parameter_name>][--value=<parameter_value>] 
```

Project configuration parameters are defined in config/project.toml. You can edit the file directly to add or update project configuration parameters, or you can use this command on the command-line.
* If `<parameter_name>` exists in `config/project.toml`, the value is updated directly
* If `<parameter_name>` does not exist in `config/project.toml`, then it is then added.
* Parameter name and value are case-sensitive.

The project configuration parameters can be referenced directly in your SQL files for parameter substitution.
To use parameter substitution in your SQL files, use `{parameter_name}` in your SQL commands.

### Build the Application Artifacts and Generate Deployment Scripts
```
pochi build
```

This command performs the following actions
* creates the `generated` output directory in the current directory
* creates Snowflake artifacts with the application code/resource files in the `generated/app` directory
* creates SQL deployment scripts in the `generated/deployment` directory to run preinstall SQLs, create an application package and its objects, upload the application code/resource files, create a version or patch, and run postinstall SQLs

Note: This target is automatically run when you run `pochi deploy`. You can use `pochi build` to examine the generated output files without automatically deploying them to the target Snowflake account.

You can use this target along with `clean`, `deploy`, and `test`. When multiple targets are specified, Pochi always runs the targets in the following order: `clean`, `build`, `deploy`, and `test`.

### Deploy the Application Package to Snowflake
```
pochi deploy [--consumer|--provider]
```
| Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|Description|
|----------------- |-----------|
| `--consumer`     |If specified, deploy only uploads the application code/resource files to create a version or patch, and executes the postinstall SQL file (if applicable).|
| `--provider`     |If specified, deploy only executes the preinstall SQL file (if applicable) and creates an application package and its objects.|

This command automatically runs the build target to generate the application artifacts and the SQL deployment scripts, and then it connects to the target Snowflake account to perform the following actions:
* Executes `generated/deployment/deploy_preinstall_objects.sql`,
* Executes `generated/deployment/deploy_application_package.sql`,
* Executes `generated/deployment/deploy_versioned_code.sql`,
* Executes `generated/deployment/deploy_postinstall_objects.sql`

You can use this target along with `clean`, `build`, and `test`. When multiple targets are specified, Pochi always runs the targets in the following order: `clean`, `build`, `deploy`, and `test`.


### Run Test Suites on Snowflake
```
pochi test [--tests=<testsuite>[.<testname>][,...]]
```
| Options&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|Description|
|----------------- |-----------|
| `--tests=<testsuite>[.<testname>][,...]`     |If specified, only the test suites and/or test names in a test suite are run. By default, all test suites are run.|


This command creates and runs the test suites defined in the `test` directory against the target Snowflake account. By default, a sample test suite testsuite1 is included in the project. It is a basic test suite with a `setup.sql`, `test01.sql`, and `teardown.sql`. When the test suite is run, the order of SQL execution is:
1. the `setup.sql`,
2. all of the test scripts in alphanumeric order, and
3. then the `teardown.sql`.

The default test verifies that an `APPLICATION` object can be created from an `APPLICATION PACKAGE` successfully. It does not validate functionality or correctness.

* setup.sql and teardown.sql are optional
* You can add add more tests in a test suite by creating SQL files with a prefix of "`test`"
* You can create more test suites by adding directories in the `test` directory




You can use this target along with `clean`, `build`, and `deploy`. When multiple targets are specified, Pochi always runs the targets in the following order: `clean`, `build`, `deploy`, and `test`.

### Clean the Project
```
pochi clean
```

This command drops the application package in the target Snowflake account and deletes the `generated` output directory in the current directory.

You can use this target along with `build`, `deploy`, and `test`. When multiple targets are specified, Pochi always runs the targets in the following order: `clean`, `build`, `deploy`, and `test`.

