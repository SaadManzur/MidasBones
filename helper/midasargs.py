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
        self._parser.add_argument(
            "-ppj", "--plot-picked-joints",
            default=False, type=bool,
            help="Plot picked joints skeleton"
        )

    def parse(self):
        skeleton = None
        picked_joints = None

        args = self._parser.parse_args()

        if args.dump_meta is not None:
            handler.dump_meta(args.dump_meta)

        if args.parse_meta is not None:
            skeleton = handler.parse_meta(args.parse_meta)

        if args.pick_joints is not None:
            assert skeleton is not None, \
                "You have to parse meta to generate skeleton first."

            picked_joints = handler.pick_joints(skeleton, args.pick_joints)

        if args.plot_dummy:
            handler.plot_dummy()

        elif args.plot_picked_joints:
            assert picked_joints is not None, \
                "You need to pick joints first"

            handler.plot_picked_joints(
                picked_joints['joints'],
                picked_joints['parents'],
                picked_joints['left'],
                picked_joints['right'],
                picked_joints['names']
            )
