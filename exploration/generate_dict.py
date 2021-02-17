from json import dump
from sys import argv
from xml.etree import ElementTree as et

DEFAULT_FILE = 'data/ceesim/NSIN_Test_Scenario_Export.xml'
DEFAULT_EXPORT = 'exploration/definitions.json'
PRINT = True
DATATYPES = {
    bool: 'bool',
    float: 'float',
    int: 'int',
    'NoneType': None,
    str: 'str'
}


def determine_datatype(it: str) -> type:
    if len(it) == 0:
        return 'NoneType'
    if it in {'true', 'false', '1', '0'}:
        return bool
    try:
        fl = float(it)
        ir = int(fl)
        if fl == ir:
            return int
        else:
            return float
    except:
        return str


def traverse_subtree(parent: et.Element, indent=0) -> dict:
    data = dict()
    for child in parent:
        if child.text:
            text = child.text.strip()
        if PRINT:
            print(f'{"* " * indent}{child.tag} {f"({text})" if text else ""}')
        if text:
            data[child.tag] = DATATYPES[determine_datatype(text)]
        else:
            data[child.tag] = traverse_subtree(child, indent + 1)
    return data


def traverse_tree(fp: str) -> dict:
    it = et.iterparse(fp)
    for _, el in it:
        if '}' in el.tag:
            el.tag = el.tag.split('}', 1)[1]
        for at in list(el.attrib.keys()):
            if '}' in at:
                newat = at.split('}', 1)[1]
                el.attrib[newat] = el.attrib[at]
                del el.attrib[at]
    root = it.root
    data = dict()
    if PRINT:
        print(root.tag)
    data[root.tag] = traverse_subtree(root)
    return data


def traverse_and_save(fp: str, exp: str):
    data = traverse_tree(fp)
    dump(data, open(exp, 'w'), sort_keys=True, indent=4)


if __name__ == '__main__':
    file = argv[1] if len(argv) > 1 else DEFAULT_FILE
    export = argv[2] if len(argv) > 2 else DEFAULT_EXPORT
    traverse_and_save(file, export)
