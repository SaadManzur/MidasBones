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
        self._parser.add_argument(
            "-pj", "--pick-joints",
            default=None, type=str,
            help="Pick a subset of joints from a json file"
        )
        self._parser.add_argument(
            "-pd", "--plot-dummy",
            default=False, type=bool,
            help="Plot dummy skeleton from picked joints"
        )

    def parse(self):
        skeleton = None

        args = self._parser.parse_args()

        if args.dump_meta is not None:
            handler.dump_meta(args.dump_meta)

        if args.parse_meta is not None:
            skeleton = handler.parse_meta(args.parse_meta)

        if args.pick_joints is not None:
            assert skeleton is not None, \
                "You have to parse meta to generate skeleton first."

            print(handler.pick_joints(skeleton, args.pick_joints))

        if args.plot_dummy:
            handler.plot_dummy()
