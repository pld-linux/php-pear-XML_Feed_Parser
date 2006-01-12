%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	Feed_Parser
%define		_status		beta
%define		_pearname	XML_Feed_Parser

Summary:	%{_pearname} - unified API for handling RSS and ATOM feeds
Summary(pl):	%{_pearname} - zunifikowane API do obs³ugi ¼róde³ RSS i ATOM
Name:		php-pear-%{_pearname}
Version:	0.3.0
Release:	1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}beta.tgz
# Source0-md5:	59ec155424b1b06e44cdbafe39093dad
URL:		http://pear.php.net/package/XML_Feed_Parser/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML_Feed_Parser is a parser for (the various) RSS and ATOM format XML
feeds. It attempts to provide a somewhat unified API while still
allowing access to the full details of each feed type.

In PEAR status of this package is: %{_status}.

%description -l pl
XML_Feed_Parser jest parserem dla (ró¿nych) formatów XML ¼róde³ RSS i
ATOM. Klasa ta stara siê dostarczyc zunifikowanego API przy
jednoczesnej mo¿liwo¶ci dostêpu do pe³nych informacji dotycz±cych
ka¿dego ¼ród³a.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

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
%{php_pear_dir}/XML/Feed/Parser.php
%{php_pear_dir}/XML/Feed/Parser
%{php_pear_dir}/data/XML_Feed_Parser/samples/

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/XML_Feed_Parser/tests/
