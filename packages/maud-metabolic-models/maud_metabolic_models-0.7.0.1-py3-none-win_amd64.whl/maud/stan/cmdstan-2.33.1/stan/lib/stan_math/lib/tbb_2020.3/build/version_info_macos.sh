#!/bin/sh
#
# Copyright (c) 2005-2020 Intel Corporation
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

# Script used to generate version info string
echo "#define __TBB_VERSION_STRINGS(N) \\"
echo '#N": BUILD_HOST'"\t\t"`hostname -s`" ("`arch`")"'" ENDL \'
echo '#N": BUILD_OS'"\t\t"`sw_vers -productName`" version "`sw_vers -productVersion`'" ENDL \'
echo '#N": BUILD_KERNEL'"\t"`uname -v`'" ENDL \'
echo '#N": BUILD_CLANG'"\t"`clang --version | sed -n "1p"`'" ENDL \'
echo '#N": BUILD_XCODE'"\t"`xcodebuild -version </dev/null 2>&1 | grep 'Xcode'`'" ENDL \'
[ -z "$COMPILER_VERSION" ] || echo '#N": BUILD_COMPILER'"\t"$COMPILER_VERSION'" ENDL \'
echo '#N": BUILD_TARGET'"\t$arch on $runtime"'" ENDL \'
echo '#N": BUILD_COMMAND'"\t"$*'" ENDL \'
echo ""
echo "#define __TBB_DATETIME \""`date -u`"\""
