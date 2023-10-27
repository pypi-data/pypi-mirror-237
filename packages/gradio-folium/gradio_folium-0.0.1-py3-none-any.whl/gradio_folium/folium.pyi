from gradio.components.base import Component

from gradio.events import Dependency

class Folium(Component):
    data_model = FileData

    def __init__(self, value: Any = None,
                 *, 
                 height: int | None = None,
                 label: str | None = None,
                 container: bool = True,
                 scale: int | None = None,
                 min_width: int | None = None,
                 visible: bool = True,
                 elem_id: str | None = None,
                 elem_classes: list[str] | str | None = None, 
                 render: bool = True,
                 root_url: str | None = None,
                 _skip_init_processing: bool = False,
                 load_fn: Callable[..., Any] | None = None,
                 every: float | None = None):
        super().__init__(value, label=label, info=None, show_label=True,
                         container=container, scale=scale, min_width=min_width,
                         visible=visible, elem_id=elem_id, elem_classes=elem_classes,
                         render=render, root_url=root_url,
                         _skip_init_processing=_skip_init_processing,
                         load_fn=load_fn, every=every)
        self.height = height
    def preprocess(self, x):
        return x

    def postprocess(self, x: Map):
        if not x:
            return None
        with NamedTemporaryFile(suffix=".html", delete=False) as tmp:
            x.save(tmp.name)
            return FileData(name=tmp.name, is_file=True)

    def example_inputs(self):
        return {"info": "Do not use as input"}

    def api_info(self):
        return {"type": {}, "description": "any valid json"}