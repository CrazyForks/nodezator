
### standard library imports

from string import Template

from inspect import signature, getsource


### local imports
from . import generaldefs, pygamedefs



CAPSULE_IDS_TO_CALLABLES_MAP = {

    ### general definitions

    "read_text_file": generaldefs.read_text_file,
    "write_text_file": generaldefs.write_text_file,
    "append_to_text_file": generaldefs.append_to_text_file,
    "read_binary_file": generaldefs.read_binary_file,
    "write_binary_file": generaldefs.write_binary_file,
    "append_to_binary_file": generaldefs.append_to_binary_file,
    "load_pyl_file": generaldefs.load_pyl_file,
    "save_as_pyl_file": generaldefs.save_as_pyl_file,
    "load_json_file": generaldefs.load_json_file,
    "save_as_json_file": generaldefs.save_as_json_file,
    "print_and_return": generaldefs.print_and_return,
    "return_untouched": generaldefs.return_untouched,
    "for_item_in_obj_pass": generaldefs.for_item_in_obj_pass,
    "perform_call": generaldefs.perform_call,
    "perform_attr_call": generaldefs.perform_attr_call,
    "tuple_from_args": generaldefs.tuple_from_args,
    "list_from_args": generaldefs.list_from_args,
    "set_from_args": generaldefs.set_from_args,
    "get_at_int": generaldefs.get_at_int,
    "get_at_string": generaldefs.get_at_string,
    "get_at_literal": generaldefs.get_at_literal,
    "namespace_from_exec": generaldefs.namespace_from_exec,
    "get_constant_returner": generaldefs.get_constant_returner,

    ### pygame-related definitions

    'color_surf_from_size': pygamedefs.color_surf_from_size,
    'color_surf_from_wh': pygamedefs.color_surf_from_wh,
    'get_pygame_constant': pygamedefs.get_pygame_constant,
    'blit_surf_a_onto_b': pygamedefs.blit_surf_a_onto_b,
    'get_positioned_rects': pygamedefs.get_positioned_rects,
    'unite_surfaces': pygamedefs.unite_surfaces,
    #'fill_surface': pygamedefs.fill_surface,
    'increase_surf_border': pygamedefs.increase_surf_border,
    'draw_border_on_surf': pygamedefs.draw_border_on_surf,
}

CAPSULE_IDS_TO_SIGNATURES_MAP = {
    capsule_id: signature(callable_obj)
    for capsule_id, callable_obj in CAPSULE_IDS_TO_CALLABLES_MAP.items()
}

CAPSULE_IDS_TO_SUBSTITUTION_CALLABLE_MAP = {
    "read_text_file": Template(
        """

with open(

  $filepath,
  mode='r',
  encoding=$encoding,
  errors=$errors,

) as f:

    $string = f.read()

""".strip()
    ).substitute,
    "write_text_file": Template(
        """

with open(
  $filepath,
  mode='w',
  encoding=$encoding,
  errors=$errors,
) as f:
    f.write($text)

$output = None

""".strip()
    ).substitute,
    "append_to_text_file": Template(
        """

with open(
  $filepath,
  mode='a',
  encoding=$encoding,
  errors=$errors,
) as f:
    f.write($text)

$output = None

""".strip()
    ).substitute,
    "read_binary_file": Template(
        """

with open($filepath, mode='rb') as f:
    $bytes_obj = f.read()

""".strip()
    ).substitute,
    "write_binary_file": Template(
        """

with open($filepath, mode='wb') as f:
    f.write($binary_data)

$output = None

""".strip()
    ).substitute,
    "append_to_binary_file": Template(
        """

with open($filepath, mode='ab') as f:
    f.write($binary_data)

$output = None

""".strip()
    ).substitute,
    "load_pyl_file": Template(
        """

with open($filepath, mode='r', encoding=$encoding) as f:
    $output = literal_eval(f.read())

""".strip()
    ).substitute,
    "save_as_pyl_file": Template(
        """

with open($filepath, mode='w', encoding=$encoding) as f:
    
    f.write(

        pformat(
          $obj,
          indent=$indent,
          width=$width,
          depth=$depth,
          compact=$compact,
        )

    )

$output = None

""".strip()
    ).substitute,
    "load_json_file": Template(
        """

with open($filepath, mode='r', encoding=$encoding) as f:

    $obj = load(

             f,
             cls=$cls,
             object_hook=$object_hook,
             parse_float=$parse_float,
             parse_int=$parse_int,
             parse_constant=$parse_constant,
             object_pairs_hook=$object_pairs_hook,
             **$kw,

           )

""".strip()
    ).substitute,
    "save_as_json_file": Template(
        """

with open($filepath, mode='w', encoding=$encoding) as f:
    
    dump(
      $obj,
      f,
      skipkeys=$skipkeys,
      ensure_ascii=$ensure_ascii,
      check_circular=$check_circular,
      allow_nan=$allow_nan,
      cls=$cls,

      indent=$indent,

      separators=$separators,
      default=$default,
      sort_keys=$sort_keys,
      **$kw,
    )

$output = None

""".strip()
    ).substitute,
    "print_and_return": Template(
        """

$obj_out = print($obj_in) or $obj_in

""".strip()
    ).substitute,
    "return_untouched": Template(
        """

$obj_out = $obj_in

""".strip()
    ).substitute,
    "for_item_in_obj_pass": Template(
        """

for _ in $obj:
    pass

$output = None

""".strip()
    ).substitute,
    "perform_call": Template(
        """
$func_return_value = $func(*$args, **$kwargs)
""".strip()
    ).substitute,
    "perform_attr_call": Template(
        """
$call_return_value = getattr($obj, $attr_name)(*$args, **$kwargs)
""".strip()
    ).substitute,
    "tuple_from_args": Template(
        """
$a_tuple = $args
""".strip()
    ).substitute,
    "list_from_args": Template(
        """
$a_list = list($args)
""".strip()
    ).substitute,
    "set_from_args": Template(
        """
$a_set = set($args)
""".strip()
    ).substitute,
    "get_at_int": Template(
        """
$item = $obj[$integer]
""".strip()
    ).substitute,
    "get_at_string": Template(
        """
$item = $obj[$string]
""".strip()
    ).substitute,
    "get_at_literal": Template(
        """
$item = $obj[$literal]
""".strip()
    ).substitute,
    "namespace_from_exec": Template(
        """

_vars = $variables
exec($python_source, _vars)
_d = {}
exec('', _d)
$namespace = {k:v for k, v in _vars.items() if k not in _d}

""".strip()
    ).substitute,
    "get_constant_returner": Template(
        """

$constant_returner = (lambda x: lambda y: x)($constant_value)

""".strip()
    ).substitute,
}

CAPSULE_IDS_TO_STLIB_IMPORT_MAP = {
    "load_pyl_file": "from ast import literal_eval",
    "save_as_pyl_file": "from pprint import pformat",
    "load_json_file": "from json import load",
    "save_as_json_file": "from json import dump",
}


CAPSULE_IDS_TO_3RDLIB_IMPORT_MAP = {
    'color_surf_from_size': "from pygame import Surface",
    'color_surf_from_wh': "from pygame import Surface",
    'get_pygame_constant': "from pygame import locals as pygame_ce_locals",
    'increase_surf_border': 'from pygame import Surface',
    'draw_border_on_surf': 'from pygame.draw import rect as draw_rect_on_surf',
}

CAPSULE_IDS_TO_STLIB_ANNOTATION_IMPORTS = {
    'load_json_file': 'from collections.abc import Callable',
    'save_as_json_file': 'from collections.abc import Callable',
    'for_item_in_obj_pass': 'from collections.abc import Iterator',
    'get_positioned_rects': 'from collections.abc import Iterable',
    'unite_surfaces': 'from collections.abc import Iterable',
}

CAPSULE_IDS_TO_3RDLIB_ANNOTATION_IMPORTS = {
    'color_surf_from_size': 'from pygame import Surface',
    'color_surf_from_wh': 'from pygame import Surface',
    'blit_surf_a_onto_b':  'from pygame import Surface',
    'unite_surfaces': 'from pygame import Surface',
    #'fill_surface': 'from pygame import Surface',
    #'fill_surface': 'from pygame import Rect',
    'increase_surf_border': 'from pygame import Surface',
    'draw_border_on_surf': 'from pygame import Surface',
}

PYGAME_RELATED_CAPSULE_IDS = frozenset((
    'color_surf_from_size',
    'color_surf_from_wh',
    'get_pygame_constant',
    'blit_surf_a_onto_b',
    'get_positioned_rects',
    'unite_surfaces',
    #'fill_surface',
    'increase_surf_border',
    'draw_border_on_surf',
))


CAPSULE_IDS_TO_SOURCE_VIEW_TEXT = {

    ## key: value pair

    capsule_id: (

        (
            (
                CAPSULE_IDS_TO_STLIB_IMPORT_MAP[capsule_id]
                + ("\n" * 2)
            )
            if capsule_id in CAPSULE_IDS_TO_STLIB_IMPORT_MAP
            else ''
        )
        + (
            (
                CAPSULE_IDS_TO_STLIB_ANNOTATION_IMPORTS[capsule_id]
                + ("\n" * 2)
            )
            if capsule_id in CAPSULE_IDS_TO_STLIB_ANNOTATION_IMPORTS
            else ''
        )
        + getsource(callable_obj)

    )

    ## source
    for capsule_id, callable_obj in CAPSULE_IDS_TO_CALLABLES_MAP.items()

    ## filtering
    if capsule_id not in PYGAME_RELATED_CAPSULE_IDS

}


CAPSULE_IDS_TO_SOURCE_VIEW_TEXT.update(

    ## (key, value) tuple

    (
        capsule_id,

        (
            (
                (
                    CAPSULE_IDS_TO_3RDLIB_IMPORT_MAP[capsule_id]
                    + ("\n" * 2)
                )
                if capsule_id in CAPSULE_IDS_TO_3RDLIB_IMPORT_MAP
                else ''
            )

            + (
                (
                    CAPSULE_IDS_TO_3RDLIB_ANNOTATION_IMPORTS[capsule_id]
                    + ("\n" * 2)
                )
                if capsule_id in CAPSULE_IDS_TO_3RDLIB_ANNOTATION_IMPORTS
                else ''
            )

            + getsource(callable_obj)
        )

    )

    ## source
    for capsule_id, callable_obj in CAPSULE_IDS_TO_CALLABLES_MAP.items()

    ## filtering
    if capsule_id in PYGAME_RELATED_CAPSULE_IDS

)

### when exporting/viewing graph as as the Python code equivalent

CAPSULE_IDS_TO_PYTHON_SOURCE = {
    capsule_id: getsource(callable_obj)
    for capsule_id, callable_obj in CAPSULE_IDS_TO_CALLABLES_MAP.items()
}
