#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mediasdk
Version  : 18.4.0
Release  : 10
URL      : https://github.com/Intel-Media-SDK/MediaSDK/archive/intel-mediasdk-18.4.0.tar.gz
Source0  : https://github.com/Intel-Media-SDK/MediaSDK/archive/intel-mediasdk-18.4.0.tar.gz
Summary  : GoogleTest (with main() function)
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT
Requires: mediasdk-data = %{version}-%{release}
Requires: mediasdk-lib = %{version}-%{release}
Requires: mediasdk-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : googletest-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libdrm_intel)
BuildRequires : pkgconfig(libmfx)
BuildRequires : pkgconfig(libva)
BuildRequires : pkgconfig(libva-drm)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : pkgconfig(xcb)
BuildRequires : pkgconfig(xcb-dri3)
BuildRequires : pkgconfig(xcb-present)
BuildRequires : python3
Patch1: 0001-remove-failing-test-during-compilation.patch

%description
# embed_isa helper tool
embed_isa is a simple application which generates c-array from the binary kernel ISA file. Usage:
```sh
embed_isa <kernel_file>.isa
```
On the output you will get 2 files:
1. <kernel_file>_isa.h header file of the format similar to:
```sh
#ifndef __<kernel_file>__
#define __<kernel_file>__
extern const unsigned char <kernel_file>[<size>];
#endif
```
2. <kernel_file>_isa.cpp source file with the kernel c-style array in the format similar to:
```sh
#include "<kernel_file>_isa.h"

%package data
Summary: data components for the mediasdk package.
Group: Data

%description data
data components for the mediasdk package.


%package dev
Summary: dev components for the mediasdk package.
Group: Development
Requires: mediasdk-lib = %{version}-%{release}
Requires: mediasdk-data = %{version}-%{release}
Provides: mediasdk-devel = %{version}-%{release}

%description dev
dev components for the mediasdk package.


%package lib
Summary: lib components for the mediasdk package.
Group: Libraries
Requires: mediasdk-data = %{version}-%{release}
Requires: mediasdk-license = %{version}-%{release}

%description lib
lib components for the mediasdk package.


%package license
Summary: license components for the mediasdk package.
Group: Default

%description license
license components for the mediasdk package.


%prep
%setup -q -n MediaSDK-intel-mediasdk-18.4.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549417611
mkdir -p clr-build
pushd clr-build
%cmake .. -DENABLE_WAYLAND=true -DENABLE_X11=true -DBUILD_TESTS=ON -DINSTALL_GTEST=OFF -DBUILD_MOCK=OFF
make  %{?_smp_mflags}
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test

%install
export SOURCE_DATE_EPOCH=1549417611
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mediasdk
cp LICENSE %{buildroot}/usr/share/package-licenses/mediasdk/LICENSE
cp googletest/LICENSE %{buildroot}/usr/share/package-licenses/mediasdk/googletest_LICENSE
cp googletest/googlemock/LICENSE %{buildroot}/usr/share/package-licenses/mediasdk/googletest_googlemock_LICENSE
cp googletest/googlemock/scripts/generator/LICENSE %{buildroot}/usr/share/package-licenses/mediasdk/googletest_googlemock_scripts_generator_LICENSE
cp googletest/googletest/LICENSE %{buildroot}/usr/share/package-licenses/mediasdk/googletest_googletest_LICENSE
pushd clr-build
%make_install
popd
## install_append content
rm -rf %{buildroot}/usr/share/mfx/samples
rm -rf %{buildroot}/usr/share/mfx/tests
## install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/mfx/plugins.cfg

%files dev
%defattr(-,root,root,-)
/usr/include/mfx/mfxastructures.h
/usr/include/mfx/mfxaudio++.h
/usr/include/mfx/mfxaudio.h
/usr/include/mfx/mfxbrc.h
/usr/include/mfx/mfxcamera.h
/usr/include/mfx/mfxcommon.h
/usr/include/mfx/mfxdefs.h
/usr/include/mfx/mfxdispatcherprefixedfunctions.h
/usr/include/mfx/mfxenc.h
/usr/include/mfx/mfxfei.h
/usr/include/mfx/mfxfeihevc.h
/usr/include/mfx/mfxjpeg.h
/usr/include/mfx/mfxla.h
/usr/include/mfx/mfxmvc.h
/usr/include/mfx/mfxpak.h
/usr/include/mfx/mfxplugin++.h
/usr/include/mfx/mfxplugin.h
/usr/include/mfx/mfxsc.h
/usr/include/mfx/mfxscd.h
/usr/include/mfx/mfxsession.h
/usr/include/mfx/mfxstructures.h
/usr/include/mfx/mfxvideo++.h
/usr/include/mfx/mfxvideo.h
/usr/include/mfx/mfxvp8.h
/usr/include/mfx/mfxvp9.h
/usr/include/mfx/mfxvstructures.h
/usr/lib64/libmfx.so
/usr/lib64/libmfxhw64.so
/usr/lib64/pkgconfig/libmfx.pc
/usr/lib64/pkgconfig/libmfxhw64.pc
/usr/lib64/pkgconfig/mfx.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmfx.so.1
/usr/lib64/libmfx.so.1.28
/usr/lib64/libmfxhw64.so.1
/usr/lib64/libmfxhw64.so.1.28
/usr/lib64/mfx/libmfx_h264la_hw64.so
/usr/lib64/mfx/libmfx_hevc_fei_hw64.so
/usr/lib64/mfx/libmfx_hevcd_hw64.so
/usr/lib64/mfx/libmfx_hevce_hw64.so
/usr/lib64/mfx/libmfx_vp8d_hw64.so
/usr/lib64/mfx/libmfx_vp9d_hw64.so
/usr/lib64/mfx/libmfx_vp9e_hw64.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mediasdk/LICENSE
/usr/share/package-licenses/mediasdk/googletest_LICENSE
/usr/share/package-licenses/mediasdk/googletest_googlemock_LICENSE
/usr/share/package-licenses/mediasdk/googletest_googlemock_scripts_generator_LICENSE
/usr/share/package-licenses/mediasdk/googletest_googletest_LICENSE
