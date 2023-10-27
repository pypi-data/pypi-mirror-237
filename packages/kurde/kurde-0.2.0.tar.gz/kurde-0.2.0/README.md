# kurde

Simple configuration language based on Python.

## Features

- Python syntax
- Flexible Enums
- Easily created nested dictionaries
- Direct addess to environment variables
- Calling/capturing shell commands
- Path manipulation
- Module `re` immediately available

## Concepts

Kurde is pure Python with some built-ins added for your convenience (see below).

After invoking your script, any JSON-serializable variable defined in the global scope will be serialized and printed to stdout.

Alternatively you can define `ROOT` variable in the global scope. It will be considered as the root object to be serialized.

After installing Kurde, command `kurde` becomes available. Use it as:
```sh
kurde path/to/your/script.py
```

For clarity it is recommended to add kurde in the shebang of your script: `#!/usr/bin/env kurde`.

For more information see examples below.

## Built-Ins

| Variable | Value      |
|----------|---------------|
| `Path`   | `pathlib.Path` |
| `Dict`   | `addict.Dict` |
| `Enum`   | `simplenum.Enum` |
| `enum`   | `simplenum` |
| `env`    | `addict.Dict(**os.environ)` |
| `cmd`    | `plumbum.local.cmd` |
| `re`     | `re` |

For reference see:
- [addict](https://github.com/mewwts/addict)
- [simple-enum](https://github.com/andrewcooke/simple-enum)
- [plumbum](https://plumbum.readthedocs.io/)

## Examples

### Simple Example

```python
#!/usr/bin/env kurde

user = dict(
    name = 'admin',
    password = 'admin123',
)
remotes = [
    '192.168.0.100',
    '192.168.0.101',
    '192.168.0.102',
]
timeout = 100
```

Renders as:
```json
{
  "user": {
    "name": "admin",
    "password": "admin123"
  },
  "remotes": [
    "192.168.0.100",
    "192.168.0.101",
    "192.168.0.102"
  ],
  "timeout": 100
}
```

### Advanced Example

```python
#!/usr/bin/env kurde

# Enum from `simple-enum` package is available.
# By default enum items are serialized by names.
class Color(Enum):
    red
    green
    blue
    white
    black

# Alternatively, enum items can be replaced by numbers assigned automatically.
class Priority(Enum, values=enum.from_zero):
    low
    medium
    high

# In the simple cases, standard dictionary is sufficient.
# It is serialized as JSON object.
theme = dict(
    foreground = Color.black,
    background = Color.green,
)

# Dictionary can be also created by assigning the the attributes.
# Dict comes from `addicts` package.
user = Dict()

# Environment variables can be accessed directly.
user.name = env.USER or 'admin'
user.full_name = "Tom Brown"

# Module re immediately available.
user.last_name = re.findall('[^ ]+', user.full_name)[-1]

# lists, dicts, sets are serialized as JSON arrays.
user.aliases = ('tommy', 'tbrown', 'brown')
user.nick = None

network = Dict()

# Non-existing attributes are created on the fly.
network.local.priority = Priority.medium

# Shell commands can be easily invoked.
# Behind `cmd` we get `plumbum.local.cmd`.
network.local.name = cmd.hostname().strip()

# pathlib.Path immediately available.
network.local.cert_path = Path(__file__).parent.absolute() / 'cert.pem'

# Closures and other constructs available.
network.remotes = {f"proxy{n}": f'192.168.0.{100 + n}' for n in range(3)}
network.remotes['localhost'] = '127.0.0.1'
```

Renders as:
```json
{
  "theme": {
    "foreground": "black",
    "background": "green"
  },
  "user": {
    "name": "kendo",
    "full_name": "Tom Brown",
    "last_name": "Brown",
    "aliases": [
      "tommy",
      "tbrown",
      "brown"
    ],
    "nick": null
  },
  "network": {
    "local": {
      "priority": 1,
      "name": "precision",
      "cert_path": "/home/kendo/wrk/kurde/examples/cert.pem"
    },
    "remotes": {
      "proxy0": "192.168.0.100",
      "proxy1": "192.168.0.101",
      "proxy2": "192.168.0.102",
      "localhost": "127.0.0.1"
    }
  }
}
```

### Example with ROOT defined

```python
#!/usr/bin/env kurde

min_value = 2
max_value = 6

ROOT = Dict()
ROOT.numbers = list(range(min_value, max_value+1))
```

Renders as:
```json
{
  "numbers": [
    2,
    3,
    4,
    5,
    6
  ]
}
```

## Disclaimer

Kurde doesn't do any sandboxing. Invoke the scripts only if you absolutely trust them. You are doing it on your own responsibility.

## Known Issues

There is an issue between addict and simplenum when calling `Dict` with enum items as arguments, e.g.:

```python
theme = Dict(
    foreground = Color.white,
    background = Color.green,
)
```
