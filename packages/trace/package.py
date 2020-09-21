# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install trace
#
# You can edit this file again by typing:
#
#     spack edit trace
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import os
from spack.util.environment import EnvironmentModifications

class Trace(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://cdcvs.fnal.gov/redmine/projects/trace"
    git      = "http://cdcvs.fnal.gov/projects/trace-git"

    version('stable', branch='stable')
    version('3.15.09', commit='f429a6a8b52925c31678cab5643f67df16f06fd5')

    patch('install-scripts.diff')
        
    def setup_run_environment(self, env):
        trace_fns=self.prefix.bin.join("trace_functions.sh")
        if os.path.isfile(trace_fns):
            env.extend(EnvironmentModifications.from_sourcing_file(trace_fns))
