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

TARGET_DISABLE_EPPE := true
PRODUCT_NAME := lineage_X6739
PRODUCT_DEVICE := X6739
PRODUCT_MANUFACTURER := INFINIX
PRODUCT_BRAND := Infinix
PRODUCT_MODEL := Infinix X6739

PRODUCT_GMS_CLIENTID_BASE := android-transsion

PRODUCT_BUILD_PROP_OVERRIDES += \
    DeviceName=X6739 \
    RisingMaintainer="Eko Rudianto (xoo2001)" \
    RisingChipset="Mediatek Dimensity 8050" \
    BuildFingerprint=Infinix/X6739-GL/Infinix-X6739:12/SP1A.210812.016/241017V722:user/release-keys

WITH_GMS := true
TARGET_CORE_GMS := true
PRODUCT_PACKAGES += \
   MarkupGoogle \
   LatinIMEGooglePrebuilt \
   Velvet \
   AvatarPicker \
   PrebuiltDeskClockGoogle

PRODUCT_NO_CAMERA := false
TARGET_BOOT_ANIMATION_RES := 1080
TARGET_SUPPORTS_QUICK_TAP := true
TARGET_HAS_UDFPS := false
TARGET_USE_GOOGLE_TELEPHONY := true
RISING_MAINTAINER := Eko Rudianto (xoo2001)

