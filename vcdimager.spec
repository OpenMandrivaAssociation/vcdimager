%define release %mkrel 4
%define version 0.7.23
%define name	vcdimager

%define major 0
%define libname %mklibname vcd %{major}
%define cdiover 0.72

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	VideoCD (pre-)mastering and ripping tool
License:	GPL
Group:          Video
Source:         http://www.vcdimager.org/pub/vcdimager/vcdimager-0.7/%name-%version.tar.bz2
URL:            http://www.vcdimager.org
BuildRoot:      %{_tmppath}/%{name}-buildroot
BuildRequires:  libxml2-devel
BuildRequires:  libcdio-devel >= %cdiover
BuildRequires:  popt-devel
BuildRequires:  automake1.8

%description 
VCDImager allows you to create VideoCD BIN/CUE CD images from mpeg
files which can be burned with cdrdao or any other program capable of
burning BIN/CUE files.

VCDRip, which comes with VCDImager, does the reverse operation. That
is, ripping mpeg streams from images (and already burned VideoCDs)
and showing some information about the VideoCD.

%package -n %{libname}
Summary: Libraries from %name
Group: System/Libraries
Provides: libvcd = %version-%release
Requires: libcdio >= %cdiover

%description -n %{libname}
VCDImager allows you to create VideoCD BIN/CUE CD images from mpeg
files which can be burned with cdrdao or any other program capable of
burning BIN/CUE files.

VCDRip, which comes with VCDImager, does the reverse operation. That
is, ripping mpeg streams from images (and already burned VideoCDs)
and showing some information about the VideoCD.

%package -n %{libname}-devel
Summary: Devel files from %name
Group: Development/C
Requires: %{libname} = %version
Requires: libcdio-devel >= %cdiover
Provides: libvcd-devel = %version-%release 

 
%description -n %{libname}-devel
This is the libraries, include files and other resources you can use
to incorporate %name into applications.

%package -n %libname-static-devel 
Summary: Static Library for developing applications with %name
Group: Development/C
Requires: %libname-devel = %version

%description -n %libname-static-devel
This contains the static library of %name needed for building apps that
link statically to %name.


%prep
rm -rf $RPM_BUILD_ROOT

%setup -q 

%build
%configure2_5x --enable-maintainer-mode
%make

%install
rm -rf "$RPM_BUILD_ROOT"
%makeinstall_std
 
%clean
rm -rf "$RPM_BUILD_ROOT"

%post
%_install_info vcdimager.info

%preun
%_remove_install_info vcdimager.info

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig


%files
%defattr(-, root, root)
%doc NEWS README
%{_bindir}/vcd-info
%{_bindir}/vcdimager
%{_bindir}/vcdxgen
%{_bindir}/vcdxrip
%{_bindir}/vcdxbuild
%{_bindir}/vcdxminfo
%{_bindir}/cdxa2mpeg
%{_infodir}/*
%{_mandir}/man1/*
%files -n %{libname}
%defattr (- ,root,root)
%_libdir/*.so.*

%files -n %{libname}-devel
%defattr(-, root, root)
%doc ChangeLog AUTHORS TODO
%_includedir/libvcd
%_libdir/*.so
%_libdir/*.la
%_libdir/pkgconfig/*.pc

%files -n %libname-static-devel
%defattr(-,root,root)
%{_libdir}/lib*.a


