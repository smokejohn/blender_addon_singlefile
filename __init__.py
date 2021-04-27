##
##  GPL License
##
##  Blender Addon | ADDONNAME
##  Copyright (C) 2021  AUTHORNAME
##
##  This program is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.
##
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##
##  You should have received a copy of the GNU General Public License
##  along with this program.  If not, see <https://www.gnu.org/licenses/>.

bl_info = {
        "name": "AddonName",
        "author": "AuthorName",
        "version": (0, 1),
        "blender": (2, 80, 0),
        "location": "3D View Sidebar (Hotkey: N)",
        "description": "Describe me here",
        "category": "Utility",
        "wiki_url": "Wiki url here",
        }

import bpy
from bpy.types import AddonPreferences, Operator, Panel, PropertyGroup
from bpy.props import BoolProperty, CollectionProperty, EnumProperty, PointerProperty, StringProperty, FloatProperty


# use your addon name initials as prefix (AddonName = AN, MyTools = MT)
class AN_Properties(PropertyGroup):
    example_text: StringProperty(default='example')
    example_number: FloatProperty(default=0.02, min=0.0, unit='LENGTH')

class AN_PT_Main(Panel):
    """ Main AddonName Panel """

    bl_idname = "AN_PT_Main"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "AddonName"
    bl_category = "CategoryTabName"

    def draw(self, context):
        scene = context.scene
        layout = self.layout

        row = layout.row()
        row.prop(scene.addonname, 'example_text')
        row = layout.row()
        row.prop(scene.addonname, 'example_number')
        row = layout.row()
        row.operator('an.base', text='Test Operator')

class AN_OP_Base(Operator):
    """ Base Operator """
    bl_idname = 'an.base'
    bl_label = 'Base Operator'
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # add your code here
        return {'FINISHED'}

classes = (
        AN_OP_Base,
        AN_PT_Main,
        )

def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    bpy.types.Scene.addonname = PointerProperty(type=AN_Properties)

def unregister():
    from bpy.utils import unregister_class
    for cls in classes:
        unregister_class(cls)

    del bpy.types.Scene.addonname
