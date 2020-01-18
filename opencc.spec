Name:       opencc
Version:    0.4.3
Release:    3%{?dist}
Summary:    Libraries for Simplified-Traditional Chinese Conversion
License:    ASL 2.0
Group:      System Environment/Libraries
URL:        http://code.google.com/p/opencc/
Source0:    http://opencc.googlecode.com/files/%{name}-%{version}.tar.gz
Patch1:     opencc-0.3.0-fixes-cmake.patch

BuildRequires:  gettext
BuildRequires:  cmake
BuildRequires:  doxygen

%description
OpenCC is a library for converting characters and phrases between
Traditional Chinese and Simplified Chinese.

%package doc
Summary:    Documentation for OpenCC
Group:      Applications/Text
Requires:   %{name} = %{version}-%{release}

%description doc
Doxygen generated documentation for OpenCC.


%package tools
Summary:    Command line tools for OpenCC
Group:      Applications/Text
Requires:   %{name} = %{version}-%{release}

%description tools
Command line tools for OpenCC, including tools for conversion via CLI and
for building dictionaries.


%package devel
Summary:    Development files for OpenCC
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch1 -p1 -b .cmake

%build
%cmake . -DENABLE_GETTEXT:BOOL=ON -DBUILD_DOCUMENTATION:BOOL=ON
make VERBOSE=1 %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

%check
ctest

%find_lang %{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%doc AUTHORS LICENSE README.md
%{_libdir}/lib*.so.*
%{_datadir}/opencc/
%exclude %{_datadir}/opencc/doc

%files doc
%{_datadir}/opencc/doc

%files tools
%{_bindir}/*
%{_datadir}/man/man1/*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.4.3-3
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.4.3-2
- Mass rebuild 2013-12-27

* Tue May 28 2013 Peng Wu <pwu@redhat.com> - 0.4.3-1
- Update to 0.4.3

* Mon Mar  4 2013 Peng Wu <pwu@redhat.com> - 0.4.0-1
- Update to 0.4.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 22 2012  Peng Wu <pwu@redhat.com> - 0.3.0-4
- Fixes Download URL

* Mon Jul 23 2012  Peng Wu <pwu@redhat.com> - 0.3.0-3
- Fixes cmake

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 02 2012  Peng Wu <pwu@redhat.com> - 0.3.0-1
- Update to 0.3.0, and fixes ctest

* Tue Feb  1 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.2.0-6
- Drop unnessary ExclusiveArch directive

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 30 2011  Peng Wu <pwu@redhat.com> - 0.2.0-4
- Change i386 to i686

* Wed Nov 30 2011  Peng Wu <pwu@redhat.com> - 0.2.0-3
- Only build for i386 and x86_64

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec 25 2010 BYVoid <byvoid.kcp@gmail.com> - 0.2.0-1
- Upstream release.
- Use CMake instead of autotools.

* Wed Sep 29 2010 jkeating - 0.1.2-2
- Rebuilt for gcc bug 634757

* Fri Sep 17 2010 BYVoid <byvoid.kcp@gmail.com> - 0.1.2-1
- Upstream release.

* Thu Aug 12 2010 BYVoid <byvoid.kcp@gmail.com> - 0.1.1-1
- Upstream release.

* Thu Jul 29 2010 BYVoid <byvoid.kcp@gmail.com> - 0.1.0-1
- Upstream release.

* Fri Jul 16 2010 BYVoid <byvoid.kcp@gmail.com> - 0.0.4-1
- Initial release of RPM.

