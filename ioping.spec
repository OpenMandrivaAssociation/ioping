Summary:	simple disk I/O latency measuring tool
Name:		ioping
Version:	0.6
Release:	4
License:	GPLv3+
Group:		System/Configuration/Hardware
Url:		http://code.google.com/p/ioping/
Source0:	http://ioping.googlecode.com/files/%{name}-%{version}.tar.gz

%description
This tool lets you monitor I/O latency in real time, in a way similar
to how ping(1) does for network latency.


%prep
%setup -q

%build
%make

%install
%makeinstall_std \
	PREFIX="%{_prefix}" \
	DESTDIR=%{buildroot}

%files
%{_bindir}/*
%{_mandir}/man1/ioping.1*

