from .io import RelateBatchIO
from .report import RelateReportIO
from ..core.io import BatchedLoadedDataset, LoadedMutsDataset


class RelateLoader(BatchedLoadedDataset, LoadedMutsDataset):
    """ Load batches of relation vectors. """

    @classmethod
    def get_data_type(cls):
        return RelateBatchIO

    @classmethod
    def get_report_type(cls):
        return RelateReportIO

    @property
    def pattern(self):
        return None

########################################################################
#                                                                      #
# Copyright ©2023, the Rouskin Lab.                                    #
#                                                                      #
# This file is part of SEISMIC-RNA.                                    #
#                                                                      #
# SEISMIC-RNA is free software; you can redistribute it and/or modify  #
# it under the terms of the GNU General Public License as published by #
# the Free Software Foundation; either version 3 of the License, or    #
# (at your option) any later version.                                  #
#                                                                      #
# SEISMIC-RNA is distributed in the hope that it will be useful, but   #
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANT- #
# ABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General     #
# Public License for more details.                                     #
#                                                                      #
# You should have received a copy of the GNU General Public License    #
# along with SEISMIC-RNA; if not, see <https://www.gnu.org/licenses>.  #
#                                                                      #
########################################################################
