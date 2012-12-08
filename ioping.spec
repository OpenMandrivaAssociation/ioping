Summary:	simple disk I/O latency measuring tool
Name:		ioping
Version:	0.6
Release:	1
License:	GPLv3+
Group:		System/Configuration/Hardware
Source0:	http://ioping.googlecode.com/files/%{name}-%{version}.tar.gz
URL:		http://code.google.com/p/ioping/

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
%defattr(644,root,root,755)
%{_mandir}/man1/ioping.1*
%attr(755,root,root) %{_bindir}/*


%changelog
* Fri Jan 13 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.6-1
+ Revision: 760626
- imported package ioping

