import logging
import anywidget
import traitlets
from typing import Tuple, Callable, List, Optional
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)


def pylog(msg):
    """Helper to log msg to Python logger"""
    logger.info(msg)


def routeEventFromJs(event, data):
    pass


def routeEventToPy(event, data):
    pass


@dataclass
class WidgetFactory:
    """
    traits: Trait name, Type, JS On Change, Python On Change
    js_to_py_funcs: creates a js function with the str value, that calls the callable
    py_to_js_funcs:
    """

    model_name: str
    _traits: List[Tuple[str, object, Optional[Callable], Optional[str]]] = field(
        default_factory=list
    )
    _js_to_py_funcs: List[Tuple[str, Callable]] = field(default_factory=list)
    _py_to_js_funcs: List[Tuple[str, str]] = field(default_factory=list)
    _widget: anywidget.AnyWidget = field(init=False)

    def __post_init__(self):
        # dynamically create a class for the _widget because traits attach at an instance level.
        _DynamicClass = type(
            _HtmlJsWidget.__name__ + "_Dynamic",
            _HtmlJsWidget.__bases__,
            dict(_HtmlJsWidget.__dict__),
        )

        self._widget = _DynamicClass()  # type: ignore

        # register the Python logging helper
        self.add_js_to_py(js_func="pylog", py_func=pylog)

    def add_trait(
        self,
        name: str,
        initial_value: Optional[object],
        python_onchange: Optional[Callable] = None,
        js_onchange: Optional[str] = None,
    ):
        """
        js_onchange: Can be either a function name or a function definition (with braces).
        """
        self._traits.append((name, initial_value, python_onchange, js_onchange))
        if isinstance(initial_value, int):
            trait = traitlets.Int(initial_value).tag(sync=True)
            self._widget.add_traits(**{name: trait})
            setattr(self._widget, name, initial_value)
        elif isinstance(initial_value, float):
            trait = traitlets.Float(initial_value).tag(sync=True)
            self._widget.add_traits(**{name: trait})
            setattr(self._widget, name, initial_value)
        elif isinstance(initial_value, list):
            trait = traitlets.List(initial_value).tag(sync=True)
            self._widget.add_traits(**{name: trait})
            setattr(self._widget, name, initial_value)
        elif isinstance(initial_value, dict):
            trait = traitlets.Dict(initial_value).tag(sync=True)
            self._widget.add_traits(**{name: trait})
            setattr(self._widget, name, initial_value)
        else:
            trait = traitlets.Unicode(str(initial_value)).tag(sync=True)
            self._widget.add_traits(**{name: trait})
            setattr(self._widget, name, initial_value)

        if python_onchange is not None:
            self._widget.observe(python_onchange, names=name)

        if js_onchange is not None:
            js_frag = f"""
                model.on("change:{name}", () => {js_onchange});            
                """
            self._widget._js_change_listeners += js_frag  # type: ignore

    def add_js(self, js_code: str):
        self._widget._additional_js_functions += "\n"
        self._widget._additional_js_functions += js_code

    def add_js_to_py(self, js_func: str, py_func: Callable):
        """
        Creates a JS function that calls py_func.
        The JS function is added to globalThis.
        This is implemented as an event
        """
        js_frag = f"""
            export async function {js_func}(funcdata){{
                globalThis.{self.model_name}.send({{event: '{py_func.__name__}', data: funcdata}});
            }}
        """

        post_render_frag = f"""
            try{{
                        model.{js_func} = {js_func};
                        }}
            catch (error){{
            console.error(error)
            }}
            """

        self._widget._additional_js_functions += js_frag  # type: ignore
        self._widget._post_render_frags += post_render_frag  # type: ignore

        self._widget._python_function_map[py_func.__name__] = py_func  # type: ignore
        logger.info(f"Registering {js_func} => {py_func}")

    def add_py_to_js(
        self, js_func: str, js_impl: Optional[str] = None
    ) -> Callable[[str], None]:
        """Binds a python function to a JS function.
        This creates a JS function with the js_func name that takes a single dict object

        Args:
            py_func (Callable): _description_
            js_func (str): _description_
        """

        if js_impl is not None:
            self._widget._additional_js_functions += js_impl  # type: ignore

        self._widget._additional_js_functions += f"""\nfunctionMap.set('{js_func}', {js_func});\n"""  # type: ignore

        return lambda x: self._widget.call_js(js_func, x)  #  type: ignore

    def set_after_render_py(self, py_func: Callable[[object], None]):
        self.add_js_to_py(js_func="after_render_pycallback", py_func=py_func)

    def set_after_render_js(self, js_func: str):
        self._widget._additional_js_functions += (
            f"\nlet after_render_jscallback = {js_func}\n"
        )

    def get_widget(self) -> anywidget.AnyWidget:
        """Creates the widget. Don't modify the factory after creating the widget: can't add traits after widget
        is created"""
        self._widget.prepare_widget(self.model_name)  # type: ignore

        return self._widget


class _HtmlJsWidget(anywidget.AnyWidget):
    """After running, the"""

    _esm = None
    _css = None

    _js_change_listeners = ""
    _additional_js_functions = ""
    _post_render_frags = ""
    _python_function_map = {}

    def __init__(self):
        pass

    def route_message(self, f_name, data):
        if f_name not in self._python_function_map:
            logger.warning(f"Unknown python function {f_name=}")
        else:
            logger.info(f"Routing to {f_name=}")
            self._python_function_map[f_name](data)

    def _handle_custom_msg(self, data, buffers):
        # https://github.com/manzt/anywidget/issues/54
        logger.info(f"{self=}, {data=}, {buffers=}")

        if data is not None and "data" in data:
            data_val = data["data"]
        else:
            data_val = None
        if data is not None and "event" in data:
            event_val = data["event"]
        else:
            event_val = None

        self.route_message(f_name=event_val, data=data_val)

    def prepare_widget(self, model_name: str):
        logger.info(
            f"Preparing: {model_name=}: {self._js_change_listeners=}, {self._additional_js_functions=}"
        )
        self._esm = f"""
            let functionMap = new Map();

            {self._additional_js_functions}
            export function render({{ model, el }}) {{
                try{{
                    globalThis.{model_name} = model;

                    console.log("Setting msg:custom");
                    model.on("msg:custom", msg => {{
                        try{{
                            console.log(`Received message from Python: ${{JSON.stringify(msg)}}`);
                            //render_message(msg['type'], msg['body']);

                            
                            let functionName = msg["event"]
                            let data = msg["data"]
                            console.log("Calling ", functionName)
                            functionMap.get(functionName)(data);
                        }}
                        catch (error){{
                            console.error(error);
                        }}
                    }});

                    console.log("Setting _js_change_listeners");
                    {self._js_change_listeners}


                    console.log("Setting _post_render_frags");
                    {self._post_render_frags}

                    // Send signal that js layer is done
                    if ( typeof after_render_pycallback !== 'undefined'){{
                        try{{
                            console.log("Calling after_render_pycallback");
                            after_render_pycallback("done");
                        }} catch (error){{
                            console.error(error);
                        }}

                    }} else {{
                        console.log("after_render_pycallback is undefined");
                    }}

                    if ( typeof after_render_jscallback !== 'undefined' ){{
                        try{{
                            console.log("Calling after_render_jscallback");
                            after_render_jscallback();
                        }} catch (error){{
                            console.error(error);
                        }}
                    }} else {{
                        console.log("after_render_jscallback is undefined");
                    }}

                    let event = new Event('{model_name}_complete');
                    globalThis.dispatchEvent(event);
                }}
                catch (error){{
                    console.error(error);
                }}
            }}




        """
        anywidget.AnyWidget.__init__(self=self)

    def call_js(self, f_name, data) -> None:
        self.send({"event": f_name, "data": data})
