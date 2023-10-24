# Copyright (C) 2023-present The Project Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from abc import ABC, abstractmethod
from typing import Any, Dict


class Data(ABC):
    """Abstract base class for serializable data.

    The use of this class is optional. The code must not rely on inheritance from this class, but only on the
    presence of its methods. These methods may be implemented without using any specific base or mixin class.

    Final data classes must implement the following methods and properties. Some of them may be implemented
    by mixins or intermediate base classes, including those using dataclass and similar frameworks. Implementing
    these methods makes it possible to use the class for fields of records stored in a data source.

    * to_dict(self) - instance method serializing self as dictionary
    * from_dict(self, data_dict) - instance method populating self from dictionary
    """

    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """Serialize self as dictionary (must return deep copy of data in self)."""

    @abstractmethod
    def from_dict(self, data: Dict[str, Any]) -> None:
        """Populate self from dictionary (must clear the existing data in self and perform deep copy of argument)."""
