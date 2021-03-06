#!/usr/bin/env python

# Copyright 2019-2020 The University of Manchester, UK
# Copyright 2020 Vlaams Instituut voor Biotechnologie (VIB), BE
# Copyright 2020 Barcelona Supercomputing Center (BSC), ES
# Copyright 2020 Center for Advanced Studies, Research and Development in Sardinia (CRS4), IT
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from .file import File


class Workflow(File):
    """\
    A scientific workflow that was used (or can be used) to analyze or
    generate files in the RO-Crate.
    """
    TYPES = ["File", "SoftwareSourceCode", "ComputationalWorkflow"]

    def _empty(self):
        return {
            "@id": self.id,
            "@type": self.TYPES,
            "name": os.path.splitext(self.id)[0],
        }


class LegacyWorkflow(Workflow):

    TYPES = ["File", "SoftwareSourceCode", "Workflow"]
