#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_lib import (
    lib_fixups_user_type,
    lib_fixups,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'vendor/oneplus/sm8150-common',
    'device/oneplus/sm8150-common',
    'vendor/qcom/common/vendor/media-legacy',
]

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
}

module = ExtractUtilsModule(
    'oneplus7',
    'oneplus',
    namespace_imports=namespace_imports,
    lib_fixups=lib_fixups,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm8150-common', module.vendor
    )
    utils.run()
