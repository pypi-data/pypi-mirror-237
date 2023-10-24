# ------------------------------------------------------------------------------
#  Copyright 2022 Upstream Data Inc                                            -
#                                                                              -
#  Licensed under the Apache License, Version 2.0 (the "License");             -
#  you may not use this file except in compliance with the License.            -
#  You may obtain a copy of the License at                                     -
#                                                                              -
#      http://www.apache.org/licenses/LICENSE-2.0                              -
#                                                                              -
#  Unless required by applicable law or agreed to in writing, software         -
#  distributed under the License is distributed on an "AS IS" BASIS,           -
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.    -
#  See the License for the specific language governing permissions and         -
#  limitations under the License.                                              -
# ------------------------------------------------------------------------------

from pyasic.miners.backends import M5X
from pyasic.miners.types.whatsminer.M5X.M50S_Plus_Plus import (  # noqa - ignore _module import
    M50SPlusPlusVK10,
    M50SPlusPlusVK20,
    M50SPlusPlusVK30,
)


class BTMinerM50SPlusPlusVK10(  # noqa - ignore ABC method implementation
    M50SPlusPlusVK10, M5X
):
    pass


class BTMinerM50SPlusPlusVK20(  # noqa - ignore ABC method implementation
    M50SPlusPlusVK20, M5X
):
    pass


class BTMinerM50SPlusPlusVK30(  # noqa - ignore ABC method implementation
    M50SPlusPlusVK30, M5X
):
    pass
