%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	Feed_Parser
%define		_status		stable
%define		_pearname	XML_Feed_Parser

Summary:	%{_pearname} - unified API for handling RSS and ATOM feeds
Summary(pl):	%{_pearname} - zunifikowane API do obs�ugi �r�de� RSS i ATOM
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	1
Epoch:		0
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	af82b1d25df6ef3437d517f4f4a260cc
URL:		http://pear.php.net/package/XML_Feed_Parser/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(xml)
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# files not distributed (bug reported)
%define _noautoreq 'pear(XML/Feed/Parser/RSS11.php)' 'pear(XML/Feed/Parser/RSS11Element.php)'

%description
XML_Feed_Parser is a parser for (the various) RSS and ATOM format XML
feeds. It attempts to provide a somewhat unified API while still
allowing access to the full details of each feed type.

In PEAR status of this package is: %{_status}.

%description -l pl
XML_Feed_Parser jest parserem dla (r�nych) format�w XML �r�de� RSS i
ATOM. Klasa ta stara si� dostarczy� zunifikowanego API przy
jednoczesnej mo�liwo�ci dost�pu do pe�nych informacji dotycz�cych
ka�dego �r�d�a.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

mv ./%{php_pear_dir}/tests/%{_pearname}/{tests/*,}
rmdir ./%{php_pear_dir}/tests/%{_pearname}/tests

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log
%doc optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/XML/Feed
%{php_pear_dir}/data/XML_Feed_Parser

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/XML_Feed_Parser
