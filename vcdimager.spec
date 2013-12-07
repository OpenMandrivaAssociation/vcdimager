%define major 0
%define libname %mklibname vcd %{major}
%define develname %mklibname -d vcd
%define staticname %mklibname -s -d vcd

Name:		vcdimager
Version:	0.7.24
Release:	7
Summary:	VideoCD (pre-)mastering and ripping tool
License:	GPL
Group:		Video
Source:		ftp://ftp.gnu.org/gnu/vcdimager/%name-%version.tar.gz
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
%configure2_5x --enable-maintainer-mode
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


%changelog
* Fri Jun 08 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.7.24-3
+ Revision: 803524
- Remove harmful *.la files breaking the vlc build
- Clean up spec file

* Thu Oct 27 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.7.24-2
+ Revision: 707553
- rebuild for new libcdio

* Wed Jun 15 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.7.24-1
+ Revision: 685450
- fix devel package name
- new version
- fix source URL

* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 0.7.23-11
+ Revision: 670763
- mass rebuild

* Fri Dec 03 2010 Tomas Kindl <supp@mandriva.org> 0.7.23-10mdv2011.0
+ Revision: 606609
- rebuild
- SPEC cleanups

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.7.23-9mdv2010.0
+ Revision: 427490
- rebuild

* Mon Oct 27 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.7.23-8mdv2009.1
+ Revision: 297784
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.7.23-7mdv2009.0
+ Revision: 225916
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 0.7.23-6mdv2008.1
+ Revision: 179677
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.23-5mdv2008.0
+ Revision: 90343
- rebuild


* Fri Jan 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.7.23-4mdv2007.0
+ Revision: 108129
- Import vcdimager

* Fri Jan 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.7.23-4mdv2007.1
- Rebuild

* Wed Mar 22 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.7.23-3mdk
- rebuild for new libiso9660 (x86_64)

* Sat Mar 18 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.7.23-2mdk
- rebuild for new libcdio
- use mkrel

* Wed Jul 13 2005 Götz Waschk <waschk@mandriva.org> 0.7.23-1mdk
- new version

* Wed May 18 2005 Götz Waschk <waschk@mandriva.org> 0.7.22-1mdk
- new source URL
- New release 0.7.22

* Tue Apr 19 2005 Götz Waschk <waschk@linux-mandrake.com> 0.7.21-3mdk
- rebuild for new libcdio

* Wed Feb 02 2005 Götz Waschk <waschk@linux-mandrake.com> 0.7.21-2mdk
- rebuild for new libcdio

* Wed Dec 08 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7.21-1mdk
- new source URL
- new version

* Mon Nov 22 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7.21-0.20041121.1mdk
- drop patches
- new snapshot for new libcdio

* Wed Nov 10 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7.20-5mdk
- rebuild for new libcdio

* Sat Jul 10 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7.20-4mdk
- drop generic docs
- reenable libtoolize
- patch 1 to fix build

* Sat Apr 03 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7.20-3mdk
- fix source url
- build against libcdio 0.68
- fix pkgconfig file
- don't run libtoolize
- official final vcdimager

* Sat Jan 17 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7.20-2mdk
- fix deps

* Thu Jan 15 2004 Götz Waschk <waschk@linux-mandrake.com> 0.7.20-1mdk
- enable maintainer mode for the man pages
- requires new libcdio
- use the mdkversion macro
- new version

