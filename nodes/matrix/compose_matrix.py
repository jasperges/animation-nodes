import bpy
from ... base_types.node import AnimationNode

class ComposeMatrix(bpy.types.Node, AnimationNode):
    bl_idname = "an_ComposeMatrix"
    bl_label = "Compose Matrix"
    isDetermined = True

    def create(self):
        self.inputs.new("an_VectorSocket", "Translation", "translation")
        self.inputs.new("an_VectorSocket", "Rotation", "rotation")
        self.inputs.new("an_VectorSocket", "Scale", "scale").value = [1, 1, 1]
        self.outputs.new("an_MatrixSocket", "Matrix", "matrix")

    def getExecutionCode(self):
        return "matrix = animation_nodes.utils.math.composeMatrix(translation, rotation, scale)"
