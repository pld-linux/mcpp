Summary:	A C/C++ preprocessor
Summary(pl.UTF-8):	Preprocesor dla języków C/C++
Name:		mcpp
Version:	2.7.2
Release:	3
License:	BSD-like (see LICENSE)
Group:		Applications
Source0:	http://downloads.sourceforge.net/mcpp/%{name}-%{version}.tar.gz
# Source0-md5:	512de48c87ab023a69250edc7a0c7b05
# Extracted from http://www.zeroc.com/download/Ice/3.4/ThirdParty-Sources-3.4.2.tar.gz
Patch0:		patch.mcpp.2.7.2
URL:		http://mcpp.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
Mcpp is a C/C++ preprocessor.

%description -l pl.UTF-8
Mcpp to preprocesor dla języków C/C++

%package devel
Summary:	Header files for mcpp library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki mcpp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for mcpp library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki mcpp.

%package static
Summary:	Static mcpp library
Summary(pl.UTF-8):	Statyczna biblioteka mcpp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static mcpp library.

%description static -l pl.UTF-8
Statyczna biblioteka mcpp.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--enable-mcpplib
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README LICENSE doc/mcpp-manual.html
%attr(755,root,root) %{_bindir}/mcpp
%attr(755,root,root) %{_libdir}/libmcpp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmcpp.so.0
%{_mandir}/man1/mcpp.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/mcpp_*.h
%attr(755,root,root) %{_libdir}/libmcpp.so
%{_libdir}/libmcpp.la

%files static
%defattr(644,root,root,755)
%{_libdir}/libmcpp.a
