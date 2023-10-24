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

from pyasic.miners.backends import BOSMiner
from pyasic.miners.types import S19, S19j, S19jNoPIC, S19jPro, S19Pro


class BOSMinerS19(BOSMiner, S19):
    pass


class BOSMinerS19Pro(BOSMiner, S19Pro):
    pass


class BOSMinerS19j(BOSMiner, S19j):
    pass


class BOSMinerS19jNoPIC(BOSMiner, S19jNoPIC):
    pass


class BOSMinerS19jPro(BOSMiner, S19jPro):
    pass
