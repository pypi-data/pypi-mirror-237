# ExSource-Tools

An experimental Python library for validating and using the [ExSource Specification](https://gitlab.com/gitbuilding/exsourcespec) which is in the early stage of development.

This packages adds the following command:

    exsource-make exsource.yml

This will attempt to process `exsource.yml` to create inputs. The first instance of this proof of principle implementation supports OpenSCAD and some FreeCAD files. FreeCAD exporter will expect there to be a PartDesign Body called `Body`, it can export this to STEP and/or STL.
