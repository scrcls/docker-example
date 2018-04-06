# -*- coding:utf-8 -*-
import importme

from common.rdb import get_redis_client

import click
import logging


@click.group()
def cli():
        pass


def test():
    client = get_redis_client()
    result = client.incr('Script:Test')


COMMANDS = {
    'test': test,
}


if __name__ == '__main__':
    for cmd_name, func in COMMANDS.items():
        cli.command(cmd_name)(func)
    cli()
