# tpm_multicast_client

Listens to the TPM multicast stream and unpack the status dictionary using Jeff Hagen's `tpmdgram` code.

## Installation

To install with `pip` do

```console
pip install sdss-tpm-multicast-client
```

To install from source do

```console
poetry install
```

More information on developing with Poetry can be found [here](https://python-poetry.org).

## Usage

The library provides a single function, `listen_to_multicast`, that creates a connection to the TPM broadcast, unpacks the datagram, and passes it to a callback function. A basic example

```python
from pprint import pprint

from tpm_multicast_client import __version__, listen_to_multicast


def pprint_datagram(data: dict):
    pprint(data)

async def main():
    _, protocol = await listen_to_multicast(pprint_datagram)
    await protocol.run_forever()


if __name__ == "__main__":
    main()
```

The callback, `pprint_datagram` in this case, can be a function or a coroutine. In the former case it will be called with `loop.call_soon()`. In the latter the coroutine is scheduled as a task.

## CLI

The library provides a simple CLI script `tpm-multicast-client` that prints the output of the datagram to stdout. It's basically equivalent to the example above.
