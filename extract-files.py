#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)

from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/infinix/X6739',
    'hardware/mediatek',
    'hardware/mediatek/libmtkperf_client',
    'hardware/transsion',
]

def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    ('vendor.mediatek.hardware.videotelephony@1.0',): lib_fixup_vendor_suffix,
}

blob_fixups: blob_fixups_user_type = {
    'system_ext/lib64/libsource.so': blob_fixup()
        .add_needed('libui_shim.so'),
    ('vendor/bin/hw/android.hardware.gnss-service.mediatek', 'vendor/lib64/hw/android.hardware.gnss-impl-mediatek.so'): blob_fixup()
        .replace_needed('android.hardware.gnss-V1-ndk_platform.so', 'android.hardware.gnss-V1-ndk.so'),
    'vendor/bin/hw/android.hardware.media.c2@1.2-mediatek-64b': blob_fixup()
        .add_needed('libstagefright_foundation-v33.so')
        .replace_needed('libavservices_minijail_vendor.so', 'libavservices_minijail.so'),
    ('vendor/bin/hw/camerahalserver', 'vendor/bin/hw/vendor.mediatek.hardware.pq@2.2-service'): blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.transsion.so')
        .replace_needed('libbinder.so', 'libbinder-v32.so')
        .replace_needed('libhidlbase.so', 'libhidlbase-v32.so'),
    'vendor/lib64/hw/android.hardware.camera.provider@2.6-impl-mediatek.so': blob_fixup()
        .add_needed('libshim_camera_metadata.so'),
    'vendor/etc/init/android.hardware.media.c2@1.2-mediatek.rc': blob_fixup()
        .regex_replace('@1.2-mediatek', '@1.2-mediatek-64b'),
    ('vendor/lib/hw/audio.primary.mt6893.so', 'vendor/lib64/hw/audio.primary.mt6893.so'): blob_fixup()
        .replace_needed('libutils.so', 'libutils-v32.transsion.so')
        .replace_needed('libalsautils.so', 'libalsautils-v31.so'),
    'vendor/etc/vintf/manifest/manifest_media_c2_V1_2_default.xml': blob_fixup()
        .regex_replace('1.1', '1.2'),
    ('vendor/lib/libalsautils-v31.so', 'vendor/lib64/libalsautils-v31.so'): blob_fixup()
        .fix_soname(),
    ('vendor/lib64/mt6893/libneuralnetworks_sl_driver_mtk_prebuilt.so',
     'vendor/lib64/libstfactory-vendor.so',
     'vendor/lib/libnvram.so',
     'vendor/lib64/libnvram.so',
     'vendor/lib/libsysenv.so',
     'vendor/lib64/libsysenv.so',
     'vendor/lib/libtflite_mtk.so',
     'vendor/lib64/libtflite_mtk.so'): blob_fixup()
        .add_needed('libbase_shim.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'X6739',
    'infinix',
    blob_fixups=blob_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
