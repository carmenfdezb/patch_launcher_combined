Name:       launcher-combined

BuildArch: noarch

Summary:    Launcher Combined Patch
Version:    1.2.0
Release:    1
Group:      Qt/Qt
License:    WTFPL
Source0:    %{name}-%{version}.tar.bz2
Requires:   patchmanager
URL:        https://github.com/carmenfdezb

%description
Changes launcher grid size and adds new icon style showing folder icons

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/patchmanager/patches/%{name}
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/%{name}

%pre
if [ -d /var/lib/patchmanager/ausmt/patches/%{name} ]; then
/usr/sbin/patchmanager -u %{name} || true
fi

%preun
if [ -d /var/lib/patchmanager/ausmt/patches/%{name} ]; then
/usr/sbin/patchmanager -u %{name} || true
fi

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/%{name}

%changelog
* Sat May 25 2024 Carmen Fdez. B. 1.2.0-1
-Support for SFOS 4.6

* Fri Feb 03 2023 Carmen Fdez. B. 1.1.0-1
- Support for SFOS 4.5.0

* Sun Aug 07 2022 Carmen Fdez. B. 1.0.0-1
- Original patch by Coderus adapted to 4.4.0.64
