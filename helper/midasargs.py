import argparse

import helper.actionhandler as handler


class MidasArgs(object):

    def __init__(self):
        self._parser = argparse.ArgumentParser()
        self._parser.add_argument(
            "-dm", "--dump-meta",
            default=None, type=str,
            help="Dump a sample meta file"
        )
        self._parser.add_argument(
            "-pm", "--parse-meta",
            default=None, type=str,
            help="Parse meta from meta file and generate skeleton"
        )

    def parse(self):
        args = self._parser.parse_args()

        if args.dump_meta is not None:
            handler.dump_meta(args.dump_meta)

        if args.parse_meta is not None:
            print(handler.parse_meta(args.parse_meta))
