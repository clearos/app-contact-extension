
Name: app-contact-extension
Epoch: 1
Version: 2.1.6
Release: 1%{dist}
Summary: Contact Extension - Core
License: LGPLv3
Group: ClearOS/Libraries
Source: app-contact-extension-%{version}.tar.gz
Buildarch: noarch

%description
The Contact Extension extends the directory with user contact information such as phone number, mobile, and address.

%package core
Summary: Contact Extension - Core
Requires: app-base-core
Requires: app-openldap-directory-core
Requires: app-organization
Requires: app-users

%description core
The Contact Extension extends the directory with user contact information such as phone number, mobile, and address.

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/contact_extension
cp -r * %{buildroot}/usr/clearos/apps/contact_extension/

install -D -m 0644 packaging/contact.php %{buildroot}/var/clearos/openldap_directory/extensions/72_contact.php

%post core
logger -p local6.notice -t installer 'app-contact-extension-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/contact_extension/deploy/install ] && /usr/clearos/apps/contact_extension/deploy/install
fi

[ -x /usr/clearos/apps/contact_extension/deploy/upgrade ] && /usr/clearos/apps/contact_extension/deploy/upgrade

exit 0

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-contact-extension-core - uninstalling'
    [ -x /usr/clearos/apps/contact_extension/deploy/uninstall ] && /usr/clearos/apps/contact_extension/deploy/uninstall
fi

exit 0

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/contact_extension/packaging
%dir /usr/clearos/apps/contact_extension
/usr/clearos/apps/contact_extension/deploy
/usr/clearos/apps/contact_extension/language
/usr/clearos/apps/contact_extension/libraries
/var/clearos/openldap_directory/extensions/72_contact.php
