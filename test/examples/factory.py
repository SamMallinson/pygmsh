#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Check factory setup.
'''
import pygmsh as pg


def generate():
    geom = pg.Geometry()

    if geom.get_gmsh_major() == 3:
        # factories are supported only in gmsh 3
        geom.set_factory("OpenCASCADE")
        geom.add_box(0, 1, 0, 1, 0, 1, 1.0)
        geom.set_factory("Built-in")
        geom.set_factory("OpenCASCADE")
    else:
        geom.add_box(0, 1, 0, 1, 0, 1, 1.0)
    return geom, 1.0

if __name__ == '__main__':
    import meshio
    geometry, _ = generate()
    with open('factory.geo', 'w') as f:
        f.write(geometry.get_code())
    out = pg.generate_mesh(geometry)
    meshio.write('factory.vtu', *out)
