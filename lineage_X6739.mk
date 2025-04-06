#
# Copyright (C) 2023 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit from device makefile.
$(call inherit-product, device/infinix/X6739/device.mk)

# Inherit some common LineageOS stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

AXION_CAMERA_REAR_INFO := 108,2,2
 AXION_CAMERA_FRONT_INFO := 32
 AXION_MAINTAINER := xoo2001
 AXION_PROCESSOR := Mediatek_Dimensity_8050
 AXION_CPU_SMALL_CORES := 0,1,2,3,4,5
 AXION_CPU_BIG_CORES := 6,7

# AxionOS scheduling properties
 PRODUCT_SYSTEM_PROPERTIES += \
     persist.sys.axion_cpu_big=$(AXION_CPU_BIG_CORES) \
     persist.sys.axion_cpu_small=$(AXION_CPU_SMALL_CORES)

TARGET_DISABLE_EPPE := true
PRODUCT_NAME := lineage_X6739
PRODUCT_DEVICE := X6739
PRODUCT_MANUFACTURER := INFINIX
PRODUCT_BRAND := Infinix
PRODUCT_MODEL := Infinix X6739

PRODUCT_GMS_CLIENTID_BASE := android-transsion

PRODUCT_BUILD_PROP_OVERRIDES += \
    DeviceName=X6739 \
    BuildFingerprint=Infinix/X6739-GL/Infinix-X6739:12/SP1A.210812.016/241017V722:user/release-keys
