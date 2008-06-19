%include	/usr/lib/rpm/macros.php
%define		_class		Event
%define		_subclass	SignalEmitter
%define		_status		beta
%define		_pearname	Event_SignalEmitter
Summary:	%{_pearname} - Generic signal emitting class with the same API as GObject
Summary(pl.UTF-8):	%{_pearname} - kompatybilna z GObject na poziomie API klasa do wysyłania sygnałów
Name:		php-pear-%{_pearname}
Version:	0.3.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	e6cb9ce1ec1749af6d122486690df640
URL:		http://pear.php.net/package/Event_SignalEmitter/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Generic signal emitting class with the same API as GObject. Since
GObject doesn't allow classes to define or emit own signals, this
class provides a PHP implementation with the same API.

In PEAR status of this package is: %{_status}.

#%description -l pl.UTF-8
#
#...
#
#Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/Event_SignalEmitter/docs/examples
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Event/SignalEmitter
%{php_pear_dir}/Event/SignalEmitter.php
