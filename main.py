from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app = Ursina()

# Define a Voxel class.
# By setting the parent to scene and the model to 'cube' it becomes a 3d button.
obj = load_model("3.obj")

class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = 'brick-c.jpg',
            color = color.color(0, 0, random.uniform(.9, 1.0)),
            highlight_color = color.lime
        )

print(dir(Button))


def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position=self.position + mouse.normal)

            if key == 'right mouse down':
                destroy(self)

for z in range(8):
    for y in range(8):
        for x in range(8):
            voxel = Voxel(position=(x,0,z))
            object = Entity(model=obj, scale=(4,4,4))
            object.setPos(x,y,z)

def input(key):
    if key == 'left mouse down':
        hit_info = raycast(camera.world_position, camera.forward, distance=5)
        if hit_info.hit:
            Voxel(position=hit_info.entity.position + hit_info.normal)
    if key == "escape":
        quit()



player = FirstPersonController()
app.run()