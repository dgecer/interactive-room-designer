import json


def save_scene(objects, filename):

    data = []

    for obj in objects:

        item = {

            "type": obj.__class__.__name__,

            "x": obj.x,
            "y": obj.y,

            "color": obj.color,

            "rotation": getattr(
                obj,
                "rotation",
                0
            )
        }

        if hasattr(obj, "width"):

            item["width"] = obj.width

        if hasattr(obj, "height"):

            item["height"] = obj.height

        if hasattr(obj, "x2"):

            item["x2"] = obj.x2

        if hasattr(obj, "y2"):

            item["y2"] = obj.y2

        data.append(item)

    with open(filename, "w") as file:

        json.dump(
            data,
            file,
            indent=4
        )


def load_scene(filename):

    with open(filename, "r") as file:

        return json.load(file)