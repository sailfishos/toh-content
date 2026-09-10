# SPDX-FileCopyrightText: 2026 Jolla Mobile Ltd
#
# SPDX-License-Identifier: BSD-3-Clause

Name:    jolla-toh-configs
Version: 0.1.0
Release: 0
Summary: Official Jolla TOH configurations
License: BSD-3-Clause
URL:     https://github.com/sailfishos/toh-content
Source0: %{name}-%{version}.tar.bz2
BuildArch: noarch
BuildRequires: qt5-qttools-linguist
BuildRequires: qtchooser
Requires: symbiosis-examples-blinker

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}

%build
# Translations for 'Inari Blue' switch
lupdate dist/ -ts jolla-toh-configs.ts
lrelease -idbased jolla-toh-configs.ts -qm jolla-toh-configs_eng_en.qm

%post
systemctl-user daemon-reload || :

%postun
systemctl-user daemon-reload || :

%install
install -D -m0644 configs/inari_blue.yaml %{buildroot}%{_datadir}/tohd-1/tohs/0001/0004/inari_blue.yaml
install -D -m0644 configs/kaamos_black.yaml %{buildroot}%{_datadir}/tohd-1/tohs/0001/0002/kaamos_black.yaml
install -D -m0644 configs/snow_white.yaml %{buildroot}%{_datadir}/tohd-1/tohs/0001/0003/snow_white.yaml
install -D -m0644 configs/the_orange.yaml %{buildroot}%{_datadir}/tohd-1/tohs/0001/0001/the_orange.yaml
install -D -m0644 dist/EnableSwitch.qml %{buildroot}%{_datadir}/jolla-settings/pages/inari_blue/EnableSwitch.qml
install -D -m0644 dist/inari_blue.json %{buildroot}%{_datadir}/jolla-settings/entries/inari_blue.json
install -D -m0755 dist/change_ambience.sh %{buildroot}%{_libexecdir}/jolla-toh-configs/change_ambience.sh

# Enable breathing effect on Inari Blue TOH
ln -s ../../../examples/blinker.yaml %{buildroot}%{_datadir}/tohd-1/tohs/0001/0004/

# Translations for 'Inari Blue' switch
install -D -m0644 jolla-toh-configs.ts %{buildroot}%{_datadir}/translations/source/jolla-toh-configs.ts
install -D -m0644 jolla-toh-configs_eng_en.qm %{buildroot}%{_datadir}/translations/jolla-toh-configs_eng_en.qm

%files
%license LICENSES/BSD-3-Clause.txt
%{_datadir}/tohd-1/tohs/0001
%{_libexecdir}/jolla-toh-configs/change_ambience.sh
%{_datadir}/jolla-settings/pages/inari_blue
%{_datadir}/jolla-settings/entries/inari_blue.json
%{_datadir}/translations/jolla-toh-configs_eng_en.qm

%package ts-devel
Summary: Translation source for %{name}

%description ts-devel
Translation source for %{name}.

%files ts-devel
%{_datadir}/translations/source/*.ts
