Summary:	Extreme Happy Netflow Tool
Summary(pl):	Extreme Happy Netflow Tool - narzêdzie do wyci±gania statystyk ruchu
Name:		ehnt
Version:	0.3
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/ehnt/%{name}-%{version}.tar.gz
# Source0-md5:	1477137f5207561cafb421864351562d
Source1:	http://dl.sourceforge.net/ehnt/%{name}_data-%{version}.tar.gz
# Source1-md5:	b861e0fb0092c45c71b9048e9a4b1679
Patch0:		%{name}-colondump.patch
Patch1:		%{name}-asnc_path.patch
URL:		http://ehnt.sourceforge.net/
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EHNT is a software to get some useful information from
Cisco/Juniper/Foundry netflow without too much trouble.

%description -l pl
EHNT to oprogramowanie do wyci±gania przydatnych informacji ze
statystyk generowanych przez routery Cisco/Juniper/Foundry, znanych
jako netflow.

%prep
%setup -q -b 1
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install ehnt ehntserv $RPM_BUILD_ROOT%{_bindir}
install asnc.txt $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG CREDITS INSTALL KNOWN_BUGS NOTES TODO README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
