%define major %(echo %version |cut -d. -f1)
%define libname %mklibname pipeline %{major}
%define devname %mklibname pipeline -d

Name:		libpipeline
Version:	1.2.3
Release:	1
Summary:	Library for manipulating pipelines of subprocesses
Group:		System/Libraries
License:	GPLv3+
URL:		http://libpipeline.nongnu.org/
Source0:	http://download.savannah.nongnu.org/releases/%{name}/%{name}-%{version}.tar.gz

%description
Library for manipulating pipelines of subprocesses.

%package -n %{libname}
Summary:	Library for manipulating pipelines of subprocesses
Group:		System/Libraries

%description -n %{libname}
Library for manipulating pipelines of subprocesses

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Development files for %{name}, a library
for manipluating pipelines of subprocesses

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%doc COPYING NEWS
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_mandir}/man3/*

