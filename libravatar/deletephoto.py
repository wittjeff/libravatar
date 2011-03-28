#!/usr/bin/python
# Copyright (C) 2011  Francois Marier <francois@libravatar.org>
#
# This file is part of Libravatar
# 
# Libravatar is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Libravatar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with Libravatar.  If not, see <http://www.gnu.org/licenses/>.

import json
import sys

import settings # pylint: disable=W0403
from utils import delete_if_exists, is_hex # pylint: disable=W0403

def main(argv=None):
    if argv is None:
        argv = sys.argv

    gearman_workload = sys.stdin.read()
    params = json.loads(gearman_workload)

    file_hash = params['file_hash']
    file_format = params['format']

    # Validate inputs
    if not is_hex(file_hash):
        return 1
    if file_format != 'jpg' and file_format != 'png':
        return 1

    filename = "%s.%s" % (file_hash, file_format)
    delete_if_exists(settings.UPLOADED_FILES_ROOT + filename)
    delete_if_exists(settings.USER_FILES_ROOT + filename)

    return 0

if __name__ == "__main__":
    sys.exit(main())
