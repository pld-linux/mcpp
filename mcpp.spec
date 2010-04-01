
Summary:	A C/C++ preprocessor
Summary(pl.UTF-8):	Preprocesor dla języków C/C++
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
Mcpp to preprocesor dla języków C/C++.

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
%configure
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
%{_bindir}/mcpp
%{_mandir}/man1/mcpp.1*
