# Copyright (c) 2020, Moritz E. Beber.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Ensure the expected behaviour of the code element."""


import pytest

from structurizr.model.code_element import CodeElement


@pytest.mark.parametrize(
    "attributes",
    [{}],
)
def test_code_element_init(attributes):
    """Expect proper initialization from arguments."""
    element = CodeElement(**attributes)
    for attr, expected in attributes.items():
        assert getattr(element, attr) == expected
