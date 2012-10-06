# Copyright (C) 2012 Thomas "stacks" Birn (@stacksth)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from lib.cuckoo.common.abstracts import Signature

class CreatesAutorunInf(Signature):
    name = "createsautoruninf"
    description = "Creates an autorun.inf file"
    severity = 2
    categories = ["generic"]
    authors = ["Thomas Birn"]
    minimum = "0.4.2"

    def run(self, results):
        for file_name in results["behavior"]["summary"]["files"]:
            if "autorun.inf" in file_name:
                self.data.append({"file": file_name})
                return True

        return False
