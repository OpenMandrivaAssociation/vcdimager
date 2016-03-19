%define major 0
%define libname %mklibname vcd %{major}
%define develname %mklibname -d vcd
%define staticname %mklibname -s -d vcd
%define _disable_rebuild_configure 1
%define _disable_lto 1

Name:		vcdimager
Version:	0.7.24
Release:	15
Summary:	VideoCD (pre-)mastering and ripping tool
License:	GPL
Group:		Video
Source0:	ftp://ftp.gnu.org/gnu/vcdimager/%{name}-%{version}.tar.gz
URL:		http://www.vcdimager.org
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libcdio)
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
Summary:	Libraries from %{name}
Group:		System/Libraries
Provides:	libvcd = %{version}-%{release}

%description -n %{libname}
VCDImager allows you to create VideoCD BIN/CUE CD images from mpeg
files which can be burned with cdrdao or any other program capable of
burning BIN/CUE files.

VCDRip, which comes with VCDImager, does the reverse operation. That
is, ripping mpeg streams from images (and already burned VideoCDs)
and showing some information about the VideoCD.

%package -n %{develname}
Summary:	Devel files from %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	pkgconfig(libcdio)
Provides:	libvcd-devel = %{version}-%{release}

%description -n %{develname}
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%package -n %{staticname}
Summary:	Static Library for developing applications with %{name}
Group:		Development/C
Requires:	%{develname} = %{version}-%{release}

%description -n %{staticname}
This contains the static library of %{name} needed for building apps that
link statically to %{name}.


%prep
%setup -q

%build
%configure --enable-static --enable-maintainer-mode
%make

%install
%makeinstall_std

%files
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
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc ChangeLog AUTHORS TODO
%{_includedir}/libvcd
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files -n %{staticname}
%{_libdir}/lib*.a


