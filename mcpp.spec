
Summary:	A C/C++ preprocessor
Summary(pl.UTF-8):	Preprocesor dla j臋zyk贸w C/C++
Name:		mcpp
Version:	2.7.2
Release:	1
License:	Custom (see LICENSE)
Group:		Applications
Source0:	http://downloads.sourceforge.net/mcpp/%{name}-%{version}.tar.gz
# Source0-md5:	512de48c87ab023a69250edc7a0c7b05
URL:		http://mcpp.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mcpp is a C/C++ preprocessor.

%description -l pl.UTF-8
Mcpp to preprocesor dla j臋zyk贸w C/C++

%package devel
Summary:        Header files for ... library
Summary(pl.UTF-8):      Pliki nag?~B贸wkowe biblioteki ...
Group:          Development/Libraries
Requires:      %{name} = %{version}-%{release}

%description devel
Header files for mcpp library.

%description devel -l pl.UTF-8
Pliki nag艂贸硍kowe biblioteki mcpp.

%package static
Summary:        Static mcpp library
Summary(pl.UTF-8):      Statyczna biblioteka mcpp
Group:          Development/Libraries
Requires:       %{name}-devel = %{version}-%{release}

%description static
Static mcpp library.

%description static -l pl.UTF-8
Statyczna biblioteka mcpp.

%prep
%setup -q

%build
#%%{__intltoolize}
#%%{__gettextize}
#%%{__libtoolize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}
%configure \
	--enable-mcpplib
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README LICENSE
%attr(755,root,root) %{_bindir}/mcpp
%attr(755,root,root) %{_libdir}/libmcpp.so.0
%attr(755,root,root) %{_libdir}/libmcpp.so.0.3.0
%{_mandir}/man1/mcpp.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%{_libdir}/libmcpp.la
%{_libdir}/libmcpp.so

%files static
%defattr(644,root,root,755)
%{_libdir}/libmcpp.a
