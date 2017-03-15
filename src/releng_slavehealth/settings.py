# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from __future__ import absolute_import

import os


SWAGGER_BASE_URL = os.environ.get('SWAGGER_BASE_URL')
DATABASE_URL = os.environ.get('DATABASE_URL')

# commented our since database is not needed initially
# if not DATABASE_URL:
#     raise Exception("You need to specify DATABASE_URL variable.")


SQLALCHEMY_DATABASE_URI = DATABASE_URL
SQLALCHEMY_TRACK_MODIFICATIONS = False


IGNORE_SLAVE_TYPES = ['try-linux64-ec2',
                      'tst-linux64-ec2',
                      'tst-linux32-ec2',
                      't-mavericks-r5',
                      'b-2008-sm',
                      'tst-w64-ec2',
                      'av-linux64']
