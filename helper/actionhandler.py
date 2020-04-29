from core.meta import Meta


def dump_meta(filename):
    Meta().dump_sample_meta(filename)


def parse_meta(filename):
    return Meta().parse_meta(filename)
