
class Skeleton(object):

    def __init__(self):
        super(Skeleton, self).__init__()
        self._jnt_names = []
        self._jnt_index = []
        self._parents = []
        self._sorted = False

    def add_joint(self, index, name):
        self._jnt_names.append(name)
        self._jnt_index.append(index)

    def add_bone(self, jnt_name, parent_name):
        assert self._sorted, "Sort the joints first"
        joint_idx = self._jnt_names.index(jnt_name)
        parent_idx = self._jnt_names.index(parent_name)
        self._parents[joint_idx] = parent_idx

    def sort_bones(self):
        sorted_jnt_names = ['']*len(self._jnt_index)
        for i in range(len(self._jnt_index)):
            sorted_jnt_names[self._jnt_index[i]] = self._jnt_names[i]

        self._jnt_names = sorted_jnt_names
        self._parents = [-1]*len(self._jnt_names)
        self._sorted = True

    def get_joint_indices(self):
        return self._jnt_index

    def get_joint_names(self):
        return self._jnt_names

    def get_parent_name(self, jnt_idx):
        parent = self._parents[jnt_idx]

        if parent >= 0:
            return self._jnt_names[parent]
        else:
            return "null"

    def get_parent_by_idx(self, jnt_idx):
        return self._parents[jnt_idx]

    def get_parent_by_name(self, jnt_name):
        jnt_idx = self._jnt_names.index(jnt_name)
        return self._parents[jnt_idx]

    def get_next_parent(self, idx, available_joints):
        parent = self._parents[idx]

        while parent not in available_joints and parent != -1:
            parent = self._parents[parent]

        return parent

    def pick_joints_by_names(self, jnt_names):
        joints = []
        parents = []
        left = []
        right = []

        for name in jnt_names:
            joints.append(self._jnt_names.index(name))

        for idx in joints:
            parents.append(self.get_next_parent(idx, joints))

        for i_joint in range(len(joints)):
            if self._jnt_names[joints[i_joint]].startswith("L"):
                left.append(i_joint)
            elif self._jnt_names[joints[i_joint]].startswith("R"):
                right.append(i_joint)

        parents = [joints.index(i) if i >= 0 else -1 for i in parents]

        return {
            "joints": joints,
            "parents": parents,
            "left": left,
            "right": right,
            "names": jnt_names
        }

    def __str__(self):
        output = "Total Joints: " + str(len(self._jnt_names)) + "\n"

        for idx in range(len(self._jnt_names)):
            output += "\n"
            parent = self.get_parent_name(idx)
            output += parent + " => " + self._jnt_names[idx]

        return output
