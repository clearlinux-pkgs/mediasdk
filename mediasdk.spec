#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mediasdk
Version  : 22.2.0
Release  : 41
URL      : https://github.com/Intel-Media-SDK/MediaSDK/archive/intel-mediasdk-22.2.0/MediaSDK-22.2.0.tar.gz
Source0  : https://github.com/Intel-Media-SDK/MediaSDK/archive/intel-mediasdk-22.2.0/MediaSDK-22.2.0.tar.gz
Summary  : GoogleTest (with main() function)
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT
Requires: mediasdk-lib = %{version}-%{release}
Requires: mediasdk-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : llvm
BuildRequires : llvm-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libdrm_intel)
BuildRequires : pkgconfig(libmfx)
BuildRequires : pkgconfig(libva)
BuildRequires : pkgconfig(libva-drm)
BuildRequires : pkgconfig(pciaccess)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(wayland-scanner)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : pkgconfig(xcb)
BuildRequires : pkgconfig(xcb-dri3)
BuildRequires : pkgconfig(xcb-present)
BuildRequires : python3

%description
The Google Mock class generator is an application that is part of cppclean.
For more information about cppclean, visit http://code.google.com/p/cppclean/

%package dev
Summary: dev components for the mediasdk package.
Group: Development
Requires: mediasdk-lib = %{version}-%{release}
Provides: mediasdk-devel = %{version}-%{release}
Requires: mediasdk = %{version}-%{release}

%description dev
dev components for the mediasdk package.


%package extras
Summary: extras components for the mediasdk package.
Group: Default

%description extras
extras components for the mediasdk package.


%package lib
Summary: lib components for the mediasdk package.
Group: Libraries
Requires: mediasdk-license = %{version}-%{release}

%description lib
lib components for the mediasdk package.


%package license
Summary: license components for the mediasdk package.
Group: Default

%description license
license components for the mediasdk package.


%prep
%setup -q -n MediaSDK-intel-mediasdk-22.2.0
cd %{_builddir}/MediaSDK-intel-mediasdk-22.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1644337064
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CC=clang
export CXX=clang++
export LD=ld.gold
CFLAGS=${CFLAGS/ -Wa,/ -fno-integrated-as -Wa,}
CXXFLAGS=${CXXFLAGS/ -Wa,/ -fno-integrated-as -Wa,}
unset LDFLAGS
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake .. -DENABLE_WAYLAND=true \
-DENABLE_X11=true
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1644337064
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mediasdk
cp %{_builddir}/MediaSDK-intel-mediasdk-22.2.0/LICENSE %{buildroot}/usr/share/package-licenses/mediasdk/60e25f4a5bdd75aaaa1091247a05055c9c0e1e53
cp %{_builddir}/MediaSDK-intel-mediasdk-22.2.0/NOTICE %{buildroot}/usr/share/package-licenses/mediasdk/60e25f4a5bdd75aaaa1091247a05055c9c0e1e53
cp %{_builddir}/MediaSDK-intel-mediasdk-22.2.0/contrib/googletest/LICENSE %{buildroot}/usr/share/package-licenses/mediasdk/5a2314153eadadc69258a9429104cd11804ea304
cp %{_builddir}/MediaSDK-intel-mediasdk-22.2.0/contrib/googletest/googlemock/LICENSE %{buildroot}/usr/share/package-licenses/mediasdk/5a2314153eadadc69258a9429104cd11804ea304
cp %{_builddir}/MediaSDK-intel-mediasdk-22.2.0/contrib/googletest/googlemock/scripts/generator/LICENSE %{buildroot}/usr/share/package-licenses/mediasdk/1d4719e04eaa4909ab5a59ef5cb04d2a5517716e
cp %{_builddir}/MediaSDK-intel-mediasdk-22.2.0/contrib/googletest/googletest/LICENSE %{buildroot}/usr/share/package-licenses/mediasdk/5a2314153eadadc69258a9429104cd11804ea304
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}*/usr/share/mfx/samples/libcttmetrics.so
rm -f %{buildroot}*/usr/share/mfx/samples/metrics_monitor

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/mfx/mfxadapter.h
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
/usr/include/mfx/mfxpcp.h
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

%files extras
%defattr(-,root,root,-)
/usr/share/mfx/plugins.cfg
/usr/share/mfx/samples/libmfx_wayland.so
/usr/share/mfx/samples/libsample_rotate_plugin.so
/usr/share/mfx/samples/sample_decode
/usr/share/mfx/samples/sample_encode
/usr/share/mfx/samples/sample_fei
/usr/share/mfx/samples/sample_hevc_fei
/usr/share/mfx/samples/sample_hevc_fei_abr
/usr/share/mfx/samples/sample_multi_transcode
/usr/share/mfx/samples/sample_vpp

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmfx.so.1
/usr/lib64/libmfx.so.1.35
/usr/lib64/libmfxhw64.so.1
/usr/lib64/libmfxhw64.so.1.35
/usr/lib64/mfx/libmfx_h264la_hw64.so
/usr/lib64/mfx/libmfx_hevc_fei_hw64.so
/usr/lib64/mfx/libmfx_hevcd_hw64.so
/usr/lib64/mfx/libmfx_hevce_hw64.so
/usr/lib64/mfx/libmfx_vp8d_hw64.so
/usr/lib64/mfx/libmfx_vp9d_hw64.so
/usr/lib64/mfx/libmfx_vp9e_hw64.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mediasdk/1d4719e04eaa4909ab5a59ef5cb04d2a5517716e
/usr/share/package-licenses/mediasdk/5a2314153eadadc69258a9429104cd11804ea304
/usr/share/package-licenses/mediasdk/60e25f4a5bdd75aaaa1091247a05055c9c0e1e53
