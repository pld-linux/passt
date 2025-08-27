%define		gitref	309eefd

Summary:	User-mode networking for virtual machines and namespaces
Name:		passt
Version:	2025_08_05
Release:	1
License:	GPL v2+, BSD
Group:		Applications/System
Source0:	https://passt.top/passt/snapshot/%{name}-%{version}.%{gitref}.tar.xz
# Source0-md5:	1de306ad0a0db6013f1c3eb8635fb4bf
URL:		https://passt.top/
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
User-mode networking for virtual machines and namespaces.

%prep
%setup -q -n %{name}-%{version}.%{gitref}

%build
%{__make} \
	VERSION="%{version}.%{gitref}" \
	TARGET="%{_target_platform}" \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	CPPFLAGS="%{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix="%{_prefix}" \
	exec_prefix="%{_exec_prefix}" \
	bindir="%{_bindir}" \
	datarootdir="%{_datadir}" \
	mandir="%{_mandir}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSES/BSD-3-Clause.txt README.plain.md
%attr(755,root,root) %{_bindir}/passt
%attr(755,root,root) %{_bindir}/passt-repair
%attr(755,root,root) %{_bindir}/pasta
%attr(755,root,root) %{_bindir}/qrap
%{_mandir}/man1/passt.1*
%{_mandir}/man1/passt-repair.1*
%{_mandir}/man1/pasta.1*
%{_mandir}/man1/qrap.1*
