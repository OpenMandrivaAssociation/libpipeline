%define major %(echo %{version} |cut -d. -f1)
%define libname %mklibname pipeline %{major}
%define devname %mklibname pipeline -d

Summary:	Library for manipulating pipelines of subprocesses
Name:		libpipeline
Version:	1.5.7
Release:	2
Group:		System/Libraries
License:	GPLv3+
Url:		https://libpipeline.nongnu.org/
Source0:	https://download.savannah.nongnu.org/releases/%{name}/%{name}-%{version}.tar.gz
Patch0:		libpipeline-1.5.6-fix-clang.patch

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
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files for %{name}, a library
for manipluating pipelines of subprocesses

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/libpipeline.so.%{major}*

%files -n %{devname}
%doc COPYING NEWS.md README.md
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%doc %{_mandir}/man3/*
