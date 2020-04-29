
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
        self._jnt_names = [self._jnt_names[i] for i in self._jnt_index]
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

    def __str__(self):
        output = "Total Joints: " + str(len(self._jnt_names)) + "\n"

        for idx in range(len(self._jnt_names)):
            output += "\n"
            parent = self.get_parent_name(idx)
            output += parent + " => " + self._jnt_names[idx]

        return output
