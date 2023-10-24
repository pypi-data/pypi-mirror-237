# Teamscale Robot Plugin

This plugin allows you to record testwise coverage for the RobotFramework.

## Installation

You can install this package via `pip install teamscalerobotplugin`

## Usage

You can specify the plugin via the `--listener` option when executing your test suite.

```bash
robot --listener teamscalerobotplugin.TiaRobotListener;partition=PARTITION MyTests.robot
```

There are a number of parameters you can use to customize the plugin:

- `partition`
  - Mandatory. The partition in Teamscale for which to retrieve impacted tests and to which to upload testwise coverage.
    Must be the same partition as supplied to the JaCoCo agent.
- `url`
  - The URL on which the [JaCoCo Agent](https://docs.teamscale.com/howto/setting-up-profiler-tga/java/#using-the-teamscale-jacoco-agent) is listening.
  - DEFAULT: `http://localhost:7001/`
- `log_file`
  - The name of the file that should be used to write logs
  - DEFAULT: `./teamscale-robot-plugin.log`
- `log_level`
  - The [level](https://docs.python.org/3/library/logging.html#logging-levels) at which events should be logged to the log file.
  Errors are always logged to the console as well.
  - DEFAULT: `INFO`
- `partial`
  - Whether the produced testwise coverage report is partial or not.
  If not, then all tests not contained in the report are deleted from Teamscale.
  - DEFAULT: true

### Examples

```bash
# Using default values
robot --listener "teamscalerobotplugin.TiaRobotListener;partition=Robot Tests" MyTests.robot
```

```bash
# Enabling debug logs
robot --listener "teamscalerobotplugin.TiaRobotListener;partition=Robot Tests;log_level=DEBUG" MyTests.robot
```

```bash
# Setting a custom URL and log file
robot --listener "teamscalerobotplugin.TiaRobotListener;partition=Robot Tests;url=http://localhost:9999/;log_file=mylog.log" MyTests.robot
```

```bash
# Setting a custom URL and making the upload partial
robot --listener "teamscalerobotplugin.TiaRobotListener;partition=Robot Tests;url=http://localhost:9999/;partial=true" MyTests.robot
```

