#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "LightsOut"
default_task = ["install_dependencies","publish"]


@init
def set_properties(project):
    project.set_property("coverage_break_build", False)
    project.set_property("unittest_module_glob", "*_test")
    
    project.build_depends_on("tk-tools")
    project.build_depends_on("tk")
    project.build_depends_on("PySimpleGUI")
    project.build_depends_on("numpy")
