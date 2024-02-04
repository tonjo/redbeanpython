# A generic, single database configuration.

[alembic]
# path to migration scripts
script_location = ${migrations_dir}

# sys.path path, will be prepended to sys.path if present.
# defaults to the current working directory.
prepend_sys_path = .

version_path_separator = os  # Use os.pathsep. Default configuration used for new projects.

# Put your db dsn here.
# Do not store credentials directly.
# Use environment variables instead.
sqlalchemy.url = %(DB_DSN)s

# Logging configuration
[loggers]
keys = root,sqlalchemy,alembic

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARN
handlers = console
qualname =

[logger_sqlalchemy]
level = WARN
handlers =
qualname = sqlalchemy.engine

[logger_alembic]
level = INFO
handlers =
qualname = alembic

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
datefmt = %H:%M:%S