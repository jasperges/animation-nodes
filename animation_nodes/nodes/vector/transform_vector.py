import bpy
from bpy.props import *
from ... base_types import AnimationNode, AutoSelectVectorization

class TransformVectorNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_TransformVectorNode"
    bl_label = "Transform Vector"

    useVectorList = BoolProperty(default = False, update = AnimationNode.updateSockets)

    def create(self):
        self.newInputGroup(self.useVectorList,
            ("Vector", "Vector", "vector"),
            ("Vector List", "Vectors", "vectors", dict(dataIsModified = True)))

        self.newInput("Matrix", "Matrix", "matrix")

        self.newOutputGroup(self.useVectorList,
            ("Vector", "Vector", "transformedVector"),
            ("Vector List", "Vectors", "vectors"))

        vectorization = AutoSelectVectorization()
        vectorization.input(self, "useVectorList", self.inputs[0])
        vectorization.output(self, self.outputs[0], dependencies = ["useVectorList"])
        self.newSocketEffect(vectorization)

    def getExecutionCode(self):
        if self.useVectorList:
            return "animation_nodes.math.transformVector3DList(vectors, matrix)"
        else:
            return "transformedVector = matrix * vector"