import json
import numpy as np

import core.constants as const
from core.skeleton import Skeleton


class Meta(object):

    def __init__(self):

        self._unit = const.UNIT_MILIMETERS

        self._joints = {
            const.HIP: -1,
            const.RHIP: -1,
            const.RHIP_KNEE: -1,
            const.RKNEE: -1,
            const.RKNEE_ANKLE: -1,
            const.RANKLE: -1,
            const.RANKLE_FOOT: -1,
            const.RFOOT: -1,
            const.LHIP: -1,
            const.LHIP_KNEE: -1,
            const.LKNEE: -1,
            const.LKNEE_ANKLE: -1,
            const.LANKLE: -1,
            const.LANKLE_FOOT: -1,
            const.LFOOT: -1,
            const.SPINE1: -1,
            const.SPINE1_2: -1,
            const.SPINE2: -1,
            const.SPINE2_3: -1,
            const.SPINE3: -1,
            const.SPINE3_4: -1,
            const.SPINE4: -1,
            const.SPINE4_NECK: -1,
            const.NECK: -1,
            const.NOSE: -1,
            const.HEAD: -1,
            const.RSHOULDER: -1,
            const.RUPPERARM: -1,
            const.RSHOULDER_ELBOW: -1,
            const.RELBOW: -1,
            const.RELBOW_WRIST: -1,
            const.RWRIST: -1,
            const.RHAND: -1,
            const.RHAND_SITE1: -1,
            const.RHAND_SITE2: -1,
            const.RHAND_SITE3: -1,
            const.RHAND_SITE4: -1,
            const.LSHOULDER: -1,
            const.LUPPERARM: -1,
            const.LSHOULDER_ELBOW: -1,
            const.LELBOW: -1,
            const.LELBOW_WRIST: -1,
            const.LWRIST: -1,
            const.LHAND: -1,
            const.LHAND_SITE1: -1,
            const.LHAND_SITE2: -1,
            const.LHAND_SITE3: -1,
            const.LHAND_SITE4: -1
        }

        self._parents = {
            const.HIP: None,
            const.RHIP: const.HIP,

            const.RHIP_KNEE: const.RHIP,
            const.RKNEE: const.RHIP_KNEE,
            const.RKNEE_ANKLE: const.RKNEE,
            const.RANKLE: const.RKNEE_ANKLE,
            const.RANKLE_FOOT: const.RANKLE,
            const.RFOOT: const.RANKLE_FOOT,

            const.LHIP: const.HIP,
            const.LHIP_KNEE: const.LHIP,
            const.LKNEE: const.LHIP_KNEE,
            const.LKNEE_ANKLE: const.LKNEE,
            const.LANKLE: const.LKNEE_ANKLE,
            const.LANKLE_FOOT: const.LANKLE,
            const.LFOOT: const.LANKLE_FOOT,

            const.SPINE1: const.HIP,
            const.SPINE1_2: const.SPINE1,
            const.SPINE2: const.SPINE1_2,
            const.SPINE2_3: const.SPINE2,
            const.SPINE3: const.SPINE2_3,
            const.SPINE3_4: const.SPINE3,
            const.SPINE4: const.SPINE4,
            const.SPINE4_NECK: const.SPINE4,

            const.NECK: const.SPINE4_NECK,
            const.NOSE: const.NECK,
            const.HEAD: const.NOSE,

            const.RSHOULDER: const.NECK,
            const.RUPPERARM: const.RSHOULDER,
            const.RSHOULDER_ELBOW: const.RUPPERARM,
            const.RELBOW: const.RSHOULDER_ELBOW,
            const.RELBOW_WRIST: const.RELBOW,
            const.RWRIST: const.RELBOW_WRIST,
            const.RHAND: const.RWRIST,
            const.RHAND_SITE1: const.RHAND,
            const.RHAND_SITE2: const.RHAND,
            const.RHAND_SITE3: const.RHAND,
            const.RHAND_SITE4: const.RHAND,

            const.LSHOULDER: const.NECK,
            const.LUPPERARM: const.LSHOULDER,
            const.LSHOULDER_ELBOW: const.LUPPERARM,
            const.LELBOW: const.LSHOULDER_ELBOW,
            const.LELBOW_WRIST: const.LELBOW,
            const.LWRIST: const.LELBOW_WRIST,
            const.LHAND: const.LWRIST,
            const.LHAND_SITE1: const.LHAND,
            const.LHAND_SITE2: const.LHAND,
            const.LHAND_SITE3: const.LHAND,
            const.LHAND_SITE4: const.LHAND
        }

        self._cameras = [
            {
                "unit": const.UNIT_MILIMETERS,
                "id": None,
                "intrinsic": np.zeros((3, 3)).tolist(),
                "radial": np.zeros(3).tolist(),
                "tangential": np.zeros(3).tolist()
            }
        ]

    def dump_sample_meta(self, filename="sample"):

        with open("output/" + filename + ".json", 'w') as output_file:
            json.dump({
                "joints": self._joints,
                "cameras": self._cameras
            }, output_file)

    def parse_meta(self, meta_name):

        skeleton = Skeleton()

        with open(meta_name, 'r') as meta:
            json_data = json.load(meta)

            joints = json_data['joints']

            inc_names = []

            for name in joints.keys():
                assert name in self._joints, "Joint name not found"

                if joints[name] >= 0:
                    skeleton.add_joint(joints[name], name)

                    inc_names.append(name)

            skeleton.sort_bones()

            for name in inc_names:
                parent = self._get_parent(name, skeleton.get_joint_names())

                if parent is not None:
                    skeleton.add_bone(name, parent)

            meta.close()

        return skeleton

    def _get_parent(self, jnt_name, joints):
        parent = self._parents[jnt_name]

        while parent not in joints and parent is not None:
            parent = self._parents[parent]

        return parent
