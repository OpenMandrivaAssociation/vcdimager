%define version 0.7.24
%define name	vcdimager

%define major 0
%define libname %mklibname vcd %{major}
%define develname %mklibname -d vcd
%define staticname %mklibname -s -d vcd
%define cdiover 0.72

Name:		%{name}
Version:	%{version}
Release:	%mkrel 1
Summary:	VideoCD (pre-)mastering and ripping tool
License:	GPL
Group:		Video
Source:		ftp://ftp.gnu.org/gnu/vcdimager/%name-%version.tar.gz
URL:		http://www.vcdimager.org
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libxml2-devel
BuildRequires:	libcdio-devel >= %cdiover
BuildRequires:	popt-devel
BuildRequires:	automake1.8

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

%package -n %{develname}
Summary: Devel files from %name
Group: Development/C
Requires: %{libname} = %version
Requires: libcdio-devel >= %cdiover
Provides: libvcd-devel = %version-%release 
Obsoletes: %{mklibname -d vcd 0}

 
%description -n %{develname}
This is the libraries, include files and other resources you can use
to incorporate %name into applications.

%package -n %staticname
Summary: Static Library for developing applications with %name
Group: Development/C
Requires: %develname = %version
Obsoletes: %{mklibname -s -d vcd 0}

%description -n %staticname
This contains the static library of %name needed for building apps that
link statically to %name.


%prep

%setup -q 

%build
%configure2_5x --enable-maintainer-mode
%make

%install
rm -rf %{buildroot}
%makeinstall_std
 
%clean
rm -rf %{buildroot}

%post
%_install_info vcdimager.info

%preun
%_remove_install_info vcdimager.info



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
%_libdir/*.so.%{major}*

%files -n %develname
%defattr(-, root, root)
%doc ChangeLog AUTHORS TODO
%_includedir/libvcd
%_libdir/*.so
%_libdir/*.la
%_libdir/pkgconfig/*.pc

%files -n %staticname
%defattr(-,root,root)
%{_libdir}/lib*.a
