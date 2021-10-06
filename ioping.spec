Summary:	simple disk I/O latency measuring tool
Name:		ioping
Version:	1.2
Release:	1
License:	GPLv3+
Group:		System/Configuration/Hardware
Url:		https://github.com/koct9i/ioping
Source0:	https://github.com/koct9i/ioping/archive/v%{version}/%{name}-%{version}.tar.gz

%description
This tool lets you monitor I/O latency in real time, in a way similar
to how ping(1) does for network latency.

%prep
%autosetup -p1

%build
export CFLAGS="-Wextra -pedantic -funroll-loops -ftree-vectorize %{optflags}"
export LDFLAGS="%{build_ldflags}"
%make_build

%install
%make_install PREFIX=%{_prefix}

%files
%doc changelog README.md
%license LICENSE
%{_bindir}/ioping
%doc %{_mandir}/man1/ioping.1*