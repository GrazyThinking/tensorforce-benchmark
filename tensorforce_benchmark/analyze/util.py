# Copyright 2017 reinforce.io. All Rights Reserved.
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
# ==============================================================================

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np


def n_step_average(data, n):
    """
    Average data over n steps.

    Args:
        data: np.array containing the ata
        n: steps to average over

    Returns: np.array of size n containing the average of the respective bins

    """
    if len(data) < n:
        n = len(data)

    cut = data[0:len(data)-len(data)%n]  # cut array so it's divisible by n
    return np.mean(cut.reshape(-1, len(data) // n), axis=1)
